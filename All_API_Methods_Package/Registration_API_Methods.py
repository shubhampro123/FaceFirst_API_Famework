import random
from datetime import datetime
from pathlib import Path
import requests

from Config_Package.Excel_Config_Files import XLUtils

excel_path = f"{Path(__file__).parent.parent.parent}\\Trial_API_Framework_07_09_23\\Reports\\API_Excel_Report\\API_excel_report.xlsx"
excel_data = f"{Path(__file__).parent.parent.parent}\\Trial_API_Framework_07_09_23\\Test_Data\\Data_From_Excel\\API_excel_data.xlsx"
sheet_name = "Test_Results"
data_sheet = "test_data"
register_email = []


class Registration_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row_count = 0

    def Crate_new_user_and_validate_response(self):
        global x, url, body, json_response, response, message, row
        result = []
        try:
            row = 2
            time_entry(row, "start_time")
            name = XLUtils.read_data(excel_data, data_sheet, row, 2)
            password = XLUtils.read_data(excel_data, data_sheet, row, 3)
            exp_status = XLUtils.read_data(excel_data, data_sheet, row, 4)
            response_list = register_new_user(name, password)
            body = response_list[2]
            response = response_list[1]
            json_response = response_list[0]
            url = response_list[3]
            message = json_response["message"]
            token = json_response["data"]["Token"]
            response_email = json_response["data"]["Email"]
            register_email.append(response_email)
            if response_list[1].status_code == exp_status and message == "success":
                excel_result(row, body, json_response, response.status_code, message, True)
                time_entry(row, "end_time")
                time_entry(row, "total_time")
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {response.status_code}, expected_status_code = 200")
                excel_result(row, body, json_response, response.status_code, message, False)
                time_entry(row, "end_time")
                time_entry(row, "total_time")
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(row, body, json_response, response.status_code, message, False)
            self.log.info(f"Login_API_validate_200_status_code_failed:  {ex}")
            time_entry(row, "end_time")
            return False

    def Crate_new_user_with_register_email_and_validate_response(self):
        global x, url, body, json_response, response, row
        result = []
        try:
            row = 3
            time_entry(row, "start_time")
            name = XLUtils.read_data(excel_data, data_sheet, row, 2)
            password = XLUtils.read_data(excel_data, data_sheet, row, 3)
            exp_status = XLUtils.read_data(excel_data, data_sheet, row, 4)
            response_list = register_new_user_with_register_email(name, password, register_email[0])
            body = response_list[2]
            response = response_list[1]
            json_response = response_list[0]
            url = response_list[3]
            act_message = json_response["message"]
            exp_message = "The email address you have entered is already registered"
            if response.status_code == exp_status and act_message == exp_message:
                excel_result(row, body, json_response, response.status_code, act_message, True)
                time_entry(row, "end_time")
                time_entry(row, "total_time")
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {act_message}, expected_message = {exp_message}")
                excel_result(row, body, json_response, response.status_code, act_message, False)
                time_entry(row, "end_time")
                time_entry(row, "total_time")
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(row, body, json_response, response.status_code, message, False)
            self.log.info(f"Crate_new_user_with_register_email_and_validate_response_failed:  {ex}")
            time_entry(row, "end_time")
            time_entry(row, "total_time")
            return False

    def Crate_new_user_with_blank_email_and_validate_response(self):
        global url, body, json_response, response, message
        result = []
        row = 4
        try:
            time_entry(row, "start_time")
            name = XLUtils.read_data(excel_data, data_sheet, row, 2)
            password = XLUtils.read_data(excel_data, data_sheet, row, 3)
            exp_status = XLUtils.read_data(excel_data, data_sheet, row, 4)
            response_list = register_new_user_blank_email(name, password)
            body = response_list[2]
            response = response_list[1]
            json_response = response_list[0]
            url = response_list[3]
            act_message1 = json_response["Message"]
            exp_message1 = "The request is invalid."
            act_message2 = json_response["ModelState"]["User.email"][0]
            exp_message2 = "field is required"
            message = act_message1 + " " + act_message2
            if response.status_code == exp_status and act_message1 == exp_message1 and act_message2 == exp_message2:
                excel_result(row, body, json_response, response.status_code, message, True)
                time_entry(row, "end_time")
                time_entry(row, "total_time")
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {act_message1}, expected_message = {exp_message1}")
                self.log.info(f"actual_message = {act_message2}, expected_message = {exp_message2}")
                excel_result(row, body, json_response, response.status_code, message, False)
                time_entry(row, "end_time")
                time_entry(row, "total_time")
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            excel_result(row, body, json_response, response.status_code, message, False)
            self.log.info(f"Crate_new_user_with_register_email_and_validate_response_failed:  {ex}")
            time_entry(row, "end_time")
            time_entry(row, "total_time")
            return False

    ############################################## reusable methods ##################################################


def register_new_user(name, password):
    random_number = 0
    for _ in range(5):
        random_number = random.randint(1000, 9999)
    email = f"name{random_number}@gmail.com"
    url = "http://restapi.adequateshop.com/api/authaccount/registration"
    data = {
        "name": name,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=data)
    response_json = response.json()
    return response_json, response, data, url


def register_new_user_blank_email(name, password):
    url = "http://restapi.adequateshop.com/api/authaccount/registration"
    data = {
        "name": name,
        "email": "",
        "password": password
    }
    response = requests.post(url, json=data)
    response_json = response.json()
    return response_json, response, data, url


def register_new_user_with_register_email(name, password, email):
    url = "http://restapi.adequateshop.com/api/authaccount/registration"
    data = {
        "name": name,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=data)
    response_json = response.json()
    return response_json, response, data, url


def excel_result(row, body, json_response, status_code, validation, result):
    actual_result = f"Response Status Code : {status_code} & Message : {validation}"
    XLUtils.writeData(excel_path, sheet_name, row, 4, body)
    XLUtils.writeData(excel_path, sheet_name, row, 5, json_response)
    XLUtils.writeData(excel_path, sheet_name, row, 8, actual_result)
    if result:
        XLUtils.result_pass(excel_path, sheet_name, row, 7)
    else:
        XLUtils.result_fail(excel_path, sheet_name, row, 7)


def excel_test_data(row):
    name = XLUtils.read_data(excel_data, sheet_name, row, 1)
    password = XLUtils.read_data(excel_data, sheet_name, row, 2)
    return name, password


def row_count_data(count):
    count = +1
    return count


def time_entry(row, time):
    global start, end
    if time == "start_time":
        start = XLUtils.getCurrentTime()
        XLUtils.writeData(excel_path, sheet_name, row, 9, start)
    if time == "end_time":
        end = XLUtils.getCurrentTime()
        XLUtils.writeData(excel_path, sheet_name, row, 10, end)
    if time == "total_time":
        time_format = "%H:%M:%S"
        datetime1 = datetime.strptime(start, time_format)
        datetime2 = datetime.strptime(end, time_format)
        time_difference = datetime2 - datetime1
        seconds_difference = time_difference.total_seconds()
        XLUtils.writeData(excel_path, sheet_name, row, 11, seconds_difference)
