import json
import random

import requests

from API_Utilities.Api_Base import API_Base_Utilities, login_token, time_entry, excel_result, response_validation
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class Tags_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().tags_test_result_sheet_name()

    def verify_create_tags_with_valid_data(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_tags_request(self.row)

            self.response = response_list[0]
            self.json_response = response_list[1]

            if response_validation(self.response):
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Tags_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_all_get_tag_data(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_tags()
            print(response_list)
            self.response = response_list[0]
            self.json_response = response_list[1]

            if response_validation(self.response):
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Role_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_update_tag_with_valid_data(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = update_tags_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]

            if response_validation(self.response):
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
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
            self.log.info(f"test_Tags_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_tags_with_valid_tag_id(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = del_tags_by_id_request()
            print(response_list)
            self.response = response_list[0]
            print(self.response)
            self.json_response = response_list[1]
            # self.act_msg = response_list[2]
            # self.exp_msg = response_list[3]
            if response_validation(self.response):
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
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

    def verify_create_tag_with_tag_alert(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_tags_request(self.row)

            self.response = response_list[0]
            self.json_response = response_list[1]

            if response_validation(self.response):
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "Test_05", "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Tags_Test_05_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


################################### Generic method #################################

def create_tags_request(row_no):
    token = login_token()
    print(token)
    data = tags_test_data(row_no)
    tag_name = f"{data[0]}{random_number()}"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_tags_endpoint(tag_name, data[1], data[2])}"

    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    # request_data = {"name": tag_name, "seriousEvent": data[1], "type": data[2]}
    # request_data = json.dumps(request_data)
    response_str = requests.post(url, headers=headers, verify=False)
    # print(request_data)
    response_json = response_str.json()
    print(response_json)
    # role_id = response_json["id"]
    return response_str, response_json, tag_name


def update_tags_request():
    tag_name = create_tags_request(2)[2]
    token = login_token()
    tag_name_and_id = [tag_name]
    get_all_resp = get_all_tags()[1]
    for x in range(len(get_all_resp["tags"])):
        t_name = get_all_resp["tags"][x]["tagName"]
        if t_name.lower() == tag_name.lower():
            tag_name_and_id.append(get_all_resp["tags"][x]["id"])
            break
    data = update_tags_test_data(5)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().update_tags_endpoint()}"
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"id": tag_name_and_id[1], "seriousEvent": data[1], "newName": data[2], "type": data[3]}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json, data


def get_all_tags():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    print(headers)
    # data = create_tags_request(2)
    # role_id_exp = data[4]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_tags_endpoint()}"
    print(url)
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    tags = response_json
    # tags_id_list = []
    # for x in range(len(tags)):
    #     tags_id_list = [response_json[""]["tags"][x]["id"]]
    return response_str, response_json, tags


def get_tags_by_id():
    create_tags_request(2)
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_tags_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    tags = response_json.get("tags", [])
    # tag_ids = [tag.get("id") for tag in tags]
    # print(tag_ids)
    tag_id = response_json["tags"][2]["id"]
    return response_str, response_json, tag_id


def get_tags_by_id_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    role_id = create_tags_request(2)[4]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_user_role_by_id_endpoint(role_id)}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    # act_role_id = response_json["userRoleInfo"]["userRoles"][0]["id"]
    return response_str, response_json, role_id


def del_tags_by_id_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    response_list = get_tags_by_id()
    role_id = response_list[2]
    print(role_id)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().del_tags_by_id_endpoint(role_id)}"
    response_str = requests.delete(url, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    return response_str, response_json, role_id


def tags_test_data(row_no):
    data = []
    for x in range(3, 6):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities
                                      .tags_test_data_sheet_name, row_no, x))
    return data


def update_tags_test_data(row_no):
    data = []
    for x in range(3, 7):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities
                                      .tags_test_data_sheet_name, row_no, x))
    return data


def random_number():
    r_number = random.randint(1, 1000)
    return r_number
