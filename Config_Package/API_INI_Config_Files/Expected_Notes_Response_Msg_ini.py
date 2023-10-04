import configparser
from pathlib import Path


class Read_notes_Response_msg:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            read_notes_response_msg_ini_file_path = f'{Path(__file__).parent.parent.parent}' \
                f'\\API_Test_Data\\Response_Exp_Msg\\Expected_Notes_Response_Msg.ini'
            self.config.read(read_notes_response_msg_ini_file_path)
        except Exception as ex:
            print("Read_notes_Response_msg config file got an exception", ex)

    def create_notes_success_msg(self, note_id):
        try:
            ele = self.config.get('MESSAGE', 'create_notes_success_msg')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def update_notes_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'update_notes_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def delete_notes_success_msg(self, note_id):
        try:
            ele = self.config.get('MESSAGE', 'delete_notes_success_msg')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def clear_notes_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'clear_notes_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def add_image_to_notes_success_msg(self):
        try:
            ele = self.config.get('MESSAGE', 'add_image_to_notes_success_msg')
            return ele
        except Exception as ex:
            print(ex)

    def delete_image_to_notes_success_msg(self, note_id):
        try:
            ele = self.config.get('MESSAGE', 'delete_image_to_notes_success_msg')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)