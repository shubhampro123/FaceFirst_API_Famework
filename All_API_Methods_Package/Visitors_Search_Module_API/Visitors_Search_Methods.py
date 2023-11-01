import json
import random
from pathlib import Path

import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class Visitors_Search_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().visitor_search_test_result_sheet_name()

    def verify_post_start_search(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = start_search_request()

            self.response = response_list[0]
            self.json_response = response_list[1]

            if response_validation(self.response):
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
            print(ex)
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_01:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_fed_search_status(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            job_id = start_search_request()[3]
            response_list = fed_search_status_request(job_id)
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
            print(ex)
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_02:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_visitor_image_by_image_id(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            job_id = start_search_request()[3]
            image_id = fed_search_status_request(job_id)[1]["matched"][0]["id"]
            response_list = get_visitor_image_by_image_id(image_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_03:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_identify_alien_federated(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = identify_alien_federated_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_04:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_identify_delete_federated(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            job_id = start_search_request()[3]
            response_list = delete_alien_federated_request(job_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_05:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_alien_image(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            job_id = start_search_request()[3]
            image_id = fed_search_status_request(job_id)[1]["matched"][0]["id"]
            response_list = get_alien_image_by_image_id(image_id)
            self.response = response_list
            if response_validation(self.response):
                excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_06:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_identify_alien_federated_status(self):
        result = []
        try:
            self.row = 8
            time_entry(self.row, "start_time", self.sheet_name)
            job_id = start_search_request()[3]
            response_list = get_identify_alien_federated_status(job_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_07", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_07:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_query_alien_face_info(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            job_id = start_search_request()[3]
            image_id = fed_search_status_request(job_id)[1]["matched"][0]["id"]
            response_list = get_query_alien_face_info(image_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
                excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_08", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_08:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_identify_cancel_federated(self):
        result = []
        try:
            self.row = 10
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = identify_cancel_federated_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(self.json_response)
            if response_validation(self.response):
                excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_09", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_09:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_query_alien_federated_identification_log(self):
        result = []
        try:
            self.row = 11
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_query_alien_federated_identification_log()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(self.json_response)
            if response_validation(self.response):
                excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_10", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_10:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_visitor_search(self):
        result = []
        try:
            self.row = 12
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = visitor_search_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            print(self.json_response)
            if response_validation(self.response):
                excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_11:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_visitor_count_by_zone(self):
        result = []
        try:
            self.row = 13
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_verify_visitor_count_by_zone()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(self.json_response)
            if response_validation(self.response):
                excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time",
                                                                              self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code,
                         self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_visitor_search_Test_12:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


def start_search_request():
    test_data_row = 2
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\Visitor.png"
    data = start_search_test_data(test_data_row)
    start_search = f"{data[0]}"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().start_search_endpoint()}"
    headers = {"Authorization": f"Token {token}"}
    request_data = {"regionId": get_region_id()}
    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    response_str = requests.post(url, headers=headers, data=request_data, files=files)
    response_json = response_str.json()
    print(response_json)
    job_id = response_json["jobId"]
    print(job_id)
    # role_id = response_json["id"]
    return response_str, response_json, start_search, job_id


def fed_search_status_request(job_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().fed_search_status_endpoint(job_id)}"
    print(url)
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    print(response_str)
    print(response_json)
    return response_str, response_json


def get_visitor_image_by_image_id(image_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_visitors_image_by_image_id_endpoint(image_id)}"
    print(url)
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    print(response_str)
    return response_str, response_json


def start_search_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().visitor_search_test_data_sheet_name(), row_no, x))
    return data


def random_number():
    r_number = random.randint(1, 100)
    return r_number


def get_region_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_zones_endpoint()}"
    response_str = requests.get(url, headers=headers)
    return response_str.json()["zoneInfo"]["zones"][1]["regionId"]


def identify_alien_federated_request():
    test_data_row = 4
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\Visitor.png"
    data = identify_alien_federated_test_data(test_data_row)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_identify_alien_federated()}"
    headers = {"Authorization": f"Token {token}"}
    request_data = {"EndAge": data[0], "MaxMatches": data[1], "StartAge": data[2], "IncludeMatrics": data[3]}
    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    response_str = requests.post(url, headers=headers, data=request_data, files=files)
    response_json = response_str.json()
    print(url)
    print(response_str)
    print(response_json)
    return response_str, response_json


def identify_alien_federated_test_data(row_no):
    data = []
    for x in range(3, 7):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().visitor_search_test_data_sheet_name(), row_no, x))
    return data


def delete_alien_federated_request(job_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().delete_alien_federated_endpoint(job_id)}"
    print(url)
    response_str = requests.delete(url, headers=headers)
    response_json = response_str.json()
    print(response_str)
    return response_str, response_json


def get_alien_image_by_image_id(image_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_alien_image_endpoint(image_id)}"
    print(url)
    response_str = requests.get(url, headers=headers)
    print(response_str)
    return response_str


def get_identify_alien_federated_status(job_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_identify_alien_federated_status_endpoint(job_id)}"
    print(url)
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    print(response_str)
    return response_str, response_json


def get_query_alien_face_info(image_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_query_alien_face_info_endpoint(image_id)}"
    print(url)
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    print(response_str)
    return response_str, response_json


def identify_cancel_federated_request():
    test_data_row = 2
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\img2.png"
    data = start_search_test_data(test_data_row)
    start_search = f"{data[0]}"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().start_search_endpoint()}"
    headers = {"Authorization": f"Token {token}"}
    request_data = {"regionId": get_region_id()}
    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    response_str = requests.post(url, headers=headers, data=request_data, files=files)
    response_json = response_str.json()
    print(response_json)
    job_id = response_json["jobId"]
    cancel_federated_url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_identify_cancel_federated_endpoint(job_id)}"
    cancel_federated_resp = requests.put(cancel_federated_url, headers=headers)
    response_json = cancel_federated_resp.json()
    return response_str, response_json


def get_query_alien_federated_identification_log():
    token = login_token()
    result_deleted = False
    count = 20
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_query_alien_federated_identification_log_endpoint(result_deleted, count)}"
    print(url)
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    print(response_str)
    return response_str, response_json


def visitor_search_request():
    test_data_row = 6
    token = login_token()
    data = start_search_test_data(test_data_row)
    start = data[0]
    limit = data[1]
    sort_direction = data[2]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_visitor_search_endpoint(start, limit, sort_direction)}"
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"startTime": data[3]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, headers=headers, data=request_data)
    response_json = response_str.json()
    print(response_json)
    return request_data, response_str, response_json


def visitor_search_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().visitor_search_test_data_sheet_name(), row_no, x))
    return data


def get_verify_visitor_count_by_zone():
    test_data_row = 8
    token = login_token()
    data = verify_visitor_count_by_zone_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_visitor_count_by_zone_endpoint()}"
    print(url)
    query_param = {"AgeBucket": data[0], "Male": data[1], "Female": data[2], "White": data[3], "Black": data[4],
                   "Asian": data[5], "Indian": data[6], "Other" : data[7], "UnknownEthnicity": data[8],
                   "StartAge": data[9], "EndAge": data[10], "Ascending": data[11], "Count": data[12]
                   }
    response_str = requests.get(url, headers=headers, params=query_param)
    response_json = response_str.json()
    print(response_str)
    return response_str, response_json


def verify_visitor_count_by_zone_test_data(row_no):
    data = []
    for x in range(3, 16):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().visitor_search_test_data_sheet_name(), row_no, x))
    return data

