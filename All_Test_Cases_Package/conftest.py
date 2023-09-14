import os

from selenium.webdriver.common.by import By

from Config_Package.INI_Config_Files.Users_Read_INI import Read_Users_Components
from Other_Utilities.Read_Excel import Read_excel
import time

from datetime import date
from datetime import datetime

import pytest as pytest
# from _pytest.mark import param

# from All_POM_Package.LoginPage import Login
# from utilities import XLUtils
from pathlib import Path
resultPath = f"{Path(__file__).parent.parent}\\Test_Data\\Data_From_Excel\\Test_Cases.xlsx"

import logging
from logging import Logger
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



"""set Explicit wait function to be used by all the web elements where ever it is needed"""


# def Explicit_wait(seconds, element):
#     wait = WebDriverWait(driver, seconds)
#     ele = wait.until(expected_conditions.element_to_be_clickable(element))


class Base_Class:

    try:
        options = webdriver.ChromeOptions()
        # options.headless = True
        options.add_experimental_option("detach", True)
        d = webdriver.Chrome(options=options)
        # d =webdriver.Chrome()
        one_second = 1
        two_second = 2
        three_second = 3
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)

    @staticmethod
    def logger_object():
        try:
            log_folder = f"{Path(__file__).parent.parent}\\Application_Logs"
            files_list = os.listdir(log_folder)
            list_size = len(files_list)
            print("file List : ", files_list, " file count: ", list_size)
            i = 0
            base_path = Path(log_folder)
            files_in_base_path = base_path.iterdir()
            print(type(files_in_base_path))
            print(files_in_base_path)
            # for file in files_list[-3]:
            #     for file_name in files_in_base_path:
            #         if file_name.name == file:
            #             os.remove(file_name)

            now = datetime.now()
            print("now =", now)
            dt = now.strftime("%d_%m_%Y_%H_%M_%S")
            file_name = f"{Path(__file__).parent.parent}\\Application_Logs\\Application_logs_{dt}.log"
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

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Users_Components().logout_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            logout_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False
