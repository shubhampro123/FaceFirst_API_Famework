import requests
from API_Utilities.Api_Base import API_Base_Utilities, time_entry, excel_result, login_token, login_Cookie
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_INI_Config_Files.Expected_Login_Response_Msg_read_ini import \
    Read_Expected_login_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Login_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().login_test_result_sheet_name()

    def login_with_valid_username_and_password(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = login_request(self.row)
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.r_body = response_list[3]
            self.act_msg = self.json_response["result"]["message"]
            self.exp_msg = Read_Expected_login_Response_msg().login_success_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def login_with_invalid_username_and_valid_password(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = login_request(self.row)
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.r_body = response_list[3]
            username = response_list[4]
            self.act_msg = self.json_response["result"]["message"]
            self.exp_msg = f"{Read_Expected_login_Response_msg().login_invalid_username()} '{username}'"
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def login_with_valid_username_and_invalid_password(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = login_request(self.row)
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.r_body = response_list[3]
            self.act_msg = self.json_response["result"]["message"]
            self.exp_msg = f"{Read_Expected_login_Response_msg().login_invalid_password()}"
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def login_with_invalid_username_and_invalid_password(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = login_request(self.row)
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.r_body = response_list[3]
            username = response_list[4]
            self.act_msg = self.json_response["result"]["message"]
            self.exp_msg = f"{Read_Expected_login_Response_msg().login_invalid_username()} '{username}'"
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def login_with_blank_username_and_blank_password(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = login_request(self.row)
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.r_body = response_list[3]
            self.act_msg = self.json_response["Data"]["exceptionMessage"]
            self.exp_msg = Read_Expected_login_Response_msg().login_blank_username_password()
            if invalid_response_validation(self.response) and self.act_msg == self.act_msg:
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_05_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_login(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_login_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_query_login_info(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_query_login_info_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["type"]
            self.exp_msg = Read_Expected_login_Response_msg().query_login_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_logout_request(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = logout_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.act_msg = self.json_response["data"]
            self.exp_msg = Read_Expected_login_Response_msg().logout_success_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Login_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

            ################################### Generic method #################################


def login_request(row_no):
    data = login_test_data(row_no)
    username = data[0]
    password = data[1]
    lat = data[2]
    lon = data[3]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_login_endpoint()}"
    form_data = {"username": username, "password": password, "lat": lat, "lon": lon}
    response_str = requests.post(url, form_data)
    response_json = response_str.json()
    return url, response_str, response_json, form_data, username


def get_login_request():
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_login_endpoint()}"
    print(url)
    response_str = requests.get(url)
    response_json = response_str.json()
    return response_str, response_json


def get_query_login_info_request():
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().query_login_info_endpoint()}"
    query_params = {"byPassSSO": "false"}
    response_str = requests.get(url, params=query_params)
    response_json = response_str.json()
    return query_params, response_str, response_json


def logout_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().logout_endpoint()}"
    response_str = requests.post(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


# Get all data form Excel
def login_test_data(row_no):
    username = XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                 API_Base_Utilities.login_test_data_sheet_name, row_no, 3)
    password = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                                 row_no, 4)
    lat = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                            row_no, 5)
    lon = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                            row_no, 6)
    return username, password, lat, lon


def response_validation(response_data):
    return int(response_data.status_code) == int(Read_API_Endpoints().get_success_response_code())


def invalid_response_validation(response_data):
    return int(response_data.status_code) == int(Read_API_Endpoints().internal_server_error())
