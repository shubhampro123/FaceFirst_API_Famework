import json
import random
import time
from pathlib import Path

import requests

from API_Utilities.Api_Base import time_entry, login_token, API_Base_Utilities, response_validation, excel_result
from All_API_Methods_Package.Enrollment_Group_Module_API.Enrollment_Group_API_Methods import \
    create_enrollment_group_with_addCaseGroupZone_request
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_INI_Config_Files.Expected_Identify_Enroll_Response_Msg_ini import \
    Read_identify_enroll_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Identify_Enroll_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().identify_enroll_test_result_sheet_name()

    def verify_create_enrollment(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_enrollment_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.act_msg = self.json_response["enroll"]["success"]
            self.exp_msg = Read_identify_enroll_Response_msg().create_enrollment_success_msg();
            if response_validation(self.response) and self:
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
            self.log.info(f"test_enrollment_group_Test_01:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_clear_enrollment_info(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = clear_enrollment_info_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
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
            excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_02:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_query_Enrollment_FaceInfo(self):
        result = []
        try:
            self.row = 4
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = query_Enrollment_FaceInfo_request()
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
            excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_03:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_enrollment_profiles(self):
        result = []
        try:
            self.row = 5
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_enrollment_profiles_request()
            self.response = response_list[0]
            self.json_response = response_list[1]
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
            excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_04:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_identify_enrollment(self):
        result = []
        try:
            self.row = 6
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = identify_enrollment()
            self.response = response_list[0]
            self.json_response = response_list[1]
            if response_validation(self.response):
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
            self.log.info(f"test_enrollment_group_Test_05:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_search_enrollments(self):
        result = []
        try:
            self.row = 7
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = search_enrollment_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            if response_validation(self.response):
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
            self.log.info(f"test_enrollment_group_Test_06:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_edit_enrollments(self):
        result = []
        try:
            self.row = 8
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = edit_enrollment_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            enroll_id = response_list[3]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_identify_enroll_Response_msg().edit_enrollment_success_msg(enroll_id)
            if response_validation(self.response) and self.act_msg == self.exp_msg:
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
            self.log.info(f"test_enrollment_group_Test_07:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_delete_enrollments(self):
        result = []
        try:
            self.row = 9
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = delete_enrollment_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
            enroll_id = response_list[3]
            self.act_msg = self.json_response["message"]
            self.exp_msg = Read_identify_enroll_Response_msg().delete_enrollment_success_msg(enroll_id)
            if response_validation(self.response) and self.act_msg == self.act_msg:
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

    def verify_add_enrollment_with_image(self):
        result = []
        try:
            self.row = 10
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_enrollment_with_image()
            self.response = response_list[0]
            self.json_response = response_list[1]
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
            self.log.info(f"test_enrollment_group_Test_09:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def Verify_Get_enrollment_image_by_id(self):
        result = []
        try:
            self.row = 11
            time_entry(self.row, "start_time", self.sheet_name)
            self.response = get_enrollment_by_id()
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
            self.log.info(f"test_enrollment_group_Test_10:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def Verify_remove_enrollment_image_by_id(self):
        result = []
        try:
            self.row = 12
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = remove_enrollment_images_request()
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
            self.log.info(f"test_enrollment_group_Test_11:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_create_enrollment_with_id_and_notification_group(self):
        result = []
        try:
            self.row = 13
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_enrollment_with_id_and_notification_group_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
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
            excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_12:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_query_enrollment_info(self):
        result = []
        try:
            self.row = 14
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = query_enrollment_info_request()
            self.r_body = response_list[0]
            self.response = response_list[1]
            self.json_response = response_list[2]
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
            excel_result(self.row, "Test_12", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                         False, self.sheet_name)
            self.log.info(f"test_enrollment_group_Test_12:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


################################ Reuse Method #######################################

def create_enrollment_request():
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_endpoint()}"
    data = create_enrollment_data(2)
    request_body = {"CgroupId": get_C_group_Id(), "OptOut": data[1], "Basis": data[2], "Action": data[3],
                    "ActivityType": data[4], "BodyMarkings": data[5], "Build": data[6],
                    "CaseEventType": data[7], "CaseNumber": data[8], "Enabled": data[9], "Gender": data[10],
                    "HeightType": data[11], "MethodOffence": data[12], "NarrativeDesc": data[13],
                    "ProfileId": get_profile_id(), "ReportedBy": data[15], "ReportedLoss": data[16],
                    "StoreId": data[17], "TimeIncident": data[18], "RegionId": select_region()}

    files = [
        ('Image', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    headers = {"Authorization": f"Token {token}"}
    print(request_body)
    response_str = requests.post(url, request_body, headers=headers, files=files, verify=False)
    response_json = response_str.json()
    caseId = response_json["enroll"]["caseId"]
    return request_body, response_str, response_json, caseId


def create_enrollment_with_image():
    enroll = search_enrollment_request()[2]
    caseId = ""
    # random_index = random.randint(0, len(enroll["caseInfo"]["cases"]) - 1)
    # caseId = enroll["caseInfo"]["cases"][random_index]["caseId"]
    for x in range(0, len(enroll["caseInfo"]["cases"])):
        if x == len(enroll["caseInfo"]["cases"]) - 1:
            caseId = enroll["caseInfo"]["cases"][x]["caseId"]
    print(caseId)
    token = login_token()
    params = {"caseId": caseId}
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\img5.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().add_enrollment_with_image_end_point()}"
    files = [
        ('Image', ('img5.png', open(image_path, 'rb'), 'image/png'))
    ]
    headers = {"Authorization": f"Token {token}"}
    response_str = requests.post(url, params=params, headers=headers, files=files, verify=False)
    response_json = response_str.json()
    print(response_json)
    return response_str, response_json


def get_enrollment_by_id():
    enroll = create_enrollment_request()
    caseId = enroll[3]
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_enrollment_end_point(caseId)}"
    response_str = requests.get(url, headers=headers, verify=False)
    return response_str


def remove_enrollment_images_request():
    token = login_token()
    data = get_face_id_using_case_id()
    add_enrollment_image(data[1])
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().remove_enrollment_by_id()}"
    request_body = {"caseId": data[1], "images": [data[0]]}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    return request_body, response_str, response_json


def get_face_id_using_case_id():
    enroll = create_enrollment_request()
    caseId = enroll[3]
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_enrollment_data_by_id(caseId)}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    face_id = response_json["faceIds"][0]
    return face_id, caseId


def edit_enrollment_request():
    enroll = create_enrollment_request()
    caseId = enroll[3]
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_endpoint()}"
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    data = edit_enrollment(10)
    request_body = {"expiration": data[0], "cgroupId": get_C_group_Id(), "storeId": data[2], "caseNumber": data[3],
                    "reportedLoss": data[4], "timeIncident": data[5], "action": data[6],
                    "profileId": get_profile_id(), "optOut": data[8], "enabled": data[9], "image": data[10],
                    "caseEventType": data[11], "activityType": data[12], "methodOffence": data[13],
                    "reportedBy": data[14], "build": data[15], "bodyMarkings": data[16], "gender": data[17],
                    "narrativeDesc": data[18], "heightType": data[19], "regionId": select_region(),
                    "caseId": caseId, "setCgroups": data[22], "cgroupIds": [get_C_group_Id()],
                    "basis": data[24]
                    }
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    enroll_id = response_json["data"]
    return request_body, response_str, response_json, enroll_id


def delete_enrollment_request():
    enroll = create_enrollment_request()
    caseId = enroll[3]
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_endpoint()}"
    headers = {"Authorization": f"Token {token}"}
    params = {"caseId": caseId, "deleteAlerts": False}
    response_str = requests.delete(url, headers=headers, params=params, verify=False)
    response_json = response_str.json()
    enroll_id = response_json["data"]
    return params, response_str, response_json, enroll_id


def clear_enrollment_info_request():
    data = create_enrollment_request()
    caseId = data[3]
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().clear_enrollment_info_endpoint()}"
    data = clear_enrollment_data(4)
    request_body = {"fields": [data[0]], "caseId": caseId}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json


def search_enrollment_request():
    # create_enrollment_request()
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}api/Enrollments/searchEnrollments"
    data = identify_search_enrollment(8)
    request_body = {"fields": [{"key": data[0], "value": data[1]}], "count": data[2], "ascending": data[3],
                    "detailLevel": data[4], "isExact": data[5], "offset": data[6], "orderBy": data[7],
                    "startEnrollmentDate": data[8], "endEnrollmentDate": data[9], "startExpirationDate": data[10],
                    "endExpirationDate": data[11], "notInCGroup": data[12], "searchInOr": data[13],
                    "cgroup_id": get_C_group_Id()}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json


def query_Enrollment_FaceInfo_request():
    data = create_enrollment_request()
    caseId = data[3]
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().query_enrollment_info_endpoint()}"
    request_body = {"caseId": caseId}
    response_str = requests.get(url, params=request_body, headers=headers, verify=False)
    response_json = response_str.json()
    return request_body, response_str, response_json


def get_enrollment_profiles_request():
    create_enrollment_request()
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_enrollment_profiles_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def identify_enrollment():
    create_enrollment_request()
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    headers = {"Authorization": f"Token {token}"}
    data = identify_enrollment_data(6)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().identify_enrollment_endpoint()}"
    request_body = {"DetailLevel": data[0], "MaxMatches": data[1], "IncludeMatrics": data[2]}
    files = [
        ('Image', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    response_str = requests.post(url, data=request_body, headers=headers, files=files, verify=False)
    response_json = response_str.json()
    return response_str, response_json


def get_profile_id():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_profile_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    return response_json["profiles"][0]["profileID"]


def select_region():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_region_endpoint()}"
    response_str = requests.get(url, headers=headers, verify=False)
    response_json = response_str.json()
    region = response_json["zoneInfo"]["zones"][1]["regionId"]
    return region


def add_enrollment_image(case_id):
    token = login_token()
    params = {"caseId": case_id}
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\img2.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().add_enrollment_with_image_end_point()}"
    files = [
        ('Image', ('image.png', open(image_path, 'rb'), 'img2/png'))
    ]
    headers = {"Authorization": f"Token {token}"}
    response_str = requests.post(url, params=params, headers=headers, files=files, verify=False)


