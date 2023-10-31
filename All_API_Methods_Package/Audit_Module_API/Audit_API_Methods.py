import json

import requests

from API_Utilities.Api_Base import time_entry, login_token, API_Base_Utilities, excel_result, response_validation
from All_API_Methods_Package.Users_Module_API.Users_API_Methods import get_user_request
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class Audit_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().alr_result_sheet_name()

    def verify_audit_approvers(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_account()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(response_list)
            for x in range(len(self.json_response)):
                result.append(self.json_response[x]["accountId"] != "")

            if response_validation(self.response) and False not in result:
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
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
            print(ex)
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Account_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_audit_users(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_account_user()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(response_list)
            for x in range(len(self.json_response)):
                result.append(self.json_response[x]["accountId"] != "")

            if response_validation(self.response) and False not in result:
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Account_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_audit_login(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_account_login()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(response_list)
            for x in range(len(self.json_response)):
                result.append(self.json_response[x]["accountId"] != "")

            if response_validation(self.response) and False not in result:
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Account_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_audit_logins(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_login_users()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response) and False not in result:
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Account_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_audit_threshold_changes(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = verify_audit_threshold_changes()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(response_list)
            for x in range(len(self.json_response)):
                result.append(self.json_response[x]["accountId"] != "")

            if response_validation(self.response) and False not in result:
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Account_Test_05_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


######################################Reusable methods#########################################################
def get_all_account():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_audit_approvers_endpoint()}"
    print(url)
    userid_data = get_user_request()
    userIds = userid_data[2]
    data = get_all_account_test_data(2)
    request_body = {
        "userIds": [userIds], "startDate": data[1], "endDate": data[2]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, request_data, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_all_account_user():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_audit_users_endpoint()}"
    print(url)
    userid_data = get_user_request()
    userIds = userid_data[2]
    print(userIds)
    data = get_all_account_test_data(3)
    request_body = {
        "userIds": [userIds], "startDate": data[1], "endDate": data[2]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, request_data, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_all_account_login():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_audit_login_endpoint()}"
    print(url)
    userid_data = get_user_request()
    userIds = userid_data[2]
    data = get_all_account_test_data(4)
    request_body = {
        "userIds": [userIds], "startDate": data[1], "endDate": data[2]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, request_data, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_all_login_users():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_request_audit_logins()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def verify_audit_threshold_changes():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_request_audit_threshold_changes()}"
    data = get_all_account_test_data(5)
    request_body = {"endDate": data[2], "startDate": data[1], "userIds": [None]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, request_data, headers=headers)
    response_json = response_str.json()
    print(response_json)
    return response_str, response_json


def get_all_account_test_data(row_no):
    data = []
    for x in range(3, 6):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().alr_test_data_sheet_name(), row_no, x))
    return data
