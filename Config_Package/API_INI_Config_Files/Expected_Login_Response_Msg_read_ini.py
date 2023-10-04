import configparser
from pathlib import Path


class Read_Expected_login_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            Read_Expected_login_Response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Login_Response_Msg.ini'
            self.config.read(Read_Expected_login_Response_msg_ini_file_path)
        except Exception as ex:
            print("Read_Expected_login_Response_msg config file got an exception", ex)

    def login_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'login_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def login_invalid_username(self):
        try:
            ele = self.config.get('MESSAGE', 'login_invalid_username')
            return ele
        except Exception as ex:
            print(ex)

    def login_invalid_password(self):
        try:
            ele = self.config.get('MESSAGE', 'login_invalid_password')
            return ele
        except Exception as ex:
            print(ex)

    def login_blank_username_password(self):
        try:
            ele = self.config.get('MESSAGE', 'login_blank_username_password')
            return ele
        except Exception as ex:
            print(ex)

    def users_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'users_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def query_login_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'query_login_msg')
            return ele
        except Exception as ex:
            print(ex)

    def logout_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'logout_success_msg')
            return ele
        except Exception as ex:
            print(ex)