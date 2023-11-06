import json
import time
from pathlib import Path

import requests

from API_Utilities.Api_Base import time_entry, excel_result, login_token, API_Base_Utilities, response_validation
from All_API_Methods_Package.Identify_and_Enroll_Module_API.Identify_Enroll_Module_API import create_enrollment_data, \
    get_C_group_Id, get_profile_id, select_region
from All_API_Methods_Package.Notification_groups_Module_API.Notification_Groups_Methods import get_user_info
from All_API_Methods_Package.Users_Module_API.Users_API_Methods import random_number
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils
from Config_Package.Excel_Config_Files.XLUtils import getRowCount


class Integration_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().integration_result_sheet_name()

    def integration_end_to_end(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = integration_end_to_end_request()
            self.response = response_list[1]
            if False not in response_list[0]:
                excel_result(self.row, "Test_01", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
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
            self.log.info(f"test_integration_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def second_integration_end_to_end_VS_with_pic(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = integration_end_to_end_VS_with_pic_request()
            self.response = response_list[1]
            if False not in response_list[0]:
                excel_result(self.row, "Test_02", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
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
            self.log.info(f"test_integration_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def third_integration_end_to_end_VS_with_pic_metadata(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = integration_end_to_end_VS_with_pic_meta_data_request()
            self.response = response_list[1]
            if False not in response_list[0]:
                excel_result(self.row, "Test_03", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
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
            self.log.info(f"test_integration_Test_03_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def fourth_integration_end_to_end_VS_with_only_metadata(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = integration_end_to_end_VS_with_only_meta_data_request()
            self.response = response_list[1]
            if False not in response_list[0]:
                excel_result(self.row, "Test_04", self.r_body, self.json_response, self.response.status_code,
                             self.act_msg, True, self.sheet_name)
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
            self.log.info(f"test_integration_Test_04_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


####################################################################################################################


def create_request_for_user_role(row):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().user_role_endpoint()}"
    data = get_data(row, 3, 30)
    role_name = f"{data[0]}{random_number()}"
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
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
    role_id = response_json["id"]
    result = response_validation(response_str)
    return request_data, response_str, response_json, role_name, role_id, result


def get_user_info_request():
    token = login_token()
    headers = {"Authorization": f"Token {token}"}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_user_info_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    region_id = response_json["regionId"]
    return response_str, response_json, region_id


def user_request_for_create_user(row):
    result = []
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().users_endpoint()}"
    data = get_data(row, 31, 57)
    user_role = create_request_for_user_role(row)
    result.append(user_role[5])
    region_id = get_user_info_request()
    result.append(region_id[2])
    headers = {"Authorization": f"Token {token}"}
    form_data = {"auth_params": data[0], "company": data[1], "title": data[2], "department": data[3],
                 "enabled": data[4], "fname": data[5], "mname": data[6], "lname": data[7],
                 "addr1": data[8], "addr2": data[9], "city": data[10], "state": data[11],
                 "zip": data[12], "email": data[13], "aemail": data[14], "hphone": data[15],
                 "wphone": data[16], "fphone": data[17], "aphone": data[18], "phone_type": data[19],
                 "provider": data[20], "timezone": data[21], "urole_id": user_role[4],
                 "region_id": data[23], "username": f"{data[24]}{random_number()}", "password": data[25]}
    response_str = requests.post(url, form_data, headers=headers)
    response_json = response_str.json()
    user_id = response_json["userId"]
    account_id = response_json["accountId"]
    username = response_json["userName"]
    current_password = data[25]
    result.append(response_validation(response_str))
    return form_data, response_str, response_json, user_id, account_id, username, current_password, result


def create_notification_group(row):
    user_info_list = get_user_info()
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().post_alert_groups_endpoint()}"
    data = get_data(row, 57, 63)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    username = f"{data[2]}{random_number()}"
    request_body = {"agroupID": bool(data[0]), "description": data[1], "name": username, "ownerID": user_info_list[0],
                    "set_cgroups": data[4]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    a_group_id = response_json["data"]
    result = response_validation(response_str)
    return request_body, response_str, response_json, username, a_group_id, result


def create_enrollment_group_request(row):
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    data = get_data(row, 65, 74)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_group_endpoint()}"
    name = f"{data[0]}{random_number()}"
    request_body = {"name": name, "description": data[1], "faceThreshold": data[2], "maskedFaceThreshold": data[3],
                    "eventsSuppressionInterval": data[4], "priority": data[5], "seriousOffender": data[6],
                    "alertHexColor": data[7], "activeThreat": data[8]}
    request_data = json.dumps(request_body)
    response_str = requests.post(url, data=request_data, headers=headers)
    response_json = response_str.json()
    data = response_json["data"]
    return request_body, response_str, response_json, data


def add_user_to_alert_group_request(row, group_id):
    result = []
    user_info_list = user_request_for_create_user(row)
    result.append(user_info_list[7])
    # test_data_row = 7
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_user_to_alert_group()}"
    a_group_id = group_id
    result.append(a_group_id[5])
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"agroupID": a_group_id[4], "userId": user_info_list[3]}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    result.append(response_validation(response_str))
    return request_body, response_str, response_json, result


def add_enrollment_to_alert_group_request(row):
    token = login_token()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().put_enrollment_group_to_alert_group()}"
    enrollment_group_id = create_enrollment_group_request(row)
    alert_id = create_notification_group(row)
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    request_body = {"CGroupID": enrollment_group_id[3], "AGroupID": alert_id[4]}
    request_data = json.dumps(request_body)
    response_str = requests.put(url, data=request_data, headers=headers)
    response_json = response_str.json()
    return request_body, response_str, response_json, alert_id


def integration_end_to_end_request():
    result = []
    response_str = ""
    row_count = getRowCount(API_Base_Utilities.test_data_excel_path,
                            Read_API_Endpoints().integration_Test_data_sheet_name())
    for x in range(2, row_count + 1):
        row = x
        data = add_enrollment_to_alert_group_request(row)[3]
        response = add_user_to_alert_group_request(row, data)
        result.append(response[3])
        response_str = response[1]
    return result, response_str


def get_data(row_no, start_column, end_column):
    data = []
    for x in range(start_column, end_column):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().integration_Test_data_sheet_name(), row_no, x))
    return data


