import requests

from API_Utilities.Api_Base import time_entry, response_validation, excel_result, login_token, API_Base_Utilities
from Config_Package.API_INI_Config_Files.Api_Endpoints_Read_ini import Read_API_Endpoints


class Zones_API_Methods:

    def __init__(self, logger):
        self.log = logger
        self.row = None
        self.r_body = None
        self.response = None
        self.exp_msg = None
        self.act_msg = None
        self.json_response = None
        self.sheet_name = Read_API_Endpoints().zones_result_sheet_name()

    def verify_get_all_zones(self):
        result = []
        try:
            self.row = 2
            time_entry(self.row, "start_time", self.sheet_name)
            response_list = get_all_zones()
            self.response = response_list[0]
            self.json_response = response_list[1]
            print(response_list)
            for x in range(len(self.json_response["zoneInfo"]["zones"])):
                result.append(self.json_response["zoneInfo"]["zones"][x]["zoneId"] != "")

            if response_validation(self.response) and False not in result:
                excel_result(self.row,"Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_01", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_01", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Zones_Test_01_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False

    def verify_get_zone_by_id(self):
        result = []
        try:
            self.row = 3
            time_entry(self.row, "start_time", self.sheet_name)
            ex_zone_id = get_all_zones()[1]["zoneInfo"]["zones"][0]["zoneId"]
            response_list = get_single_zone_by_id(ex_zone_id)
            self.response = response_list[0]
            self.json_response = response_list[1]
            ac_zones_id = self.json_response["zoneInfo"]["zones"][0]["zoneId"]
            print(response_list)
            if response_validation(self.response) and ex_zone_id == ac_zones_id:
                excel_result(self.row,"Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             True, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(True)
            else:
                self.log.info(f"actual_status_code = {self.response.status_code}, expected_status_code = 200")
                self.log.info(f"actual_message = {self.act_msg}, expected_message = {self.exp_msg}")
                excel_result(self.row,"Test_02", self.r_body, self.json_response, self.response.status_code, self.act_msg,
                             False, self.sheet_name)
                time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
                result.append(False)
            if False in result:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            excel_result(self.row,"Test_02", self.r_body, self.json_response, self.response.status_code, self.exp_msg,
                         False, self.sheet_name)
            self.log.info(f"test_Zones_Test_02_Exception:  {ex}")
            time_entry(self.row, "end_time", self.sheet_name), time_entry(self.row, "total_time", self.sheet_name)
            return False


def get_all_zones():
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_all_zones_endpoint()}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json


def get_single_zone_by_id(zone_id):
    token = login_token()
    headers = {"Token": token}
    url = f"{API_Base_Utilities.Base_URL}{Read_API_Endpoints().get_zone_by_id_endpoint(zone_id)}"
    response_str = requests.get(url, headers=headers)
    response_json = response_str.json()
    return response_str, response_json