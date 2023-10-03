import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints


class Account_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().account_result_sheet_name()

    def verify_get_all_account(self):
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
            self.log.info(f"test_Account_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_account_by_account_id(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            ex_account_id = get_all_account()[1][0]["accountId"]
            response_list = get_single_account_by_account_id(ex_account_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            ac_account_id = self.json_response["accountId"]
            print(response_list)
            if response_validation(self.response) and ex_account_id == ac_account_id:
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
            self.log.info(f"test_Account_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_account_stations_by_account_id(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            account_id = get_all_account()[1][0]["accountId"]
            print("account_id",account_id)
            response_list = get_account_stations_by_account_id(account_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(response_list)
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
            self.log.info(f"test_Account_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


def get_all_account():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_account_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_single_account_by_account_id(account_id):
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_account_by_account_id_endpoint(account_id)}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_account_stations_by_account_id(account_id):
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_account_stations_by_account_id_endpoint(account_id)}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json
