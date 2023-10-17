import json
from pathlib import Path

import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities
from All_API_Methods_Package.Enrollment_Group_Module_API.Enrollment_Group_API_Methods import \
    create_enrollment_group_request
from All_API_Methods_Package.Users_Module_API.Users_API_Methods import select_region
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class All_Module_Search_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().all_module_search_result_sheet_name()

    def verify_events_search(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_event_search()
            self.response = response_list[0]
            print(self.response)
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
            print(ex)
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Account_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_users_search(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_user_by_id_request()
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
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Users_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_notes_search(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            create_notes_request()
            response_list = notes_search_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            if response_validation(self.response):
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_03:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_visitors_search(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            create_notes_request()
            response_list = get_visitors_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            if response_validation(self.response):
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
            print(ex)
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_04:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_enrollments_search(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_enrollment_group_by_id()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
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
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_05:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_visitor_search_jobs_search(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_visitor_search_jobs_search()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
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
            excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_06:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


##################################################################################
def get_event_search():
    token = login_token()
    print(token)
    headers = {"Token": token, "Content-Type": "application/json"}
    data = events_test_data(2)
    print(data)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().events_search_endpoint()}"
    print(url)
    params = {"Start": "0", "Limit": "20", "SortDirection": "Ascending"}
    request_body = {"enrollmentGroupIds": [data[0]], "startTime": data[1], "endTime": data[2],
                    "tags": [data[3]], "regionIds": [select_region()], "cameraIds": [data[5]],
                    "eventIds": [data[6]]}
    request_data = json.dumps(request_body)
    print(request_data)
    response_str = requests.post(url, data=request_data, headers=headers, params=params)
    response_json = response_str.json()
    print(response_json)
    return response_str, response_json


def get_user_by_id_request():
    data = get_user_request()
    user_id = data[2]
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_users_by_id_endpoint()}"
    params = {"id": user_id}
    response_str = requests.get(url, headers=headers, params=params)
    response_json = response_str.json()
    return response_str, response_json


def get_user_request():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_users_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    user_id = response_json[1]["id"]
    accountId = response_json[0]["accountId"]
    return response_str, response_json, user_id, accountId


def get_visitors_request():
    token = login_token()
    headers = {"Token": token, "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().visitors_search_end_point()}"
    data = visitors_search_data(6)
    print(data)
    params = {"Start": "0", "Limit": "20", "SortDirection": "Ascending"}
    request_body = {"startTime": data[0], "endTime": data[1], "startAge": data[2],
                    "endAge": data[3], "isMale": data[4], "regionIds": [select_region()], "trackId": data[6],
                    "visitorIds": [data[6]]}
    request_data = json.dumps(request_body)
    print(request_data)
    response_str = requests.post(url, data=request_data, headers=headers, params=params)
    print(response_str)
    response_json = response_str.json()
    print(response_json)
    return request_body, response_str, response_json


def notes_search_request():
    test_data_row = 4
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().note_search_endpoint()}"
    print(url)
    data = notes_search_test_data(test_data_row)
    headers = {"Token": token, "Content-Type": "application/json"}
    request_body = {"caseNumber": data[0],
                    "storeId": data[1],
                    "Count": data[2],
                    "IncludeCaseIds": data[3],
                    "offset": data[4],
                    "OrderBy": data[5]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def create_notes_request():
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_notes_endpoint()}"
    data = create_enrollment_data(2)
    request_body = {"gender": data[0], "build": data[1], "bodyMarkings": data[2], "narrativeDesc": data[3],
                    "action": data[4], "storeId": data[5], "caseNumber": data[6],
                    "timeIncident": data[7], "reportedBy": data[8], "reportedLoss": data[9],
                    "caseEventType": data[10],
                    "activityType": data[11], "heightType": data[12], "methodOffence": data[13],
                    "ProfileId": get_profile_id(), "ClearGeo": data[15], "geo": data[16],
                    }

    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    headers = {"Token": token}

    print(request_body)
    response_str = requests.post(url, request_body, headers=headers, files=files)
    response_json = response_str.json()
    print("response_json", response_json)
    return request_body, response_str, response_json


def get_profile_id():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}api/Profiles"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_json["profiles"][0]["profileId"]


def get_enrollment_group_by_id():
    token = login_token()
    headers = {"Token": token}
    data = create_enrollment_group_request(3)
    form_data = {"id": data[3]}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_enrollment_group_endpoint()}"
    response_str = requests.get(url, params=form_data, headers=headers)
    response_json = response_str.json()
    return form_data, response_str, response_json


def get_visitor_search_jobs_search():
    token = login_token()
    headers = {"Token": token, "Content-Type": "application/json"}
    user_id = get_user_request()
    data = visitors_search_job_data(8)
    print(data)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_visitor_search_jobs_search_endpoint()}"
    form_data = {"EndDate": data[0], "ResultsDeleted": data[1], "StartDate": data[2],
                 "UserId": user_id[2], "count": data[4], "offset": data[5]}
    response_str = requests.get(url, params=form_data, headers=headers)
    response_json = response_str.json()
    return form_data, response_str, response_json


def events_test_data(row_no):
    data = []
    for x in range(3, 10):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().all_module_search_test_data_sheet_name(), row_no, x))
    return data


def notes_search_test_data(row_no):
    data = []
    for x in range(3, 9):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().all_module_search_test_data_sheet_name(), row_no, x))
    return data


def create_enrollment_data(row_no):
    data = []
    for x in range(3, 20):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data


def visitors_search_data(row_no):
    data = []
    for x in range(3, 12):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().all_module_search_test_data_sheet_name(), row_no, x))
    return data


def visitors_search_job_data(row_no):
    data = []
    for x in range(3, 9):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().all_module_search_test_data_sheet_name(), row_no, x))
    return data
