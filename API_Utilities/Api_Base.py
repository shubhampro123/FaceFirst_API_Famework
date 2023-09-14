import os
from datetime import datetime
import logging
from pathlib import Path


class API_Base_Utilities:

    Base_URL = "https://ff-india-qa11.eastus2.cloudapp.azure.com"

    @staticmethod
    def logger_object():
        try:
            print("pass")
            log_folder = f"{Path(__file__).parent.parent}\\API_Logs"
            files_list = os.listdir(log_folder)
            list_size = len(files_list)
            print("file List : ", files_list, " file count: ", list_size)
            i = 0
            base_path = Path(log_folder)
            files_in_base_path = base_path.iterdir()
            print(type(files_in_base_path))
            print(files_in_base_path)
            for file in files_list[:-3]:
                for file_name in files_in_base_path:
                    if file_name.name == file:
                        os.remove(file_name)
            now = datetime.now()
            print("now =", now)
            dt = now.strftime("%d_%m_%Y_%H_%M_%S")
            file_name = f"{Path(__file__).parent.parent}\\API_Logs\\API_logs_{dt}.log"
            print("Log_file_name: ", file_name)
            formatter = logging.Formatter("%(asctime)s : %(name)-12s : %(levelname)-8s : %(message)s",
                                          datefmt='%d/%m/%Y %r')
            handler = logging.FileHandler(filename=file_name)
            handler.setFormatter(formatter)
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            logger.addHandler(handler)
            return logger
        except Exception as ex:
            print(ex)