def start_search_request():
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\img5.png"
    region_id = get_user_info_request()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().start_search_endpoint()}"
    files = [
        ('Images', ('img5.png', open(image_path, 'rb'), 'image/png'))
    ]
    headers = {"Authorization": f"Token {token}"}
    request_data = {"threshold": 0.25, "regionId": region_id[2]}
    response_str = requests.post(url, headers=headers, files=files, data=request_data)
    response_json = response_str.json()
    job_id = response_json["jobId"]
    # role_id = response_json["id"]
    return response_str, response_json, job_id


def get_fed_search_status_request(job_id):
    token = login_token()
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
    params = {'jobId': job_id}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().fed_search_status_endpoint(job_id)}"
    print(url)
    response_str = requests.get(url, params=params, headers=headers)
    time.sleep(3)
    print(response_str)
    response_json = response_str.json()
    image_id = []
    for x in range(0, 5):
        time.sleep(1)
        image_id.append(response_json["matched"][x]["id"])
    return response_str, image_id


def create_enrollment_request(image_id):
    token = login_token()
    # image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\img2.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_enrollment_endpoint()}"
    data = create_enrollment_data(2)
    request_body = {"CgroupId": get_C_group_Id(), "OptOut": data[1], "Basis": data[2], "Action": data[3],
                    "ActivityType": data[4], "BodyMarkings": data[5], "Build": data[6],
                    "CaseEventType": data[7], "CaseNumber": data[8], "Enabled": data[9], "Gender": data[10],
                    "HeightType": data[11], "MethodOffence": data[12], "NarrativeDesc": data[13],
                    "ProfileId": get_profile_id(), "ReportedBy": data[15], "ReportedLoss": data[16],
                    "StoreId": data[17], "TimeIncident": data[18], "RegionId": select_region()}

    image = get_image_using_image_id(image_id)
    files = [
        ('Image', ('image.jpg', image.content, 'image/jpeg'))
    ]
    headers = {"Authorization": f"Token {token}"}
    response = requests.post(url, headers=headers, data=request_body,  files=files)
    response_json = response.json()
    caseId = response_json.get("enroll", {}).get("caseId", None)
    print(response_json)
    return request_body, response, response_json, caseId, image


