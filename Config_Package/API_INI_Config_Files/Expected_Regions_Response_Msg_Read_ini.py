import configparser
from pathlib import Path


class Read_Expected_Region_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            Read_Expected_Regions_Response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Regions_Response_Msg.ini'
            self.config.read(Read_Expected_Regions_Response_msg_ini_file_path)
        except Exception as ex:
            print("Read_Expected_Regions_Response_msg config file got an exception", ex)

    def update_success_msg(self, region_id):
        try:
            ele = self.config.get('MESSAGE', 'update_success_msg')
            return ele.format(region_id)
        except Exception as ex:
            print(ex)

    def delete_success_msg(self, region_id):
        try:
            ele = self.config.get('MESSAGE', 'delete_success_msg')
            return ele.format(region_id)
        except Exception as ex:
            print(ex)

    def create_success_msg(self, region_id):
        try:
            ele = self.config.get('MESSAGE', 'create_success_msg')
            return ele.format(region_id)
        except Exception as ex:
            print(ex)
