import configparser
from pathlib import Path


class Read_Expected_Enrollment_Group_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            Read_Expected_Enrollment_Group_Response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Enrollment_Group_Response_Msg.ini'
            self.config.read(Read_Expected_Enrollment_Group_Response_msg_ini_file_path)
        except Exception as ex:
            print("Read_Expected_Enrollment_Group_Response_msg config file got an exception", ex)

    def create_enrollment_group_msg(self, value):
        try:
            ele = self.config.get('MESSAGE', 'create_enrollment_group_msg')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def update_enrollment_group_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'update_enrollment_group_msg')
            return ele
        except Exception as ex:
            print(ex)

    def delete_enrollment_group_msg(self, value):
        try:
            ele = self.config.get('MESSAGE', 'delete_enrollment_group_msg')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def create_enrollment_group_with_addCaseGroupZone_msg(self, value, value1):
        try:
            ele = self.config.get('MESSAGE', 'create_enrollment_group_with_addCaseGroupZone_msg')
            return ele.format(value, value1)
        except Exception as ex:
            print(ex)

    def removeCaseGroupZone_msg(self, value, value1):
        try:
            ele = self.config.get('MESSAGE', 'removeCaseGroupZone_msg')
            return ele.format(value, value1)
        except Exception as ex:
            print(ex)

    def addCaseGroupCase_msg(self, value, value1):
        try:
            ele = self.config.get('MESSAGE', 'addCaseGroupCase_msg')
            return ele.format(value, value1)
        except Exception as ex:
            print(ex)

    def removeCaseGroupCase_msg(self, value, value1):
        try:
            ele = self.config.get('MESSAGE', 'removeCaseGroupCase_msg')
            return ele.format(value, value1)
        except Exception as ex:
            print(ex)

    def addAlertGroupCase_msg(self, value):
        try:
            ele = self.config.get('MESSAGE', 'addAlertGroupCase_msg')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def removeAlertGroupCase_msg(self, value):
        try:
            ele = self.config.get('MESSAGE', 'removeAlertGroupCase_msg')
            return ele.format(value)
        except Exception as ex:
            print(ex)