def get_image_using_image_id(image_id):
    token = login_token()
    url = f"https://ff-india-qa10.eastus2.cloudapp.azure.com/api/media/{image_id}/visitor?use_thumbnail=1&blur_images=0"
    headers = {"Authorization": f"Token {token}"}
    response = requests.get(url, headers=headers)
    print(response.content)
    return response


def integration_end_to_end_VS_with_pic_request():
    result = []
    response_str = ""
    start_search_resp = start_search_request()
    job_id = start_search_resp[2]
    result.append(response_validation(start_search_resp[0]))
    fed_search_resp = get_fed_search_status_request(job_id)
    image_id = fed_search_resp[1]
    print(image_id)
    result.append(response_validation(fed_search_resp[0]))
    for x in range(0, len(image_id)):
        time.sleep(2)
        create_enroll_resp = create_enrollment_request(image_id[x])
        result.append(response_validation(create_enroll_resp[1]))
        response_str = create_enroll_resp[1]
        case_id = create_enroll_resp[3]
        add_notes_resp = add_notes_to_enrollment_request(case_id, create_enroll_resp[4])
        result.append(response_validation(add_notes_resp[1]))

    identify_enrollment_index_resp = identify_enrollment_index()
    result.append(identify_enrollment_index_resp[0])
    result.append(identify_enrollment_index_resp[2])
    return result, response_str


def add_notes_to_enrollment_request(case_id, image):
    token = login_token()
    # image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().create_notes_endpoint()}"
    data = create_notes_data(2)
    request_body = {"gender": data[0], "build": data[1], "bodyMarkings": data[2], "narrativeDesc": data[3],
                    "action": data[4], "storeId": data[5], "caseNumber": data[6],
                    "timeIncident": data[7], "reportedBy": data[8], "reportedLoss": data[9],
                    "caseEventType": data[10],
                    "activityType": data[11], "heightType": data[12], "methodOffence": data[13],
                    "ProfileId": data[14], "CaseId": case_id, "SetCases": data[16],
                    }

    # image = get_image_using_image_id(image_id)
    files = [
        ('Image', ('image.jpg', image.content, 'image/jpeg'))
    ]
    headers = {"Authorization": f"Token {token}"}
    response_str = requests.post(url, headers=headers, data=request_body,  files=files)
    response_json = response_str.json()
    return request_body, response_str, response_json


def identify_enrollment_index():
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\img5.png"
    headers = {"Authorization": f"Token {token}"}
    data = identify_enrollment_data(6)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().identify_enrollment_endpoint()}"
    request_body = {"DetailLevel": data[0], "MaxMatches": data[1], "IncludeMatrics": data[2]}
    files = [
        ('Images', ('img5.png', open(image_path, 'rb'), 'image/png'))
    ]
    response_str = requests.post(url, data=request_body, headers=headers, files=files)
    response_json = response_str.json()
    print(response_json)
    matches = response_json["id"]["matches"]
    print(matches)
    index = []
    for x in range(0, len(matches)):
        print(matches[x]["score"])
        index.append(matches[x]["score"] is not "")
    index_result = False
    if False not in index:
        index_result = True
    return response_str, response_json, index_result


def identify_enrollment_data(row_no):
    data = []
    for x in range(3, 6):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().identify_enroll_test_data_sheet_name(), row_no, x))
    return data


def create_notes_data(row_no):
    data = []
    for x in range(12, 29):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().integration_Test_with_metadata_data_sheet_name(), row_no, x))
    return data


