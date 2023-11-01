import json
from pathlib import Path

import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, API_Base_Utilities, login_token

from All_API_Methods_Package.Enrollment_Group_Module_API.Enrollment_Group_API_Methods import \
    create_enrollment_group_test_data
from All_API_Methods_Package.Identify_and_Enroll_Module_API.Identify_Enroll_Module_API import get_C_group_Id, \
    get_profile_id, create_enrollment_data, create_enrollment_request
from All_API_Methods_Package.Notification_groups_Module_API.Notification_Groups_Methods import get_user_info, \
    create_notification_groups_without_users_enrollment_group_zone_test_data, add_user_to_alert_group_test_data
from All_API_Methods_Package.Region_Module_API.Region_methods import region_module_test_module, \
    get_request_region_by_descendants
from All_API_Methods_Package.User_Roles_Module_API.User_Role_Methods import create_user_role_request, \
    user_role_test_data, random_number
from All_API_Methods_Package.Users_Module_API.Users_API_Methods import users_test_data, select_region
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
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_integration_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def second_integration_end_to_end(self):
        job_id = start_search_request()[2]
        get_fed_search_status_request(job_id)
        create_enrollment_request()


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
                 "region_id": region_id[2], "username": f"{data[24]}{random_number()}", "password": data[25]}
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
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    region_id = get_user_info_request()
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().start_search_endpoint()}"
    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
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
    print(response_str)
    response_json = response_str.json()
    matches = response_json["matched"]
    print(matches)



