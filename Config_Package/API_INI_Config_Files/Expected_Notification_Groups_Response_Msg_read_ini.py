import configparser
from pathlib import Path


class Read_Expected_Notification_Groups_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            users_response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                                               f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Notification_Groups_Response_Msg.ini'
            self.config.read(users_response_msg_ini_file_path)
        except Exception as ex:
            print("Read_Expected_Notification_Groups_Response_msg config file got an exception", ex)

    def notification_created_success_msg(self,alert_group_id):
        try:
            ele = self.config.get('MESSAGE', 'notification_created_success_msg')
            return ele.format(alert_group_id)
        except Exception as ex:
            print(ex)

    def notification_updated_success_msg(self,alert_group_id):
        try:
            ele = self.config.get('MESSAGE', 'notification_updated_success_msg')
            return ele.format(alert_group_id)
        except Exception as ex:
            print(ex)

    def user_added_to_notification_success_msg(self, user_id, alert_group_id):
        try:
            ele = self.config.get('MESSAGE', 'user_added_to_notification_success_msg')
            return ele.format(user_id, alert_group_id)
        except Exception as ex:
            print(ex)

    def user_added_to_notification_status_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'user_added_to_notification_status_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def user_removed_from_notification_success_msg(self, user_id, alert_group_id):
        try:
            ele = self.config.get('MESSAGE', 'user_removed_from_notification_success_msg')
            return ele.format(user_id, alert_group_id)
        except Exception as ex:
            print(ex)

    def user_removed_from_notification_status_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'user_removed_from_notification_status_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def notification_delete_msg(self, alert_name, alert_group_id):
        try:
            ele = self.config.get('MESSAGE', 'notification_delete_msg')
            return ele.format(alert_name, alert_group_id)
        except Exception as ex:
            print(ex)