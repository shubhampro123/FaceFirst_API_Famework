import configparser
from pathlib import Path


class Read_API_Endpoints:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\API_Test_Data\\Api_Endpoints' \
                                        f'\\Endpoints.ini'
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("Read_API_Endpoints config file got an exception", ex)

    def get_login_endpoint(self):
        try:
            ele = self.config.get('LOGIN', 'login_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_report_sheet_path(self):
        try:
            ele = self.config.get('EXCEL_PATH', 'report_excel_sheet_path')
            return ele
        except Exception as ex:
            print(ex)

    def get_test_data_sheet_path(self):
        try:
            ele = self.config.get('EXCEL_PATH', 'test_data_excel_sheet_path')
            return ele
        except Exception as ex:
            print(ex)

    def get_login_test_data_sheet_name(self):
        try:
            ele = self.config.get('SHEET_NAME', 'login_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_test_report_sheet_name(self):
        try:
            ele = self.config.get('SHEET_NAME', 'test_report_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_success_response_code(self):
        try:
            ele = self.config.get('RESPONSE_CODE', 'success_response_code')
            return ele
        except Exception as ex:
            print(ex)