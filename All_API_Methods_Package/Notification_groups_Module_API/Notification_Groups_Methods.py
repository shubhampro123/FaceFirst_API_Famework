import json
import random

import requests

from API_Utilities.Api_Base import time_entry, login_token, API_Base_Utilities, excel_result, \
    invalid_response_validation
from All_API_Methods_Package import Users_Module_API
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_INI_Config_Files.Expected_Notification_Groups_Response_Msg_read_ini import \
    Read_Expected_Notification_Groups_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Notification_Groups_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().notification_groups_result_sheet_name()

    def verify_create_notification_group_with_users_enrollment_group_zones(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_notification_group_with_users_enrollment_group_zones()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            alert_id = self.json_response["data"]
            self.act_msg = self.json_response["message"]
            print(response_list)
            self.exp_msg = Read_Expected_Notification_Groups_Response_msg().notification_created_success_msg(alert_id)
            if response_validation(self.response) and self.exp_msg == self.act_msg:
                excel_result(self.row,"Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
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
            self.log.info(f"test_Notification_Groups_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_notification_group_without_users_enrollment_group_and_zones(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_notification_group_without_users_enrollment_group_zones()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            alert_id = self.json_response["data"]
            self.act_msg = self.json_response["message"]
            print(response_list)
            self.exp_msg = Read_Expected_Notification_Groups_Response_msg().notification_created_success_msg(alert_id)
            if response_validation(self.response) and self.exp_msg == self.act_msg:
                excel_result(self.row,"Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
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
            self.log.info(f"test_Notification_Groups_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_all_alert_groups(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_notification_groups()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(response_list)
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
            self.log.info(f"test_Notification_Groups_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_single_alert_group_using_id(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            post_response_list = create_notification_group_without_users_enrollment_group_zones()
            alert_id = post_response_list[2]["data"]
            ex_alert_name = post_response_list[3]
            response_list = get_notification_group_using_id(alert_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            ac_alert_name = self.json_response["agroupinfo"]["agroups"][0]["name"]
            print(response_list)
            if response_validation(self.response) and ex_alert_name == ac_alert_name:
                excel_result(self.row,"Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_04", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Notification_Groups_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def modify_alert_group(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            post_response_list = create_notification_group_without_users_enrollment_group_zones()
            print(post_response_list)
            alert_id = post_response_list[2]["data"]
            alert_name = post_response_list[3]
            print(alert_id)
            print(alert_name)
            response_list = edit_alert_group_request(alert_id,alert_name)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            print("response_list",response_list)
            ex_update_msg = Read_Expected_Notification_Groups_Response_msg().notification_updated_success_msg(alert_id)
            ac_update_msg = response_list[2]["message"]
            if response_validation(self.response) and ex_update_msg == ac_update_msg:
                excel_result(self.row,"Test_05", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_05", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_05", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Notification_Groups_Test_05_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_add_user_to_alert_group(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            user_info_list = get_user_info()
            post_response_list = create_notification_group_without_users_enrollment_group_zones()
            print(post_response_list)
            alert_id = post_response_list[2]["data"]
            print(alert_id)
            response_list = add_user_to_alert_group_request(alert_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            print("response_list",response_list)
            ex_update_msg = Read_Expected_Notification_Groups_Response_msg().user_added_to_notification_success_msg(user_info_list[3], alert_id)
            ac_update_msg = response_list[2]["result"]["message"]
            self.exp_msg = Read_Expected_Notification_Groups_Response_msg().user_added_to_notification_status_success_msg()
            self.act_msg = response_list[2]["result"]["status"]

            if response_validation(self.response) and ex_update_msg == ac_update_msg and self.exp_msg == self.act_msg:
                excel_result(self.row,"Test_06", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_06", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_06", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Notification_Groups_Test_06_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_remove_user_from_alert_group(self):
        result = []
        try:
            self.row = 8
            time_entry(self.row, "start_time", self.sheet_name)
            user_info_list = get_user_info()
            post_response_list = create_notification_group_without_users_enrollment_group_zones()
            print(post_response_list)
            alert_id = post_response_list[2]["data"]
            print(alert_id)
            add_user_to_alert_group_request(alert_id)
            response_list = remove_user_from_alert_group_request(alert_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            print("response_list",response_list)
            ex_update_msg = Read_Expected_Notification_Groups_Response_msg().user_removed_from_notification_success_msg(user_info_list[3], alert_id)
            ac_update_msg = response_list[2]["result"]["message"]
            self.exp_msg = Read_Expected_Notification_Groups_Response_msg().user_removed_from_notification_status_success_msg()
            self.act_msg = response_list[2]["result"]["status"]

            if response_validation(self.response) and ex_update_msg == ac_update_msg and self.exp_msg == self.act_msg:
                excel_result(self.row,"Test_07", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_07", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_07", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Notification_Groups_Test_07_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_alert_group(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            post_response_list = create_notification_group_without_users_enrollment_group_zones()
            print(post_response_list)
            alert_id = post_response_list[2]["data"]
            print(alert_id)
            get_response_list = get_notification_group_using_id(alert_id)
            alert_name = get_response_list[1]["agroupinfo"]["agroups"][0]["name"]
            response_list = get_delete_user_request(alert_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            print("response_list",response_list)
            self.exp_msg = Read_Expected_Notification_Groups_Response_msg().notification_delete_msg(alert_name,alert_id)
            self.act_msg = self.json_response["message"]

            if response_validation(self.response) and self.exp_msg == self.act_msg:
                excel_result(self.row,"Test_08", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_08", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_08", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Notification_Groups_Test_08_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_notification_group_should_not_be_duplicate(self):
        result = []
        try:
            self.row = 10
            time_entry(self.row, "start_time", self.sheet_name)
            post_response_list = create_notification_group_without_users_enrollment_group_zones()
            print(post_response_list)
            alert_id = post_response_list[2]["data"]
            print(alert_id)
            alert_name = post_response_list[3]
            post_duplicate_response_list = create_duplicate_notification_group(alert_name)
            self.r_body = post_duplicate_response_list[0]
            self.response = post_duplicate_response_list[1]
            self.json_response = post_duplicate_response_list[2]
            print("response_list",post_duplicate_response_list)

            if invalid_response_validation(self.response):
                excel_result(self.row,"Test_09", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_09", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_09", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Notification_Groups_Test_08_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_add_enrollment_group_to_notification_group(self):
        result = []
        try:
            self.row = 11
            time_entry(self.row, "start_time", self.sheet_name)
            enrollment_id = get_enrollment_group_id()
            response_list = create_notification_group_without_users_enrollment_group_zones()
            alert_id = response_list[2]["data"]
            add_enrollment_resp_list = add_enrollment_to_alert_group_request(enrollment_id, alert_id)
            self.r_body = add_enrollment_resp_list[0]
            self.response = add_enrollment_resp_list[1]
            self.json_response = add_enrollment_resp_list[2]
            self.act_msg = self.json_response["result"]["status"]
            print(response_list)
            if response_validation(self.response):
                excel_result(self.row,"Test_10", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_10", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Notification_Groups_Test_10_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


def response_validation(response_data):
    return int(response_data.status_code) == int(Read_API_Endpoints().get_success_response_code())


def random_number():
    r_number = random.randint(1, 1000)
    return r_number


def create_notification_groups_with_users_enrollment_group_zone_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notification_groups_test_data_sheet_name, row_no, x))
    return data


def create_notification_groups_without_users_enrollment_group_zone_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notification_groups_test_data_sheet_name, row_no, x))
    return data


def get_user_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_users_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    user_id = response_json[1]["id"]
    accountId = response_json[0]["accountId"]
    return response_str, response_json, user_id, accountId


def create_notification_group_with_users_enrollment_group_zones():
    user_info_list = get_user_info()
    all_users_zone_id = get_all_device_zone_id()
    case_group_id = get_enrollment_group_id()
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_alert_groups_endpoint()}"
    data = create_notification_groups_with_users_enrollment_group_zone_test_data(2)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    username = f"{data[0]}{random_number()}"
    request_body = {"name": username, "description": data[1], "ownerID": user_info_list[0], "userIds": [user_info_list[3]],
                    "caseGroupIdsUserIds": [case_group_id],"zoneIds":[all_users_zone_id]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json, username


def create_notification_group_without_users_enrollment_group_zones():
    user_info_list = get_user_info()
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_alert_groups_endpoint()}"
    data = create_notification_groups_without_users_enrollment_group_zone_test_data(4)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    username = f"{data[2]}{random_number()}"
    request_body = {"agroupID": bool(data[0]), "description": data[1], "name": username, "ownerID": user_info_list[0],
                    "set_cgroups": data[4]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json, username


def create_duplicate_notification_group(alert_name):
    user_info_list = get_user_info()
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_alert_groups_endpoint()}"
    data = create_notification_groups_without_users_enrollment_group_zone_test_data(4)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"agroupID": bool(data[0]), "description": data[1], "name": alert_name, "ownerID": user_info_list[0],
                    "set_cgroups": data[4]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def get_all_notification_groups():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_alert_groups_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_notification_group_using_id(a_group_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_alert_group_using_ID(a_group_id)}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def edit_alert_group_request(alert_id, alert_name):
    user_info_list = get_user_info()
    test_data_row = 5
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_alert_group_ID(alert_id)}"
    print(url)
    data = edit_alert_group_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"agroupID": alert_id, "description": data[1], "name": alert_name, "ownerID":user_info_list[3],
                    "set_cgroups": data[4]}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def edit_alert_group_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notification_groups_test_data_sheet_name, row_no, x))
    return data


def add_user_to_alert_group_request(alert_id):
    user_info_list = get_user_info()
    test_data_row = 7
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_user_to_alert_group()}"
    print(url)
    data = add_user_to_alert_group_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"agroupID": alert_id, "userId": user_info_list[3]}
    request_data = json.dumps(request_body)
    print("request_data",request_data)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    print("response_json",response_json)
    return request_body, response_str, response_json


def add_user_to_alert_group_test_data(row_no):
    data = []
    for x in range(3, 5):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notification_groups_test_data_sheet_name, row_no, x))
    return data


def remove_user_from_alert_group_request(alert_id):
    user_info_list = get_user_info()
    test_data_row = 8
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_remove_user_from_alert_group()}"
    print(url)
    data = remove_user_from_alert_group_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"agroupID": alert_id, "userId": user_info_list[3]}
    request_data = json.dumps(request_body)
    print("request_data",request_data)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    print("response_json",response_json)
    return request_body, response_str, response_json


def remove_user_from_alert_group_test_data(row_no):
    data = []
    for x in range(3, 5):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notification_groups_test_data_sheet_name, row_no, x))
    return data


def get_user_info():
    """
    0. accountId
    1. regionId
    2. userName
    3. userId
    4. userRoleId
    :return:
    """
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_main_user_info()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_json["accountId"], response_json["regionId"], response_json["userName"], response_json["userId"], response_json["userRoleId"]


def get_all_device_zone_id():
    """
    0. zone id
    :return: zone id
    """
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_zone_id()}"
    print(url)
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_json["zoneInfo"]["zones"][0]["zoneId"]


def get_enrollment_group_id():
    """
    caseGroupIdsUserIds
    :return: caseGroupIdsUserIds
    """
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_case_group()}"
    data = create_case_groups_test_data(4)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    enrollment_name = f"{data[0]}{random_number()}"
    request_body = {"name": enrollment_name, "description": data[1], "faceThreshold": data[2], "maskedFaceThreshold": data[3],
                    "eventsSuppressionInterval": data[4], "priority": data[5], "seriousOffender": data[6], "alertHexColor": data[7], "activeThreat": data[8]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return response_json["data"]


def create_case_groups_test_data(row_no):
    data = ["test enrollment", "test description", 0.83, 0.83, "0", "Low", "Low", "#FFFFFF", False]
    return data


def get_delete_user_request(alert_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().delete_alert_group(alert_id)}"
    response_str = requests.delete(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def add_enrollment_to_alert_group_request(enrollment_group_id, alert_id):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_enrollment_group_to_alert_group()}"
    print(url)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"CGroupID": enrollment_group_id, "AGroupID": alert_id}
    request_data = json.dumps(request_body)
    print("request_data",request_data)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    print("response_json",response_json)
    return request_body, response_str, response_json