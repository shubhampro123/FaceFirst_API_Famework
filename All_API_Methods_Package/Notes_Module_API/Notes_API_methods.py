import json
from pathlib import Path

import requests

from API_Utilities.Api_Base import time_entry, login_token, API_Base_Utilities, response_validation, excel_result
from All_API_Methods_Package.Identify_and_Enroll_Module_API.Identify_Enroll_Module_API import create_enrollment_request
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_INI_Config_Files.Expected_Notes_Response_Msg_ini import Read_notes_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Notes_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().notes_result_sheet_name()

    def verify_create_notes(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_notes_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            note_id = self.json_response["data"]["id"]
            self.exp_msg = Read_notes_Response_msg().create_notes_success_msg(note_id)
            self.act_msg = self.json_response["data"]["message"]
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
            excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_group_Test_01:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_notes_using_note_id(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            ex_note_id = create_notes_request()[2]["data"]["id"]
            response_list = get_notes_using_id(ex_note_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            ac_notes_id = self.json_response["notesInfo"]["notes"][0]["noteID"]
            self.act_msg = ac_notes_id
            if response_validation(self.response) and ex_note_id == ac_notes_id:
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
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_02:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_update_notes(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            note_id = create_notes_request()[2]["data"]["id"]
            response_list = edit_notes_request(note_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.exp_msg = Read_notes_Response_msg().update_notes_success_msg()
            self.act_msg = self.json_response["result"]["message"]
            if response_validation(self.response) and self.exp_msg == self.act_msg:
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
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_03:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_notes_using_note_id(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            note_id = create_notes_request()[2]["data"]["id"]
            response_list = delete_notes_request(note_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            self.exp_msg = Read_notes_Response_msg().delete_notes_success_msg(note_id)
            self.act_msg = self.json_response["message"]
            if response_validation(self.response) and self.exp_msg == self.act_msg:
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
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_04:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_clear_notes(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            note_id = create_notes_request()[2]["data"]["id"]
            response_list = clear_notes_request(note_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.exp_msg = Read_notes_Response_msg().clear_notes_success_msg()
            self.act_msg = self.json_response["result"]["message"]
            if response_validation(self.response) and self.exp_msg == self.act_msg:
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, "Test_05", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_05:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_add_image_to_note_using_note_id(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            note_id = create_notes_request()[2]["data"]["id"]
            response_list = add_image_request(note_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.exp_msg = Read_notes_Response_msg().add_image_to_notes_success_msg()
            self.act_msg = self.json_response["result"]["status"]
            if response_validation(self.response) and self.exp_msg == self.act_msg:
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
            excel_result(self.row, "Test_06", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_06:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_image_using_note_id(self):
        result = []
        try:
            self.row = 8
            time_entry(self.row, "start_time", self.sheet_name)
            note_id = create_notes_request()[2]["data"]["id"]
            self.response = get_image_using_note_id(note_id)
            if response_validation(self.response):
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
            self.log.info(f"test_notes_Test_07:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_image_using_note_id(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            note_id = create_notes_request()[2]["data"]["id"]
            image_id = get_notes_using_id(note_id)[1]["notesInfo"]["notes"][0]["imageIDs"][0]
            response_list = delete_image_request(note_id, image_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.exp_msg = Read_notes_Response_msg().delete_image_to_notes_success_msg(note_id)
            self.act_msg = self.json_response["message"]
            if response_validation(self.response) and self.exp_msg == self.act_msg:
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
            self.log.info(f"test_notes_Test_08:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_notes_search(self):
        result = []
        try:
            self.row = 10
            time_entry(self.row, "start_time", self.sheet_name)
            create_notes_request()
            response_list = notes_search_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            if response_validation(self.response):
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
            self.log.info(f"test_notes_Test_09:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_notes_aggregates_by_geospatial(self):
        result = []
        try:
            self.row = 11
            time_entry(self.row, "start_time", self.sheet_name)
            create_notes_request()
            response_list = aggregates_by_geospatial_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            if response_validation(self.response):
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
            self.log.info(f"test_notes_Test_10:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_by_enrollment(self):
        result = []
        try:
            self.row = 12
            time_entry(self.row, "start_time", self.sheet_name)
            case_id = create_notes_to_a_person_request()[3]
            response_list = get_by_enrollment_request(case_id)
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
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
            excel_result(self.row, "Test_11", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_notes_Test_11:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


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
    headers = {"Authorization": f"Token {token}"}
    response_str = requests.post(url, request_body, headers=headers, files=files)
    response_json = response_str.json()
    return request_body, response_str, response_json


def get_profile_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}api/Profiles"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_json["profiles"][0]["profileId"]


def create_enrollment_data(row_no):
    data = []
    for x in range(3, 20):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data


def get_notes_using_id(note_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_notes_endpoint(note_id)}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def edit_notes_request(note_id):
    test_data_row = 4
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().update_notes_endpoint()}"
    data = edit_notes_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"gender": data[0], "build": data[1], "bodyMarkings": data[2], "narrativeDesc": data[3],
                    "action": data[4], "storeId": data[5], "caseNumber": data[6],
                    "timeIncident": data[7], "reportedBy": data[8], "reportedLoss": str(data[9]),
                    "caseEventType": data[10],
                    "activityType": data[11], "heightType": data[12], "methodOffence": data[13],
                    "NoteId": note_id, "SetCases": data[15]
                    }
    request_data = json.dumps(request_body)
    print(request_data)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    print(response_json)
    return request_body, response_str, response_json


def edit_notes_test_data(row_no):
    data = []
    for x in range(3, 19):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data


def delete_notes_request(note_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().delete_notes_endpoint(note_id)}"
    response_str = requests.delete(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def clear_notes_request(note_id):
    test_data_row = 6
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().clear_notes_endpoint()}"
    data = clear_notes_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"fields": [data[0]],
                    "NoteId": note_id
                    }
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def clear_notes_test_data(row_no):
    data = []
    for x in range(3, 5):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data


def add_image_request(note_id):
    test_data_row = 8
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\img2.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().images_bulk_endpoint(note_id)}"
    data = add_image_test_data(test_data_row)
    request_body = {
        "NoteId": note_id
    }

    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    headers = {"Authorization": f"Token {token}"}
    response_str = requests.post(url, request_body, headers=headers, files=files)
    response_json = response_str.json()
    return request_body, response_str, response_json


def add_image_test_data(row_no):
    data = []
    for x in range(3, 5):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data


def get_image_using_note_id(note_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_images_endpoint(note_id)}"
    request_body = {"thumbnail_width": "200"}
    response_str = requests.get(url, headers=headers, params=request_body)
    return response_str


def delete_image_request(note_id, image_id):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().delete_images_endpoint(note_id)}"
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"noteId": note_id, "imageIds": [image_id]}
    request_data = json.dumps(request_body)
    response_str = requests.delete(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def notes_search_request():
    test_data_row = 10
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().note_search_endpoint()}"
    data = notes_search_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"caseNumber": data[0],
                    "storeId": data[1],
                    "Count": data[2],
                    "IncludeCaseIds": data[3],
                    "offset": data[4],
                    "OrderBy": data[5]
                    }
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def notes_search_test_data(row_no):
    data = []
    for x in range(3, 9):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data


def aggregates_by_geospatial_request():
    test_data_row = 12
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().aggregates_by_geospatial_endpoint()}"
    data = aggregates_by_geospatial_test_data(test_data_row)
    lat_long_list = data[0].split(",")
    lat = float(lat_long_list[0])
    lon_g = float(lat_long_list[1])
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"geoCenter": [lat, lon_g],
                    "geoMaxDistance": data[1],
                    "regionIds": [get_region_id()],
                    }
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def get_region_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_zones_endpoint()}"
    response_str = requests.get(url, headers=headers)
    return response_str.json()["zoneInfo"]["zones"][1]["regionId"]


def aggregates_by_geospatial_test_data(row_no):
    data = []
    for x in range(3, 6):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data


def create_notes_to_a_person_request():
    case_id = create_enrollment_request()[3]
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_notes_endpoint()}"
    data = create_enrollment_data(2)
    request_body = {"gender": data[0],
                    "caseEventType": data[10],
                    "ProfileId": get_profile_id(),
                    "CaseId": case_id,
                    "SetCases": True,
                    }

    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    headers = {"Authorization": f"Token {token}"}
    response_str = requests.post(url, request_body, headers=headers, files=files)
    response_json = response_str.json()
    return request_body, response_str, response_json, case_id


def get_by_enrollment_request(case_id):
    test_data_row = 14
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_by_enrollment_endpoint()}"
    data = get_by_enrollment_test_data(test_data_row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"caseId": case_id,
                    "count": data[1],
                    "includeCaseIds": data[2],
                    "offset": data[3],
                    "orderBy": data[4]
                    }
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json


def get_by_enrollment_test_data(row_no):
    data = []
    for x in range(3, 8):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.notes_test_data_sheet_name, row_no, x))
    return data
