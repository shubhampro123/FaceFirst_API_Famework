import json

import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities
from All_API_Methods_Package.Identify_and_Enroll_Module_API.Identify_Enroll_Module_API import create_enrollment_request
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class Enrollment_Template_Data_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().enrollment_template_data_test_results_sheet_name()

    def verify_get_all_enrollment_template_data(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_enrollment_template_data_request()
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
            self.log.info(f"test_Enrollment_Template_Data_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_enrollment_template_data(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            case_id = create_enrollment_request()[3]
            response_list = create_enrollment_template_data_request(case_id)
            delete_enrollment_template_data_request(case_id)
            delete_enrollment_request(case_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
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
            self.log.info(f"test_Enrollment_Template_Data_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_enrollment_template_data(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            case_id = create_enrollment_request()[3]
            response_list = delete_enrollment_template_data_request(case_id)
            delete_enrollment_request(case_id)
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
            self.log.info(f"test_Enrollment_Template_Data_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_enrollment_template_data_count(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_enrollment_template_data_count_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
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
            self.log.info(f"test_Enrollment_Template_Data_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_enrollment_template_data_by_enrollment_id(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            case_id = create_enrollment_request()[3]
            response_list = get_enrollment_template_data_by_id_request(case_id)
            delete_enrollment_request(case_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
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
            self.log.info(f"test_Enrollment_Template_Data_Test_05_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_edit_enrollment_template_data(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            case_id = create_enrollment_request()[3]
            response_list = edit_enrollment_template_data_request(case_id)
            delete_enrollment_request(case_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            if response_validation(self.response):
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
            self.log.info(f"test_Enrollment_Template_Data_Test_06_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


def get_all_enrollment_template_data_request():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_enrollment_template_data_endpoint()}"
    query_param = {"pageNumber": 0, "batchSize": 10}
    response_str = requests.get(url, headers=headers, params=query_param)
    response_json = response_str.json()
    return response_str, response_json


def create_enrollment_template_data_request(case_id):
    token = login_token()
    test_data_row = 2
    data = create_enrollment_template_data(test_data_row)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_enrollment_template_data_endpoint()}"
    request_body = {"id": case_id, "algVersion": data[1], "stale": data[2]}
    request_data = json.dumps(request_body)
    headers = {"Token": token, "Content-Type": "application/json"}

    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def create_enrollment_template_data(row_no):
    data = []
    for x in range(3, 7):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().enrollment_template_data_test_data_sheet_name(), row_no, x))
    return data


def delete_enrollment_template_data_request(case_id):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().delete_enrollment_template_data_endpoint(case_id)}"
    headers = {"Token": token}
    response_str = requests.delete(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_enrollment_template_data_count_request():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_enrollment_template_data_count_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_enrollment_template_data_by_id_request(enrollment_id):
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_enrollment_template_data_by_id_endpoint(enrollment_id)}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def delete_enrollment_request(case_id):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_endpoint()}"
    headers = {"Token": token}
    params = {"caseId": case_id, "deleteAlerts": False}
    response_str = requests.delete(url, headers=headers, params=params)
    response_json = response_str.json()
    return response_str, response_json


def edit_enrollment_template_data_request(case_id):
    token = login_token()
    test_data_row = 2
    data = create_enrollment_template_data(test_data_row)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_enrollment_template_data_endpoint(case_id)}"
    request_body = {"id": case_id, "algVersion": data[1], "stale": data[2]}
    request_data = json.dumps(request_body)
    headers = {"Token": token, "Content-Type": "application/json"}

    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json