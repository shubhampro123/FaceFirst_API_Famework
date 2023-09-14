from datetime import datetime
from pathlib import Path
import requests
from API_Utilities.Api_Base import API_Base_Utilities
from Config_Package.API_Endpoints_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.API_Endpoints_INI_Config_Files.Expected_Login_Response_Msg_read_ini import \
    Read_Expected_login_Response_msg
from Config_Package.Excel_Config_Files import XLUtils


class Login_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None

    def login_with_valid_username_and_password(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time")
            response_list = login_request(self.row)
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.r_body = response_list[3]
            self.act_msg = self.json_response["result"]["message"]
            self.exp_msg = Read_Expected_login_Response_msg().login_success_msg()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.act_msg, True)
                time_entry(self.row, "end_time"), time_entry(self.row, "total_time"), result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.act_msg, False)
                time_entry(self.row, "end_time"), time_entry(self.row, "total_time"), result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.act_msg, False)
            self.log.info(f"test_Login_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time"), time_entry(self.row, "total_time")
            return False

    def login_with_invalid_username_and_password(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time")
            response_list = login_request(self.row)
            self.response = response_list[1]
            self.json_response = response_list[2]
            self.r_body = response_list[3]
            self.act_msg = self.json_response["result"]["message"]
            self.exp_msg = Read_Expected_login_Response_msg().login_invalid_password()
            if response_validation(self.response) and self.act_msg == self.exp_msg:
                excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.act_msg, True)
                time_entry(self.row, "end_time"), time_entry(self.row, "total_time"), result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.act_msg, False)
                time_entry(self.row, "end_time"), time_entry(self.row, "total_time"), result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(self.row, self.r_body, self.json_response, self.response.status_code, self.exp_msg, False)
            self.log.info(f"test_Login_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time"), time_entry(self.row, "total_time")
            return False

            ################################### Generic method #################################


# API all Excel file path
report_excel_path = f"{Path(__file__).parent.parent.parent}{Read_API_Endpoints().get_report_sheet_path()}"
test_data_excel_path = f"{Path(__file__).parent.parent.parent}{Read_API_Endpoints().get_test_data_sheet_path()}"

# Sheet name
login_test_data_sheet_name = Read_API_Endpoints().get_login_test_data_sheet_name()
report_sheet_name = Read_API_Endpoints().get_test_report_sheet_name()


def login_request(row_no):
    data = login_test_data(row_no)
    username = data[0]
    password = data[1]
    lat = data[2]
    lon = data[3]
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_login_endpoint()}"
    form_data = {"username": username, "password": password, "lat": lat, "lon": lon}
    response_str = requests.post(url, form_data)
    response_json = response_str.json()
    return url, response_str, response_json, form_data


# Get all data form Excel
def login_test_data(row_no):
    username = XLUtils.read_data(test_data_excel_path, login_test_data_sheet_name, row_no, 3)
    password = XLUtils.read_data(test_data_excel_path, login_test_data_sheet_name, row_no, 4)
    lat = XLUtils.read_data(test_data_excel_path, login_test_data_sheet_name, row_no, 5)
    lon = XLUtils.read_data(test_data_excel_path, login_test_data_sheet_name, row_no, 6)
    return username, password, lat, lon


# write all data in Excel
def excel_result(row_no, body, json_res, status_code, validation, result):
    actual_result = f"Response Status Code : {status_code} & Message : {validation}"
    XLUtils.writeData(report_excel_path, report_sheet_name, row_no, 4, body)
    XLUtils.writeData(report_excel_path, report_sheet_name, row_no, 5, json_res)
    XLUtils.writeData(report_excel_path, report_sheet_name, row_no, 8, actual_result)
    if result:
        XLUtils.result_pass(report_excel_path, report_sheet_name, row_no, 7)
    else:
        XLUtils.result_fail(report_excel_path, report_sheet_name, row_no, 7)


# test case execution time count method
def time_entry(row_no, time):
    global start, end
    if time == "start_time":
        start = XLUtils.getCurrentTime()
        XLUtils.writeData(report_excel_path, report_sheet_name, row_no, 9, start)
    if time == "end_time":
        end = XLUtils.getCurrentTime()
        XLUtils.writeData(report_excel_path, report_sheet_name, row_no, 10, end)
    if time == "total_time":
        time_format = "%H:%M:%S"
        datetime1 = datetime.strptime(start, time_format)
        datetime2 = datetime.strptime(end, time_format)
        time_difference = datetime2 - datetime1
        seconds_difference = time_difference.total_seconds()
        XLUtils.writeData(report_excel_path, report_sheet_name, row_no, 11, seconds_difference)


def response_validation(response_data):
    return int(response_data.status_code) == int(Read_API_Endpoints().get_success_response_code())
