import json
import random

import requests
from API_Utilities.Api_Base import login_token, API_Base_Utilities, time_entry, response_validation, excel_result
from All_API_Methods_Package.User_Roles_Module_API.User_Role_Methods import random_number
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_INI_Config_Files.Expected_Enrollment_Group_Response_Msg_Read_ini import \
    Read_Expected_Enrollment_Group_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Enrollment_Group_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().enrollment_group_test_result_sheet_name()

    def verify_the_get_all_enrollment_group(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_enrollment_group_request()
            self.response = response_list[0]
            if response_validation(self.response):
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
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_01:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_the_enrollment_groups_is_created_with_valid_data(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_enrollment_group_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["message"]
            exp_id = response_list[3]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg().create_enrollment_group_msg(exp_id)
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
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_02:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_the_get_single_enrollment_group(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_enrollment_group_by_id()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            if response_validation(self.response):
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
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_03:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_the_update_enrollment_group(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = update_enrollment_group_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["message"]
            act_group_id = self.json_response["data"]
            exp_group_id = response_list[3]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg().update_enrollment_group_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg and act_group_id == exp_group_id:
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
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_04:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_remove_a_single_Enrollment_Group_from_collection(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = delete_enrollment_group()
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.act_msg = self.json_response["message"]
            exp_id = response_list[2]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg().delete_enrollment_group_msg(exp_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
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
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_05:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_enrollment_group_with_addCaseGroupZone(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_enrollment_group_with_addCaseGroupZone_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["result"]["message"]
            account_id = response_list[3]
            cGroupId = response_list[4]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg(). \
                create_enrollment_group_with_addCaseGroupZone_msg(cGroupId, account_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_06:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_removeCaseGroupZone(self):
        result = []
        try:
            self.row = 8
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = remove_enrollment_group_with_removeCaseGroupZone_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["result"]["message"]
            account_id = response_list[3]
            cGroupId = response_list[4]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg(). \
                removeCaseGroupZone_msg(cGroupId, account_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_06:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_addCaseGroupCase(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_enrollment_group_with_verify_addCaseGroupCase_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["result"]["message"]
            account_id = response_list[3]
            cGroupId = response_list[4]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg().addCaseGroupCase_msg(cGroupId, account_id)
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
            excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_08:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_removeCaseGroupCase(self):
        result = []
        try:
            self.row = 10
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = remove_enrollment_group_with_removeCaseGroupCase_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["result"]["message"]
            account_id = response_list[3]
            cGroupId = response_list[4]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg().removeCaseGroupCase_msg(cGroupId, account_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_09:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_addAlertGroupCase(self):
        result = []
        try:
            self.row = 11
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = remove_enrollment_group_with_addAlertGroupCase_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["result"]["message"]
            cGroupId = response_list[4]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg().addAlertGroupCase_msg(cGroupId)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_10:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_removeAlertGroupCase(self):
        result = []
        try:
            self.row = 12
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = remove_enrollment_group_with_removeAlertGroupCase_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["result"]["message"]
            cGroupId = response_list[4]
            self.exp_msg = Read_Expected_Enrollment_Group_Response_msg().removeAlertGroupCase_msg(cGroupId)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_11:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

        ################################### Generic method #################################


def get_all_enrollment_group_request():
    token = login_token()
    print(token)
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_enrollment_group_endpoint()}"
    print(url)
    response_str = requests.get(url, headers=headers, verify=False)
    print(response_str)
    response_json = response_str.json()
    print(response_json)
    return response_str, response_json


def create_enrollment_group_request(row_no):
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    data = create_enrollment_group_test_data(row_no)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_group_endpoint()}"
    name = f"{data[0]}{random_number()}"
    request_body = {"name": name, "description": data[1], "faceThreshold": data[2], "maskedFaceThreshold": data[3],
                    "eventsSuppressionInterval": data[4], "priority": data[5], "seriousOffender": data[6],
                    "alertHexColor": data[7], "activeThreat": data[8]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    data = response_json["data"]
    return request_body, response_str, response_json, data


def create_enrollment_group_with_addCaseGroupZone_request():
    token = login_token()
    data = create_enrollment_group_request(3)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_group_with_addCaseGroupZone_endpoint()}"
    cGroupId = data[3]
    zones_data = get_all_zones()
    zoneIds = zones_data[0]
    account_id = zones_data[1]
    request_body = {"cGroupId": cGroupId, "zoneIds": [zoneIds]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    return request_body, response_str, response_json, account_id, cGroupId


def create_enrollment_group_with_verify_addCaseGroupCase_request():
    token = login_token()
    data = create_enrollment_group_request(3)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().addCaseGroupCase_endpoint()}"
    cGroupId = data[3]
    zones_data = get_all_zones()
    account_id = zones_data[1]
    request_body = {"id": [account_id], "case_id": get_case_id(token), "cgroup_id": cGroupId}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json, account_id, cGroupId


def remove_enrollment_group_with_removeCaseGroupZone_request():
    token = login_token()
    data = create_enrollment_group_request(3)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().removeCaseGroupZone_endpoint()}"
    cGroupId = data[3]
    zones_data = get_all_zones()
    zoneIds = zones_data[0]
    account_id = zones_data[1]
    request_body = {"cGroupId": cGroupId, "zoneIds": [zoneIds]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json, account_id, cGroupId


def remove_enrollment_group_with_removeCaseGroupCase_request():
    token = login_token()
    data = create_enrollment_group_request(3)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().removeCaseGroupCase_endpoint()}"
    cGroupId = data[3]
    zones_data = get_all_zones()
    account_id = zones_data[1]
    request_body = {"id": [account_id], "case_id": get_case_id(token), "cgroup_id": cGroupId}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json, account_id, cGroupId


def remove_enrollment_group_with_addAlertGroupCase_request():
    token = login_token()
    data = create_enrollment_group_request(3)
    print(data[3])
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().addAlertGroupCase_endpoint()}"
    print(url)
    cGroupId = data[3]
    aGroupId = get_aGroup_id()
    request_body = {"CGroupID": cGroupId, "AGroupID": aGroupId}
    request_data = json.dumps(request_body)
    print(request_data)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    return request_body, response_str, response_json, aGroupId, cGroupId


def remove_enrollment_group_with_removeAlertGroupCase_request():
    token = login_token()
    data = remove_enrollment_group_with_addAlertGroupCase_request()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().removeAlertGroupCase_endpoint()}"
    cGroupId = data[4]
    aGroupId = data[3]
    request_body = {"CGroupID": cGroupId, "AGroupID": aGroupId}
    request_data = json.dumps(request_body)
    print(request_data)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    return request_body, response_str, response_json, aGroupId, cGroupId


def update_enrollment_group_request(row_no):
    token = login_token()
    res = create_enrollment_group_request(3)
    print(res[3])
    group_id = res[3]
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    data = update_enrollment_group_test_data(row_no)
    name = f"{data[0]}{random_number()}"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().update_enrollment_group_endpoint()}/{group_id}"
    print(url)
    # request_body = {"name": data[0], "description": data[1], "faceThreshold": data[2], "maskedFaceThreshold": data[3],
    #                 "eventsSuppressionInterval": data[4], "priority": data[5], "seriousOffender": data[6],
    #                 "alertHexColor": data[7], "activeThreat": data[8]}

    request_body = {"name":name,"description": data[1],"faceThreshold":data[2],
                    "maskedFaceThreshold":data[3],"eventsSuppressionInterval":data[4],"priority":data[5],
                    "seriousOffender":data[6],"alertHexColor":data[7],"activeThreat":data[8]}

    request_data = json.dumps(request_body)
    print(request_data)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    return request_body, response_str, response_json, group_id


def delete_enrollment_group():
    token = login_token()
    res = create_enrollment_group_request(3)
    group_id = res[3]
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().delete_enrollment_group_endpoint()}/{group_id}"
    response_str = requests.delete(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json, group_id


def get_enrollment_group_by_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    data = create_enrollment_group_request(3)
    form_data = {"id": data[3]}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_enrollment_group_endpoint()}"
    response_str = requests.get(url, params=form_data, headers=headers, verify=False)
    response_json = response_str.json()
    return form_data, response_str, response_json


def create_enrollment_group_test_data(row_no):
    data = []
    for x in range(3, 12):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().enrollment_group_test_data_sheet_name(), row_no, x))
    return data


def update_enrollment_group_test_data(row_no):
    data = []
    for x in range(3, 12):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().enrollment_group_test_data_sheet_name(), row_no, x))
    return data


def get_all_zones():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_zones_endpoint()}"
    query_params = {"offset": 0}
    response_str = requests.get(url, params=query_params, headers=headers, verify=False)
    response_json = response_str.json()
    data = response_json["zoneInfo"]["zones"][1]["zoneId"]
    account_id = response_json["zoneInfo"]["zones"][1]["accountId"]
    return data, account_id


def get_case_id(token):
    headers = {"Authorization": f"Token {token}", 'Content-Type': 'application/json'}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_enrollment_endpoint()}"
    request_body = {"DetailLevel": 3, "Offset": 0, "count": 20, "Ascending": 0, "IsExact": False}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, headers=headers, data=request_data, verify=False)
    response_json = response_str.json()
    case_Id = response_json["caseInfo"]["cases"][0]["caseId"]
    return case_Id


def get_aGroup_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_alert_groups_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    aGroupId = response_json["agroupinfo"]["agroups"][0]["agroupID"]
    return aGroupId
