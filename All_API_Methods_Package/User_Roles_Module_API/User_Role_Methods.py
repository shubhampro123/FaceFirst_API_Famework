import json
import random

import requests

from API_Utilities.Api_Base import API_Base_Utilities, login_token, time_entry, excel_result, response_validation
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class User_Role_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().user_role_result_sheet_name()

    def verify_create_user_role_with_valid_data_in_enable_mode(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_user_role_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["roleName"]
            self.exp_msg = response_list[3]
            if response_validation(self.response) and self.act_msg == self.exp_msg:
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Role_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_single_user_role_by_id(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_user_role_by_id_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.act_msg = response_list[2]
            self.exp_msg = response_list[3]
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Role_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_update_user_role_with_valid_data(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = update_user_role_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            print(self.response)
            self.json_response = response_list[2]
            self.act_msg = self.json_response["roleName"]
            self.exp_msg = response_list[3]
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Role_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_user_role_with_valid_user_role_id(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = del_user_role_by_id_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            # self.act_msg = response_list[2]
            # self.exp_msg = response_list[3]
            if response_validation(self.response):
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Role_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_all_get_user_roles(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_user_role()
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.act_msg = response_list[2]
            self.exp_msg = response_list[3]
            if response_validation(self.response) and self.act_msg in self.exp_msg:
                excel_result(self.row,"Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_05", self.r_body, self.json_response, self.response.status_code,
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
            self.log.info(f"test_Users_Role_Test_05_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_the_user_role_is_created_with_valid_data_in_disable_mode(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_user_role_request(self.row)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["roleName"]
            self.exp_msg = response_list[3]
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Role_Test_06_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


################################### Generic method #################################

def create_user_role_request(row_no):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().user_role_endpoint()}"
    data = user_role_test_data(row_no)
    role_name = f"{data[0]}{random_number()}"
    headers = {"Token": token, "Content-Type": "application/json"}
    request_data = {"rolename": role_name, "enabled": data[1], "description": data[2],
                    "permissions": {"user": data[3], "alert": data[4], "alertGroup": data[5], "station": data[6],
                                    "blob": data[7],
                                    "case": data[8], "caseGroup": data[9], "subscription": data[10],
                                    "investigation": data[11],
                                    "publication": data[12], "userRole": data[13], "visionAware": data[14],
                                    "notifier": data[15],
                                    "analytics": data[16], "enrollmentReview": data[17], "auditLog": data[18],
                                    "account": data[19],
                                    "devices": data[20], "zone": data[21], "notes": data[22], "alien": data[23],
                                    "profile": data[24],
                                    "tag": data[25], "face": data[26]}}
    request_data = json.dumps(request_data)
    response_str = requests.post(url, data=request_data, headers=headers)
    print(response_str)
    response_json = response_str.json()
    # print(response_json)
    role_id = response_json["id"]
    return request_data, response_str, response_json, role_name, role_id


def update_user_role_request(row_no):
    post_user_role = create_user_role_request(4)
    user_role_id = post_user_role[2]["id"]
    user_role_name = post_user_role[2]["roleName"]
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().update_user_role_endpoint()}"
    data = user_role_test_data(row_no)
    role_name = data[0]
    print(role_name)
    headers = {"Token": token, "Content-Type": "application/json"}
    request_data = {"rolename": role_name, "enabled": data[1], "description": data[2],
                    "permissions": {"user": data[3], "alert": data[4], "alertGroup": data[5], "station": data[6],
                                    "blob": data[7],
                                    "case": data[8], "caseGroup": data[9], "subscription": data[10],
                                    "investigation": data[11],
                                    "publication": data[12], "userRole": data[13], "visionAware": data[14],
                                    "notifier": data[15],
                                    "analytics": data[16], "enrollmentReview": data[17], "auditLog": data[18],
                                    "account": data[19],
                                    "devices": data[20], "zone": data[21], "notes": data[22], "alien": data[23],
                                    "profile": data[24],
                                    "tag": data[25], "face": data[26]}}
    request_data = json.dumps(request_data)
    print(request_data)
    response_str = requests.put(url, data=request_data, headers=headers)
    # print(request_data)
    response_json = response_str.json()
    return request_data, response_str, response_json, role_name


def create_user_role_request_disable(row_no):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().user_role_endpoint()}"
    data = user_role_test_data(row_no)
    role_name = f"{data[0]}{random_number()}"
    headers = {"Token": token, "Content-Type": "application/json"}
    request_data = {"rolename": role_name, "enabled": data[1], "description": data[2],
                    "permissions": {"user": data[3], "alert": data[4], "alertGroup": data[5], "station": data[6],
                                    "blob": data[7],
                                    "case": data[8], "caseGroup": data[9], "subscription": data[10],
                                    "investigation": data[11],
                                    "publication": data[12], "userRole": data[13], "visionAware": data[14],
                                    "notifier": data[15],
                                    "analytics": data[16], "enrollmentReview": data[17], "auditLog": data[18],
                                    "account": data[19],
                                    "devices": data[20], "zone": data[21], "notes": data[22], "alien": data[23],
                                    "profile": data[24],
                                    "tag": data[25], "face": data[26]}}
    request_data = json.dumps(request_data)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    print(response_json)
    role_id = response_json["id"]
    return request_data, response_str, response_json, role_name, role_id


def get_single_user_role():
    token = login_token()
    headers = {"Token": token}
    data = create_user_role_request(2)
    role_id_exp = data[4]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_user_role_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    user_roles = response_json["userRoleInfo"]["userRoles"]
    roles_id_list = []
    for x in range(len(user_roles)):
        roles_id_list = [response_json["userRoleInfo"]["userRoles"][x]["id"]]
    return response_str, response_json, role_id_exp, roles_id_list


def get_all_user_role():
    token = login_token()
    headers = {"Token": token}
    data = create_user_role_request(2)
    role_id_exp = data[4]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_user_role_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    user_roles = response_json["userRoleInfo"]["userRoles"]
    roles_id_list = []
    for x in range(len(user_roles)):
        roles_id_list = [response_json["userRoleInfo"]["userRoles"][x]["id"]]
    return response_str, response_json, role_id_exp, roles_id_list


def get_user_role_by_id_request():
    token = login_token()
    headers = {"Token": token}
    role_id = create_user_role_request(2)[4]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_user_role_by_id_endpoint(role_id)}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    act_role_id = response_json["userRoleInfo"]["userRoles"][0]["id"]
    return response_str, response_json, role_id, act_role_id


def del_user_role_by_id_request():
    token = login_token()
    headers = {"Token": token}
    role_id = create_user_role_request(2)[4]
    print(role_id)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().del_user_role_by_id_endpoint(role_id)}"
    response_str = requests.delete(url, headers=headers)
    response_json = response_str.json()
    print(response_json)
    # act_role_id = response_json["userRoleInfo"]["userRoles"][0]["id"]
    return response_str, response_json, role_id


def user_role_test_data(row_no):
    data = []
    for x in range(3, 30):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().user_role_test_data_sheet_name(), row_no, x))
    return data


def random_number():
    r_number = random.randint(1, 100)
    return r_number