def integration_end_to_end_VS_with_pic_meta_data_request():
    result = []
    response_str = ""
    start_search_resp = start_search_with_pic_metadata_request()
    job_id = start_search_resp[2]
    result.append(response_validation(start_search_resp[0]))
    fed_search_resp = get_fed_search_status_request(job_id)
    image_id = fed_search_resp[1]
    result.append(response_validation(fed_search_resp[0]))
    for x in range(0, len(image_id)):
        time.sleep(2)
        create_enroll_resp = create_enrollment_request(image_id[x])
        result.append(response_validation(create_enroll_resp[1]))
        response_str = create_enroll_resp[1]
        case_id = create_enroll_resp[3]
        add_notes_resp = add_notes_to_enrollment_request(case_id, create_enroll_resp[4])
        result.append(response_validation(add_notes_resp[1]))

    identify_enrollment_index_resp = identify_enrollment_index_visitor_search_with_pic()
    result.append(identify_enrollment_index_resp[0])
    result.append(identify_enrollment_index_resp[2])
    return result, response_str


def start_search_with_pic_metadata_request():
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    region_id = get_user_info_request()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().start_search_endpoint()}"
    data = start_search_with_pic_metadata_data(2)
    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    headers = {"Authorization": f"Token {token}"}
    request_data = {"threshold": data[0], "limit": data[1], "StartDateTime": data[2],
                    "EndDateTime": data[3], "StartAge": data[4], "EndAge": data[5],
                    "IsMale": data[6], "regionId": data[7]}
    response_str = requests.post(url, headers=headers, files=files, data=request_data)
    response_json = response_str.json()
    print(response_json)
    job_id = response_json["jobId"]
    # role_id = response_json["id"]
    return response_str, response_json, job_id


def start_search_with_pic_metadata_data(row_no):
    data = []
    for x in range(3, 11):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().integration_Test_with_metadata_data_sheet_name(), row_no, x))
    return data


def integration_end_to_end_VS_with_only_meta_data_request():
    result = []
    response_str = ""
    row_count = getRowCount(API_Base_Utilities.test_data_excel_path,
                            Read_API_Endpoints().integration_Test_data_sheet_name())
    start_search_resp = start_search_with_only_metadata_request()
    job_id = start_search_resp[2]
    result.append(response_validation(start_search_resp[0]))
    fed_search_resp = get_fed_search_status_request(job_id)
    result.append(response_validation(fed_search_resp))
    create_enroll_resp = create_enrollment_request()
    result.append(response_validation(create_enroll_resp[1]))
    response_str = create_enroll_resp[1]
    return result, response_str


def start_search_with_only_metadata_request():
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    region_id = get_user_info_request()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().start_search_endpoint()}"
    data = start_search_with_only_metadata_data(3)
    headers = {"Authorization": f"Token {token}"}
    request_data = {"threshold": data[0], "limit": data[1], "StartDateTime": data[2],
                    "EndDateTime": data[3], "StartAge": data[4], "EndAge": data[5],
                    "IsMale": data[6], "regionId": data[7]}
    response_str = requests.post(url, headers=headers, data=request_data)
    response_json = response_str.json()
    print(response_json)
    job_id = response_json["jobId"]
    # role_id = response_json["id"]
    return response_str, response_json, job_id


def start_search_with_only_metadata_data(row_no):
    data = []
    for x in range(3, 11):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      Read_API_Endpoints().integration_Test_with_metadata_data_sheet_name(), row_no, x))
    return data


def identify_enrollment_index_visitor_search_with_pic():
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    headers = {"Authorization": f"Token {token}"}
    data = identify_enrollment_data(6)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().identify_enrollment_endpoint()}"
    request_body = {"DetailLevel": data[0], "MaxMatches": data[1], "IncludeMatrics": data[2]}
    files = [
        ('Images', ('img5.png', open(image_path, 'rb'), 'image/png'))
    ]
    response_str = requests.post(url, data=request_body, headers=headers, files=files)
    response_json = response_str.json()
    print(response_json)
    matches = response_json["id"]["matches"]
    print(matches)
    index = []
    for x in range(0, len(matches)):
        print(matches[x]["score"])
        index.append(matches[x]["score"] is not "")
    index_result = False
    if False not in index:
        index_result = True
    return response_str, response_json, index_result

