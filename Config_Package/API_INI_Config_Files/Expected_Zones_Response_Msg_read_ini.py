import configparser
from pathlib import Path


class Read_Expected_Zones_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                                               f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Zones_Response_Msg.ini'
            self.config.read(response_msg_ini_file_path)
        except Exception as ex:
            print("Read_Zones_Response_msg config file got an exception", ex)

    def get_zones_validation(self):
        try:
            ele = self.config.get('MESSAGE', 'get_zones_validation')
            return ele
        except Exception as ex:
            print(ex)