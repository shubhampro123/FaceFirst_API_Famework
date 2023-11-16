import json
from pathlib import Path

import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities, \
    invalid_response_validation
from All_API_Methods_Package.All_Module_Search_API.All_module_search_API_Methods import get_user_request
from All_API_Methods_Package.Notification_groups_Module_API.Notification_Groups_Methods import random_number
from All_API_Methods_Package.Zones_Module_API.Zones_API_Methods import get_single_zone_by_id
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_INI_Config_Files.Expected_Regions_Response_Msg_Read_ini import Read_Expected_Region_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Region_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().region_result_sheet_name()

    def verify_get_region_by_account_id(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_region_request_by_account_id()
            self.response = response_list[0]
            self.json_response = response_list[1]
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
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Region_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_region_by_id(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_request_by_region_id()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
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
            self.log.info(f"test_Region_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_region_by_region_path(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_region_by_region_path()
            self.response = response_list[0]
            self.json_response = response_list[1]
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
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Region_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_region_by_descendants(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_request_region_by_descendants()
            self.response = response_list[0]
            self.json_response = response_list[1]
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
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Region_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_regions_migrate_events(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_create_regions_migrate_events()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
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
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Region_Test_05_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_regions_by_cameras(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_regions_by_cameras()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
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
            excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Region_Test_06_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_update_region_by_id(self):
        result = []
        try:
            self.row = 8
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_request_update_region_by_id()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            region_id = response_list[3]
            self.exp_msg = Read_Expected_Region_Response_msg().update_success_msg(region_id)
            self.act_msg = self.json_response["message"]
            if response_validation(self.response) and self.exp_msg == self.act_msg:
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
            excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_group_Test_07:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_regions_import(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_regions_import()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response) or invalid_response_validation(self.response):
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
            self.log.info(f"test_notes_group_Test_08:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def varify_create_regions_by_id(self):
        result = []
        try:
            self.row = 10
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_request_regions()
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.r_body = response_list[2]
            region_id = response_list[3]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_Expected_Region_Response_msg().create_success_msg(region_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_group_Test_09:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def varify_create_regions_by_id_descendants(self):
        result = []
        try:
            self.row = 11
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_request_regions_by_descendants()
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.r_body = response_list[2]
            region_id = response_list[3]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_Expected_Region_Response_msg().create_success_msg(region_id)
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
            excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_group_Test_10:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def varify_create_regions_by_move(self):
        result = []
        try:
            self.row = 12
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_request_regions_by_move()
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.r_body = response_list[2]
            region_id = response_list[3]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_Expected_Region_Response_msg().update_success_msg(region_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
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
            excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_group_Test_11:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def varify_delete_regions(self):
        result = []
        try:
            self.row = 13
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = delete_region_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            region_id = response_list[2]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_Expected_Region_Response_msg().delete_success_msg(region_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
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
            excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_group_Test_12:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    ################################### Generic method #################################


def get_region_request_by_account_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    # region_id = select_region()
    account_id = get_user_request()
    params = {'accountid': account_id[3], 'edgeOnly': 'false'}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_id_endpoint()}"
    response_str = requests.get(url, params=params, headers=headers)
    response_json = response_str.json()
    get_id = response_json[0]["id"]
    return response_str, response_json, get_id


def get_request_by_region_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    region_id = get_region_request_by_account_id()
    params = {'includeCameras': 'false'}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_by_id_endpoint(region_id[2])}"
    response_str = requests.get(url, params=params, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def select_region():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    region = response_json["zoneInfo"]["zones"][0]["zoneId"]
    return region


def get_region_by_region_path():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    region_id = get_region_request_by_account_id()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_by_region_path(region_id[2])}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    # act_role_id = response_json["userRoleInfo"]["userRoles"][0]["id"]
    return response_str, response_json


def get_request_region_by_descendants():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    region_id = get_region_request_by_account_id()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_by_descendants(region_id[2])}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    get_id = response_json[0]["id"]
    account_id = response_json[0]["accountId"]
    get_code = response_json[0]["code"]
    get_name = response_json[0]["name"]
    get_time_zone = response_json[0]["timezone"]
    get_parent_id = response_json[0]["parentId"]
    # act_role_id = response_json["userRoleInfo"]["userRoles"][0]["id"]
    return response_str, response_json, get_id, account_id, get_code, get_name, get_time_zone, get_parent_id


def get_request_update_region_by_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_id = get_request_region_by_descendants()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_by_id_endpoint(request_id[2])}"
    request_body = {"code": request_id[4], "name": request_id[5], "unitType": 1, "timezone": request_id[6],
                    "accountId": request_id[3]}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    region_id = response_json["data"]
    return request_data, response_str, response_json, region_id


def get_regions_by_cameras():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    region_id = get_request_region_by_descendants()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_id_by_cameras(region_id[2])}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    # act_role_id = response_json["userRoleInfo"]["userRoles"][0]["id"]
    return response_str, response_json


def get_create_regions_migrate_events():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    zone_id = get_all_zones()
    print(zone_id)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_by_migrate_events(zone_id[0])}"
    response_str = requests.post(url, zone_id[0], headers=headers)
    response_json = response_str.json()
    print(response_json)
    # act_role_id = response_json["userRoleInfo"]["userRoles"][0]["id"]
    return response_str, response_json


def get_all_zones():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_zones_endpoint()}"
    query_params = {"offset": 0}
    response_str = requests.get(url, params=query_params, headers=headers)
    response_json = response_str.json()
    data = response_json["zoneInfo"]["zones"][3]["regionId"]
    account_id = response_json["zoneInfo"]["zones"][1]["accountId"]
    return data, account_id


def get_regions_import():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    file_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\Dmart.json"
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_import_file()}"
    form_data = {'File': ('json_file.json', json.dumps(json_data), 'application/json')}
    response_str = requests.post(url, files=form_data, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def create_request_regions():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_id_endpoint()}"
    data = region_module_test_module(2)
    code = f"{data[1]}{random_number()}"
    parent_id = get_request_region_by_descendants()
    request_body = {"parentId": parent_id[7], "code": code, "name": data[2], "unitType": data[3],
                    "timezone": data[4], "contact": {"firstName": data[5], "lastName": data[6],
                                                     "email": data[7], "phoneNumber": str(data[8]),
                                                     "faxNumber": str(data[9])},
                    "location": {"address1": data[10], "address2": data[11], "city": data[12],
                                 "state": data[13], "country": data[14], "postalCode": data[15],
                                 "geocode": [data[16]]}}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    region_id = response_json["data"]
    return response_str, response_json, request_body, region_id


def create_request_regions_by_descendants():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    response_ids = get_request_region_by_descendants()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_region_by_descendants(response_ids[2])}"

    data = region_module_test_module(2)
    code = f"{data[1]}{random_number()}"
    request_body = {"parentId": response_ids[7], "code": code, "name": data[2], "unitType": data[3],
                    "timezone": data[4], "contact": {"firstName": data[5], "lastName": data[6],
                                                     "email": data[7], "phoneNumber": str(data[8]),
                                                     "faxNumber": str(data[9])},
                    "location": {"address1": data[10], "address2": data[11], "city": data[12],
                                 "state": data[13], "country": data[14], "postalCode": data[15],
                                 "geocode": [data[16]]}}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    region_id = response_json["data"]
    return response_str, response_json, request_body, region_id


def create_request_regions_by_move():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    source_id = create_request_regions_by_descendants()[3]
    response = get_request_region_by_descendants()[1]
    target_name = "North level"
    DestinationId = None
    for element in response:
        if element.get("name") == target_name:
            DestinationId = element.get("id")
            break
    params = {'SourceId': source_id, 'DestinationId': DestinationId, 'ByCode': False}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_move_regions()}"
    response_str = requests.post(url, params=params, headers=headers)
    response_json = response_str.json()
    data_id = response_json["data"]
    return response_str, response_json, params, data_id


def delete_region_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    region_id = create_request_regions_by_descendants()[3]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().delete_region_endpoint(region_id)}"
    response_str = requests.delete(url, headers=headers)
    response_json = response_str.json()
    data_id = response_json["data"]
    return response_str, response_json, data_id


def region_module_test_module(row_no):
    data = []
    for x in range(3, 22):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().region_module_test_module(), row_no, x))
    return data
