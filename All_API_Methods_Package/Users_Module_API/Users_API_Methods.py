import json
import random
import requests

from API_Utilities.Api_Base import API_Base_Utilities, login_token, time_entry, excel_result, response_validation
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_INI_Config_Files.Expected_Users_Response_Msg_read_ini import Read_Expected_users_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Users_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().users_test_result_sheet_name()

    def verify_create_user_with_valid_information_in_enabled_mode(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = user_create_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["status"]
            self.exp_msg = Read_Expected_users_Response_msg().users_success_msg()
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
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_user_with_mandatory_information_in_enabled_mode(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = user_create_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["status"]
            self.exp_msg = Read_Expected_users_Response_msg().users_success_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
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
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_user_with_valid_information_in_disabled_mode(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = user_create_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["status"]
            self.exp_msg = Read_Expected_users_Response_msg().users_success_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
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
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_user_with_mandatory_fields_in_disable_mode(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = user_create_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["status"]
            self.exp_msg = Read_Expected_users_Response_msg().users_success_msg()
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
            self.log.info(f"test_Users_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_edit_user_with_mandatory_information(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = edite_user_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["message"]
            self.exp_msg = f"User  {self.json_response['data']} is updated."
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_08_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_edit_user_password(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = edit_user_password()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_Expected_users_Response_msg().edit_password_success_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_08_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_users_api(self):
        result = []
        try:
            self.row = 12
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_user_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_11_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_user_by_account_id(self):
        result = []
        try:
            self.row = 13
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_user_request_by_account_id()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_12_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_user_by_id(self):
        result = []
        try:
            self.row = 14
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_user_by_id_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_13", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_13", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_13", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_13_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_users_update_alert_schedule(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = users_update_alert_schedule_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["data"]
            self.exp_msg = Read_Expected_users_Response_msg().user_update_alert_schedule_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_06_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_users_using_json(self):
        result = []
        try:
            self.row = 8
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_users_using_json()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["status"]
            self.exp_msg = Read_Expected_users_Response_msg().user_create_msg()
            act_username = self.json_response["userName"]
            exp_username = response_list[3]
            if response_validation(self.response) and self.act_msg == self.exp_msg and act_username == exp_username:
                excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_07_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_edite_user_with_json_data(self):
        result = []
        try:
            self.row = 11
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = edite_user_json_data_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            user_id = response_list[3]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_Expected_users_Response_msg().edit_user_success_msg(user_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_10_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_user_info(self):
        result = []
        try:
            self.row = 15
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_user_info_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_14", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_14", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_14", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_14_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_service_user_true(self):
        result = []
        try:
            self.row = 16
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_service_user_true_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response) and validate_response_is_service_user(self.json_response):
                excel_result(self.row, "Test_15", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_15", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_15", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_15_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_service_user_false(self):
        result = []
        try:
            self.row = 17
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_service_user_false_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response) and validate_response_is_not_service_user(self.json_response):
                excel_result(self.row, "Test_16", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_16", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_16", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_16_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_users_alert_schedule(self):
        result = []
        try:
            self.row = 18
            time_entry(self.row, "start_time", self.sheet_name)
            data = get_user_id_or_account_id()
            user_id = data[0]
            response_list = get_users_alert_schedule_request(user_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response) and validate_alert_schedule(self.json_response, user_id):
                excel_result(self.row, "Test_17", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_17", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_17", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_17_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_user_from_system(self):
        result = []
        try:
            self.row = 19
            time_entry(self.row, "start_time", self.sheet_name)
            data = user_create_request(2)
            user_id = data[3]
            ex_msg = Read_Expected_users_Response_msg().delete_user_success_msg(user_id)
            response_list = get_delete_user_from_system_request(user_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            ac_msg = self.json_response["message"]
            if response_validation(self.response) and ex_msg == ac_msg:
                excel_result(self.row, "Test_18", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_18", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_18", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_18_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_user(self):
        result = []
        try:
            self.row = 20
            time_entry(self.row, "start_time", self.sheet_name)
            data = user_create_request(2)
            user_id = data[3]
            ex_msg = Read_Expected_users_Response_msg().delete_user_success_msg(user_id)
            response_list = get_delete_user_request(user_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            ac_msg = self.json_response["message"]
            if response_validation(self.response) and ex_msg == ac_msg:
                excel_result(self.row, "Test_19", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_19", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_19", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_14_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    ################################### Generic method #################################


def user_create_request(row_no):
    token = login_token()
    print("token",token)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().users_endpoint()}"
    data = users_test_data(row_no)
    print(data)
    headers = {"Authorization": f"Token {token}"}
    form_data = {"auth_params": data[0], "company": data[1], "title": data[2], "department": data[3],
                 "enabled": data[4], "fname": data[5], "mname": data[6], "lname": data[7],
                 "addr1": data[8], "addr2": data[9], "city": data[10], "state": data[11],
                 "zip": data[12], "email": data[13], "aemail": data[14], "hphone": data[15],
                 "wphone": data[16], "fphone": data[17], "aphone": data[18], "phone_type": data[19],
                 "provider": data[20], "timezone": data[21], "urole_id": select_user_role(),
                 "region_id": select_region(), "username": f"{data[24]}{random_number()}", "password": data[25]}
    print(form_data)
    response_str = requests.post(url, form_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    user_id = response_json["userId"]
    account_id = response_json["accountId"]
    username = response_json["userName"]
    current_password = data[25]
    return form_data, response_str, response_json, user_id, account_id, username, current_password


def edite_user_request():
    data = user_create_request(2)
    user_id = data[3]
    account_id = [4]
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().edit_user_endpoint()}"
    data = edite_user_test_data(11)
    headers = {"Authorization": f"Token {token}"}
    form_data = {"auth_params": data[0], "company": data[1], "title": data[2], "department": data[3],
                 "enabled": data[4], "fname": data[5], "mname": data[6], "lname": data[7],
                 "addr1": data[8], "addr2": data[9], "city": data[10], "state": data[11],
                 "zip": data[12], "email": data[13], "aemail": data[14], "hphone": data[15],
                 "wphone": data[16], "fphone": data[17], "aphone": data[18], "phone_type": data[19],
                 "provider": data[20], "timezone": data[21], "urole_id": select_user_role(),
                 "region_id": select_region(), "user_id": user_id, "pw_current": data[25], "pw_new1": data[26],
                 "pw_new2": data[27]}
    response_str = requests.put(url, form_data, headers=headers, verify=False)
    response_json = response_str.json()
    return form_data, response_str, response_json


def edite_user_json_data_request():
    data = user_create_request(2)
    user_id = data[3]
    id_data = get_user_request()
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().edit_user_endpoint()}"
    data = edite_user_json_test_data(15)
    headers = {"Authorization": f"Token {token}"}
    form_data = {"Addr1": data[0], "Addr2": data[1], "Zip": data[2], "Enabled": data[3],
                 "Pw_current": data[4], "Region_id": select_region(), "Hphone": data[6], "AccountId": id_data[3],
                 "Fphone": data[8], "Pw_new1": data[9], "Pw_new2": data[10], "City": data[11],
                 "Phone_type": data[12], "Aphone": data[13], "Url": data[14], "User_id": user_id,
                 "Urole_id": select_user_role(), "State": data[17], "Provider": data[18], "Fname": data[19],
                 "Department": data[20], "IsServiceUser": data[21], "UserName": data[22],
                 "Lname": data[23], "Wphone": data[24], "Mname": data[25], "Title": data[26],
                 "Timezone": data[27], "Password": data[28], "Aemail": data[29], "Email": data[30],
                 "Company": data[31], "Auth_params": data[31]}
    response_str = requests.put(url, form_data, headers=headers, verify=False)
    response_json = response_str.json()
    return form_data, response_str, response_json, user_id


def users_update_alert_schedule_request():
    token = login_token()
    data_id = get_user_request()
    user_id = data_id[2]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().users_update_alert_schedule_endpoint()}"
    data = alert_schedule_test_data(7)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"userId": user_id, "alertEnabled": data[1], "sendSms": data[2],
                    "sendMms": data[3], "sendEmail": data[4], "sendInappNotification": data[5],
                    "scheduleDetail": [{"enabled": data[6], "startTime": data[7], "endTime": data[8]},
                                       {"enabled": data[9], "startTime": data[10], "endTime": data[11]},
                                       {"enabled": data[12], "startTime": data[13], "endTime": data[14]},
                                       {"enabled": data[15], "startTime": data[16], "endTime": data[17]},
                                       {"enabled": data[18], "startTime": data[19], "endTime": data[20]},
                                       {"enabled": data[21]}, {"enabled": data[22]}]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json


def get_user_request_by_account_id():
    data = get_user_request()
    accountID = data[3]
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_users_by_account_id_endpoint()}"
    params = {"AccountId": accountID}
    response_str = requests.get(url, headers=headers, params=params, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def get_user_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_users_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    user_id = response_json[1]["id"]
    accountId = response_json[0]["accountId"]
    return response_str, response_json, user_id, accountId


def get_user_by_id_request():
    data = get_user_request()
    user_id = data[2]
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_users_by_id_endpoint()}"
    params = {"id": user_id}
    response_str = requests.get(url, headers=headers, params=params, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def create_users_using_json():
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_users_endpoint()}"
    data = create_user_test_data(9)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    id_data = get_user_request()
    username = f"{data[30]}{random_number()}"
    request_body = {"accountId": id_data[3], "addr1": data[1], "addr2": data[2], "aemail": data[3],
                    "aphone": data[4], "auth_params": data[5], "city": data[6], "company": data[7],
                    "department": data[8], "email": data[9], "enabled": data[10], "fname": data[11],
                    "fphone": data[12], "hphone": data[13], "isServiceUser": data[14], "lname": data[15],
                    "mname": data[16], "password": data[17], "phone_type": data[18], "provider": data[19],
                    "pw_current": data[20], "pw_new1": data[21], "pw_new2": data[22],
                    "region_id": select_region(), "state": data[24], "timezone": data[25],
                    "title": data[26], "url": data[27], "urole_id": select_user_role(),
                    "user_id": id_data[2], "userName": username, "wphone": data[31],
                    "zip": data[32]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json, username


def edit_user_password():
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_user_password_endpoint()}"
    r_data = user_create_request(2)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    user_id = r_data[3]
    username = r_data[5]
    current_password = r_data[6]
    data = update_password_test_data(13)
    request_body = {"userName": username, "userId": user_id, "currentPassword": current_password,
                    "newPassword": data[3], "isServiceUserRequest": data[4], "isPasswordExpired": True}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json


def users_test_data(row_no):
    data = []
    for x in range(3, 29):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.users_test_data_sheet_name, row_no, x))
    return data


def create_user_test_data(row_no):
    data = []
    for x in range(3, 36):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.users_test_data_sheet_name, row_no, x))
    return data


def alert_schedule_test_data(row_no):
    data = []
    for x in range(3, 26):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.users_test_data_sheet_name, row_no, x))
    return data


def edite_user_test_data(row_no):
    data = []
    for x in range(3, 31):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.users_test_data_sheet_name, row_no, x))
    return data


