import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities
from All_API_Methods_Package.Enrollment_Group_Module_API.Enrollment_Group_API_Methods import \
    create_enrollment_group_request, get_all_enrollment_group_request
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints


class Enrollment_Group_Data_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().enrollment_group_data_test_results_sheet_name()

    def verify_get_enrollment_group_data_by_enrollment_group_id(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            c_group_id = get_all_enrollment_group_request()[1][2]["id"]
            print(c_group_id)
            response_list = get_enrollment_group_data_by_enrollment_group_id_request(c_group_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row,"Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_01", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Enrollment_Data_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_enrollment_group_data_by_page_number_and_batch_size(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_enrollment_group_data_by_page_number_and_batch_size_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row,"Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_02", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Enrollment_Group_Data_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_enrollment_group_data_count(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_enrollment_group_data_count_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row,"Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_03", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Enrollment_Group_Data_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


def get_enrollment_group_data_by_enrollment_group_id_request(c_group_id):
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_enrollment_group_data_by_id_endpoint(c_group_id)}"
    print(url)
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_enrollment_group_data_by_page_number_and_batch_size_request():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}" \
              f"{Read_API_Endpoints().get_enrollment_group_data_by_page_number_and_batch_size_endpoint()}"
    print(url)
    query_param = {
            "pageNumber": 0,
            "batchSize": 5,
        }
    response_str = requests.get(url, headers=headers, params=query_param)
    response_json = response_str.json()
    return response_str, response_json


def get_enrollment_group_data_count_request():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_enrollment_group_data_count_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json