def create_enrollment_with_id_and_notification_group_request():
    data = create_enrollment_request()
    case_id = data[3]
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enroll_with_id_ng(case_id)}"
    request_body = {"regionId": select_region(), "enrollmentId": case_id, "cameraId": "null",
                    "enrollmentGroupIds": [get_C_group_Id()]}
    print(request_body)
    request_data = json.dumps(request_body)
    response_str = requests.post(url, request_data, headers=headers, verify=False)
    response_json = response_str.json()
    print(response_json)
    return request_data, response_str, response_json


def query_enrollment_info_request():
    data = create_enrollment_request()
    case_id = data[3]
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().query_enrollment_info_by_id()}"
    request_body = [case_id]
    request_data = json.dumps(request_body)
    response_str = requests.post(url, request_data, headers=headers, verify=False)
    response_json = response_str.json()
    return request_data, response_str, response_json


def get_C_group_Id():
    data = create_enrollment_group_with_addCaseGroupZone_request()
    return data[4]


def create_enrollment_data(row_no):
    data = []
    for x in range(3, 23):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().identify_enroll_test_data_sheet_name(), row_no, x))
    return data


def clear_enrollment_data(row_no):
    data = []
    for x in range(3, 5):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().identify_enroll_test_data_sheet_name(), row_no, x))
    return data


def identify_enrollment_data(row_no):
    data = []
    for x in range(3, 6):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().identify_enroll_test_data_sheet_name(), row_no, x))
    return data


def identify_search_enrollment(row_no):
    data = []
    for x in range(3, 18):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().identify_enroll_test_data_sheet_name(), row_no, x))
    return data


def edit_enrollment(row_no):
    data = []
    for x in range(3, 28):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().identify_enroll_test_data_sheet_name(), row_no, x))
    return data
