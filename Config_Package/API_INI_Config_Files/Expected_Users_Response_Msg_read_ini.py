from pathlib import Path

import configparser


class Read_Expected_users_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            users_Response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                                               f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Users_Response_Msg.ini'
            self.config.read(users_Response_msg_ini_file_path)
        except Exception as ex:
            print("Read_Expected_login_Response_msg config file got an exception", ex)

    def users_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'users_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def user_update_alert_schedule_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'user_update_alert_schedule_msg')
            return ele
        except Exception as ex:
            print(ex)

    def user_create_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'user_create_msg')
            return ele
        except Exception as ex:
            print(ex)

    def edit_user_success_msg(self, value):
        try:
            ele = self.config.get('MESSAGE', 'edit_user_success_msg')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def delete_user_success_msg(self, value):
        try:
            ele = self.config.get('MESSAGE', 'delete_user_success_msg')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def edit_password_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'edit_password_success_msg')
            return ele
        except Exception as ex:
            print(ex)