def edite_user_json_test_data(row_no):
    data = []
    for x in range(3, 36):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.users_test_data_sheet_name, row_no, x))
    return data


def update_password_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.users_test_data_sheet_name, row_no, x))
    return data


def random_number():
    r_number = random.randint(1, 10000)
    return r_number


def select_user_role():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().user_role_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    user_role = response_json["userRoleInfo"]["userRoles"][0]["userRoleId"]
    return user_role


def select_region():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    region = response_json["zoneInfo"]["zones"][0]["zoneId"]
    return region


def get_user_info_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_user_info_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def get_service_user_true_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_service_user_true_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def validate_response_is_service_user(json_response):
    result = []
    for i in range(len(json_response)):
        result.append(json_response[i]["serviceUser"] == True)
    return False not in result


def get_service_user_false_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_service_user_false_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def validate_response_is_not_service_user(json_response):
    result = []
    for i in range(len(json_response)):
        result.append(json_response[i]["serviceUser"] == False)
    return False not in result


def get_user_id_or_account_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_users_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    user_id = response_json[0]["id"]
    account_id = response_json[0]["accountId"]
    return user_id, account_id


def get_users_alert_schedule_request(user_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_alert_schedule_endpoint(user_id)}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def validate_alert_schedule(json_response, user_id):
    return json_response["userID"] == user_id


def get_delete_user_from_system_request(user_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_delete_user_from_system_endpoint(user_id)}"
    response_str = requests.delete(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def get_delete_user_request(user_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_delete_user_endpoint(user_id)}"
    response_str = requests.delete(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json
