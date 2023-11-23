from pathlib import Path

import requests

from API_Utilities.Api_Base import API_Base_Utilities, time_entry, response_validation, excel_result, login_token
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class Detect_Face_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().detect_face_result_sheet_name()

    def verify_post_detect_face_with_valid_data(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = create_detect_face_request(self.row)

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
            self.log.info(f"test_Detect_Faces_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    ################################### Generic method #################################


def create_detect_face_request(row_no):
    token = login_token()
    image_path = f"{Path(__file__).parent.parent.parent}\\API_Test_Data\\image.png"
    data = detect_face_test_data(row_no)
    detect_faces = f"{data[0]}"
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().detect_face_endpoint()}"
    headers = {"Authorization": f"Token {token}"}
    request_data = {"MaxFaces": data[0], "DetectionThreshold": data[1], "MinEyeDistance": data[2],
                    "IncludeEyeCoordinates": data[3]}

    files = [
        ('Images', ('image.png', open(image_path, 'rb'), 'image/png'))
    ]
    response_str = requests.post(url, headers=headers, data=request_data, files=files, verify=False)
    response_json = response_str.json()
    # role_id = response_json["id"]
    return response_str, response_json, detect_faces


def detect_face_test_data(row_no):
    data = []
    for x in range(3, 30):
        data.append(XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                      API_Base_Utilities.detect_face_test_data_sheet_name, row_no, x))
    return data

    # files = [
    #     ('Images', ('image.png', open(image_png, 'rb'), 'image/png'))
    # ]