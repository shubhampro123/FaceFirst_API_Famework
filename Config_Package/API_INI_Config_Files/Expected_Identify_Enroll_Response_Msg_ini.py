import configparser
from pathlib import Path


class Read_identify_enroll_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            Read_identify_enroll_Response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Identify_Enroll_Response_Msg.ini'
            self.config.read(Read_identify_enroll_Response_msg_ini_file_path)
        except Exception as ex:
            print("Read_identify_enroll_Response_msg config file got an exception", ex)

    def create_enrollment_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'create_enrollment_success_msg')
            return ele
        except Exception as ex:
            print(ex)
