import random
import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class Visitors_Search_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().visitor_search_test_result_sheet_name()

    def verify_post_start_search_with_valid_data(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = start_search_request(self.row)

            self.response = response_list[0]
            self.json_response = response_list[1]

            if response_validation(self.response):
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Visitor_Search_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_fed_search_status_with_valid_data(self):
        start_search_request()

        # result = []
        # try:
        #     self.row = 3
        #     time_entry(self.row, "start_time", self.sheet_name)
        #     response_list = get_user_role_by_id_request()
        #     self.response = response_list[0]
        #     self.json_response = response_list[1]
        #     self.act_msg = response_list[2]
        #     self.exp_msg = response_list[3]
        #     if response_validation(self.response) and self.act_msg == self.exp_msg:
        #         excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
        #                      self.act_msg,
        #                      True, self.sheet_name)
        #         time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
        #         result.append(True)
        #     else:
        #         self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
        #         self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
        #         excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
        #                      self.act_msg,
        #                      False, self.sheet_name)
        #         time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
        #         result.append(False)
        #     if False in result:
        #         return False
        #     else:
        #         return True
        # except Exception as ex:
        #     excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
        #                  False, self.sheet_name)
        #     self.log.info(f"test_Users_Role_Test_02_Exception:  {ex}")
        #     time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
        #     return False

        ################################### Generic method #################################


def start_search_request(row_no):
    token = login_token()
    print(token)
    # image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    data = visitor_search_test_data(row_no)
    print(data)
    start_search = f"{data[0]}"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().start_search_endpoint()}"
    print(url)
    headers = {"Authorization": f"Token {token}"}
    request_data = {"threshold": data, "StartDateTime": data[1], "EndDateTime": data[2], "regionId": data[3]}
    # files = [
    #     ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    # ]
    print(request_data)
    response_str = requests.post(url, headers=headers, data=request_data)
    response_json = response_str.json()
    print(response_json)
    job_id = response_json["jobId"]
    print(job_id)
    # role_id = response_json["id"]
    return response_str, response_json, start_search, job_id


# def get_fed_search_by_job_id_request():
#     token = login_token()
#     headers = {"Authorization": f"Token {token}"}
#     job_id = create_job_id_request(2)[4]
#     url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().fed_search_status_endpoint()}"
#     response_str = requests.get(url, headers=headers)
#     response_json = response_str.json()
#     act_role_id = response_json["id"]
#     return response_str, response_json, job_id, act_role_id


def visitor_search_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().visitor_search_test_data_sheet_name(), row_no, x))
    return data


def random_number():
    r_number = random.randint(1, 100)
    return r_number
