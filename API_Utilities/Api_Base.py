import os
from datetime import datetime
import logging
from pathlib import Path

import requests
import self

from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints
from Config_Package.Excel_Config_Files import XLUtils


class API_Base_Utilities:
    Base_URL = "https://ff-india-qa10.eastus2.cloudapp.azure.com/"

    # API all Excel file path
    report_excel_path = f"{Path(__file__).parent.parent.parent}{Read_API_Endpoints().get_report_sheet_path()}"
    test_data_excel_path = f"{Path(__file__).parent.parent.parent}{Read_API_Endpoints().get_test_data_sheet_path()}"

    # Sheet name
    login_test_data_sheet_name = Read_API_Endpoints().get_login_test_data_sheet_name()
    users_test_data_sheet_name = Read_API_Endpoints().users_test_data_sheet_name()
    notification_groups_test_data_sheet_name = Read_API_Endpoints().notification_groups_test_data_sheet_name()
    zones_test_data_sheet_name = Read_API_Endpoints().zones_test_data_sheet_name()
    account_test_data_sheet_name = Read_API_Endpoints().account_test_data_sheet_name()
    notes_test_data_sheet_name = Read_API_Endpoints().notes_test_data_sheet_name()
    detect_face_test_data_sheet_name = Read_API_Endpoints().detect_face_test_data_sheet_name()
    tags_test_data_sheet_name = Read_API_Endpoints().tags_test_data_sheet_name()
    user_role_test_data_sheet_name = Read_API_Endpoints().detect_face_test_data_sheet_name()
    region_test_data_sheet_name = Read_API_Endpoints().region_data_sheet_name()
    visitor_search_test_data_sheet_name = Read_API_Endpoints().visitor_search_test_data_sheet_name()
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = cls.logger_object()
        return cls.logger

    @staticmethod
    def logger_object():
        try:
            print("pass")
            log_folder = f"{Path(__file__).parent.parent}\\API_Logs"
            files_list = os.listdir(log_folder)
            list_size = len(files_list)
            print("file List : ", files_list, " file count: ", list_size)
            i = 0
            base_path = Path(log_folder)
            files_in_base_path = base_path.iterdir()
            print(type(files_in_base_path))
            print(files_in_base_path)
            for file in files_list[:-3]:
                for file_name in files_in_base_path:
                    if file_name.name == file:
                        os.remove(file_name)
            now = datetime.now()
            print("now =", now)
            dt = now.strftime("%d_%m_%Y_%H_%M_%S")
            file_name = f"{Path(__file__).parent.parent}\\API_Logs\\API_logs_{dt}.log"
            print("Log_file_name: ", file_name)
            formatter = logging.Formatter("%(asctime)s : %(name)-12s : %(levelname)-8s : %(message)s",
                                          datefmt='%d/%m/%Y %r')
            handler = logging.FileHandler(filename=file_name)
            handler.setFormatter(formatter)
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            logger.addHandler(handler)
            return logger
        except Exception as ex:
            print(ex)


# write all data in Excel

def excel_result(row_no, test_case_id, body, json_res, status_code, validation, result, sheet_name):
    actual_result = f"Response Status Code : {status_code} & Message : {validation}"
    XLUtils.writeData(API_Base_Utilities.report_excel_path, sheet_name, row_no, 2, test_case_id)
    XLUtils.writeData(API_Base_Utilities.report_excel_path, sheet_name, row_no, 4, body)
    XLUtils.writeData(API_Base_Utilities.report_excel_path, sheet_name, row_no, 5,
                      json_res)
    XLUtils.writeData(API_Base_Utilities.report_excel_path, sheet_name, row_no, 8,
                      actual_result)
    if result:
        XLUtils.result_pass(API_Base_Utilities.report_excel_path, sheet_name, row_no, 7)
    else:
        XLUtils.result_fail(API_Base_Utilities.report_excel_path, sheet_name, row_no, 7)


# test case execution time count method
def time_entry(row_no, time, sheet_name):
    global start, end
    if time == "start_time":
        start = XLUtils.getCurrentTime()
        XLUtils.writeData(API_Base_Utilities.report_excel_path, sheet_name, row_no, 9, start)
    if time == "end_time":
        end = XLUtils.getCurrentTime()
        XLUtils.writeData(API_Base_Utilities.report_excel_path, sheet_name, row_no, 10, end)
    if time == "total_time":
        time_format = "%H:%M:%S"
        datetime1 = datetime.strptime(start, time_format)
        datetime2 = datetime.strptime(end, time_format)
        time_difference = datetime2 - datetime1
        seconds_difference = time_difference.total_seconds()
        XLUtils.writeData(API_Base_Utilities.report_excel_path, sheet_name, row_no, 11,
                          seconds_difference)


def login_token():
    row_no = 2
    username = XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                 API_Base_Utilities.login_test_data_sheet_name, row_no, 3)
    password = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                                 row_no, 4)
    lat = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                            row_no, 5)
    lon = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                            row_no, 6)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_login_endpoint()}"
    form_data = {"username": username, "password": password, "lat": lat, "lon": lon}
    response_str = requests.post(url, form_data)
    response_json = response_str.json()
    token = response_json["result"]["token"]
    return token


def login_Cookie():
    row_no = 2
    username = XLUtils.read_data(API_Base_Utilities.test_data_excel_path,
                                 API_Base_Utilities.login_test_data_sheet_name, row_no, 3)
    password = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                                 row_no, 4)
    lat = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                            row_no, 5)
    lon = XLUtils.read_data(API_Base_Utilities.test_data_excel_path, API_Base_Utilities.login_test_data_sheet_name,
                            row_no, 6)
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_login_endpoint()}"
    form_data = {"username": username, "password": password, "lat": lat, "lon": lon}
    response_str = requests.post(url, form_data)
    response_json = response_str.json()
    cookies = response_json["result"]["cookies"]
    return cookies


def response_validation(response_data):
    return int(response_data.status_code) == int(Read_API_Endpoints().get_success_response_code())


def invalid_response_validation(response_data):
    return int(response_data.status_code) == int(Read_API_Endpoints().internal_server_error())
