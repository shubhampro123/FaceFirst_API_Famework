import configparser
from pathlib import Path


class Read_Expected_login_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\API_Test_Data\\Response_Exp_Msg' \
                                        f'\\Expected_Login_Response_Msg.ini'
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("Read_Expected_login_Response_msg config file got an exception", ex)

    def login_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'login_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def login_invalid_password(self):
        try:
            ele = self.config.get('MESSAGE', 'login_invalid_password')
            return ele
        except Exception as ex:
            print(ex)