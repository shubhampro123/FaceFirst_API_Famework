import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Visitors_read_INI import Read_Visitors_Components


class Visitors_Search_Filter_Combination_POM:
    def __init__(self, logger):
        self.d = Base_Class.d
        self.log = logger
        self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_filter_login_failed.png")
            self.log.info(f"login_before:  {ex}")
            return False

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()). \
                is_displayed():
            self.login_before()
            time.sleep(Base_Class.one_second)

    def search_visitors_with_no_filter_criteria(self):
        try:
            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            drop_down = self.d.find_element(By.XPATH, Read_Visitors_Components().search_drop_down_search_btn_by_xpath())
            self.click_on_search_btn_in_drop_down()
            if drop_down.is_enabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_no_filter_criteria_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_no_filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_no_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_hierarchy_filter_criteria(self):
        try:
            self.login()
            time.sleep(Base_Class.one_second)
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            self.zone_selection()
            self.click_on_search_btn_in_drop_down()

            if self.validate_zone_result():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_hierarchy_"
                                       f"filter_criteria_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_hierarchy_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_gender_filter_criteria(self):
        try:
            self.login()
            time.sleep(Base_Class.one_second)
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)
            self.click_on_search_btn_in_drop_down()

            if self.validate_gender_search(gender_data):
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\search_visitors_with_gender_filter_criteria_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_gender_filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_gender_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_gender_and_hierarchy_filter_criteria(self):
        result = []
        try:
            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            self.zone_selection()
            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)
            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_gender_search(gender_data))
            result.append(self.validate_zone_result())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_gender_and_hierarchy_"
                                       f"filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_gender_and_hierarchy_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_gender_and_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_age_range_filter_criteria(self):
        try:
            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.click_on_search_btn_in_drop_down()

            if self.validate_age_search(start_age, end_age):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_"
                                       f"filter_criteria_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_age_range_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_age_range_and_hierarchy_filter_criteria(self):
        result = []
        try:
            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.zone_selection()

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_age_search(start_age, end_age))
            result.append(self.validate_zone_result())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_and_"
                                       f"hierarchy_filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_and_hierarchy_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_age_range_and_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_age_range_and_gender_filter_criteria(self):
        result = []
        try:
            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_age_search(start_age, end_age))
            result.append(self.validate_gender_search(gender_data))
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_and"
                                       f"_gender_filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_and_gender_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_age_range_and_gender_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_age_range_gender_and_hierarchy_filter_criteria(self):
        result = []
        try:
            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)
            self.zone_selection()

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_age_search(start_age, end_age))
            result.append(self.validate_gender_search(gender_data))
            result.append(self.validate_zone_result())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_gender_"
                                       f"and_hierarchy_filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_age_range_gender_and_hierarchy_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_age_range_gender_and_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_range_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()

            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_"
                                       f"filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_filter_"
                                   f"criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_range_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_range_and_hierarchy_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.zone_selection()

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_zone_result())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_and_"
                                       f"hierarchy_filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_and_hierarchy"
                                   f"_filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_range_and_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_range_and_gender_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()

            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_gender_search(gender_data))
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_and_gender_"
                                       f"filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_and_gender_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_range_and_gender_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_range_gender_and_hierarchy_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()

            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)
            self.zone_selection()

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_gender_search(gender_data))
            result.append(self.validate_zone_result())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_gender_and_"
                                       f"hierarchy_filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_range_gender_and_"
                                   f"hierarchy_filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_range_gender_and_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_and_age_range_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()

            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_search(start_age, end_age))
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_and_age_range_"
                                       f"filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_and_age_range_filter_"
                                   f"criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_and_age_range_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_age_range_and_hierarchy_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()

            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.zone_selection()

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_search(start_age, end_age))
            result.append(self.validate_zone_result())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_age_range_and_"
                                       f"hierarchy_filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_age_range_and_hierarchy_"
                                   f"filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_age_range_and_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_age_range_and_gender_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()

            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_search(start_age, end_age))
            result.append(self.validate_gender_search(gender_data))
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_age_range_and_gender"
                                       f"_filter_criteria_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_age_range_and_gender"
                                   f"_filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_age_range_and_gender_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def search_visitors_with_datetime_age_range_gender_and_hierarchy_filter_criteria(self):
        result = []
        try:
            date = int(Read_Visitors_Components().get_start_date())
            month = str(Read_Visitors_Components().get_start_month())
            year = int(Read_Visitors_Components().get_start_year())
            hour = str(Read_Visitors_Components().get_start_hour())
            minute = int(Read_Visitors_Components().get_start_minuet())
            period = str(Read_Visitors_Components().get_start_am_pm_period())

            e_month = str(Read_Visitors_Components().get_end_month())
            e_date = int(Read_Visitors_Components().get_end_date())
            e_year = int(Read_Visitors_Components().get_end_year())
            e_hour = str(Read_Visitors_Components().get_end_hour())
            e_minute = int(Read_Visitors_Components().get_end_minuet())
            e_period = str(Read_Visitors_Components().get_end_am_pm_period())

            self.login()
            self.click_on_visitors_link()
            self.click_on_search_drop_down()

            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            start_age = Read_Visitors_Components().start_age_data_input()
            end_age = Read_Visitors_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.zone_selection()

            gender_data = Read_Visitors_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_search_btn_in_drop_down()

            result.append(self.validate_date_result(date, month, year, hour, minute, period))
            result.append(self.validate_date_result(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_search(start_age, end_age))
            result.append(self.validate_gender_search(gender_data))
            result.append(self.validate_zone_result())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_age_range_gender_"
                                       f"and_hierarchy_filter_criteriafailed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\search_visitors_with_datetime_age_range_gender_and_"
                                   f"hierarchy_filter_criteria_failed.png")
            self.log.info(f"search_visitors_with_datetime_age_range_gender_and_hierarchy_filter_criteria failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    ######################################## Resuable Methods #########################################################

    def zone_selection(self):
        zone_selection = self.d.find_element(By.XPATH,
                                             Read_Visitors_Components().zone_selection_by_xpath())
        zone_selection.click()
        time.sleep(Base_Class.one_second)

        # checkbox_list = self.d.find_elements(By.XPATH,
        #                                   Read_Visitors_Components().zone_check_bx_list_by_xpath())
        zone_text_list = self.d.find_elements(By.XPATH,
                                              Read_Visitors_Components().zone_text_list_by_xpath())

        try:
            for i in range(len(zone_text_list) + 1):
                actual_tag_text = zone_text_list.__getitem__(i).text.lower()
                print(actual_tag_text)
                expected_tag_text = Read_Visitors_Components().zone_data_input().lower()
                print(expected_tag_text)
                if expected_tag_text in actual_tag_text:
                    zone_text_list.__getitem__(i).click()
        except Exception as ex:
            str(ex)

        save_btn = self.d.find_element(By.XPATH, Read_Visitors_Components().save_button_by_xpath())
        # save_btn.click()
        self.d.execute_script("arguments[0].click();", save_btn)

    def click_on_search_drop_down(self):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().search_drop_down_by_xpath())
        ele.click()

    def click_on_search_btn_in_drop_down(self):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().search_drop_down_search_btn_by_xpath())
        ele.click()

    def select_gender(self, gender_data):
        """
        This function helps us to select the gender dropdown
        :return:
        """
        gender_ele = self.d.find_element(By.XPATH, Read_Visitors_Components().select_gender_by_xpath())

        s = Select(gender_ele)
        s.select_by_value(gender_data)

    def click_on_visitors_link(self):
        visitors_btn = self.d.find_element(By.XPATH,
                                           Read_Visitors_Components().visitors_link_by_xpath())
        visitors_btn.click()
        time.sleep(Base_Class.one_second)

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):

        # click on the form calendar popup
        if strategy == "from":
            self.click_on_start_date_check_box()
            self.click_on_start_date_text_bx_by_xpath()
        else:
            # click on the to calender pop up
            self.click_on_end_date_check_box()
            self.click_on_end_date_text_bx_by_xpath()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, Read_Visitors_Components().calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(2)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Visitors_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitors_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitors_Components().start_date_txt_bx_by_xpath())
            start_date_txt_bx.click()
        else:
            # click on the to calender pop up
            end_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitors_Components().end_date_txt_bx_by_xpath())
            end_date_txt_bx.click()

        req_month = month
        req_year = year
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        month_year = self.d.find_element(By.XPATH, Read_Visitors_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitors_Components().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitors_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitors_Components().calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitors_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        date = self.d.find_element(By.XPATH,
                                   "(//td[@class='day' or @class='day weekend' or @class='day active'])[" + str(
                                       date) + "]")
        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitors_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              Read_Visitors_Components().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_down_button = self.d.find_element(By.XPATH, Read_Visitors_Components().clock_min_up_button_by_xpath())
            clock_down_button.click()
            current_min_ele = self.d.find_element(By.XPATH, Read_Visitors_Components()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitors_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitors_Components().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   Read_Visitors_Components().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, Read_Visitors_Components()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)

        if int(cur_min) > int(minute):
            while int(cur_min) != int(minute):
                clock_up_button = self.d.find_element(By.XPATH, Read_Visitors_Components()
                                                      .clock_min_up_button_by_xpath())
                clock_up_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Visitors_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)
        else:
            while int(cur_min) != int(minute):
                clock_down_button = self.d.find_element(By.XPATH, Read_Visitors_Components()
                                                        .clock_min_down_button_by_xpath())
                clock_down_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Visitors_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)

        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitors_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitors_Components().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH, Read_Visitors_Components()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

    def select_start_age(self, start_age):
        """
        This function is used to select the start age
        :param start_age:
        :return:
        """
        start_age_ele = self.d.find_element(By.XPATH, Read_Visitors_Components().start_age_by_xpath())
        s = Select(start_age_ele)
        s.select_by_visible_text(start_age)

    def select_end_age(self, end_age):
        """
        This function is used to select the end age
        :param end_age:
        :return:
        """
        end_age_ele = self.d.find_element(By.XPATH, Read_Visitors_Components().end_age_by_xpath())
        s = Select(end_age_ele)
        s.select_by_visible_text(end_age)

    def click_on_start_date_check_box(self):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().start_date_check_bx_by_xpath())
        ele.click()

    def click_on_end_date_check_box(self):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().end_date_check_bx_by_xpath())
        ele.click()

    def click_on_start_date_text_bx_by_xpath(self):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().start_date_txt_bx_by_xpath())
        ele.click()

    def click_on_end_date_text_bx_by_xpath(self):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().end_date_txt_bx_by_xpath())
        ele.click()

    # def zones_search_result_validation(self):
    #     zones_search_result_validation = self.d.find_element(By.XPATH,
    #                                                          read_event_filter_ini().
    #                                                          zone_search_result_validation())
    #     actual_text = zones_search_result_validation.text
    #     expected_text = read_event_filter_ini().get_zone()
    #     assert actual_text == expected_text.lower()

    def validate_age_search(self, start_age, end_age):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().age_result_by_xpath())
        return start_age and end_age in ele.text

    def validate_gender_search(self, gender_data):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().gender_result_by_xpath())
        return gender_data in ele.text

    def validate_zone_result(self):
        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().zone_result_by_xpath())
        exp_zone = Read_Visitors_Components().zone_data_input().lower()
        return exp_zone in ele.text.lower()

    def validate_date_result(self, date, month, year, hour, minute, period):
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        mon = month_to_num.get(month)

        # Convert the day, month, hour, and minute to integers
        day_int = int(date)
        month_int = int(mon)
        hour_int = int(hour)
        minute_int = int(minute)

        # Format the date components with leading zeros
        date_str = f"{month_int:02d}/{day_int:02d}/{year} {hour_int:02d}:{minute_int:02d} {period}"

        print("date format: ", date_str)

        time.sleep(3)

        ele = self.d.find_element(By.XPATH, Read_Visitors_Components().date_result_by_xpath())
        return date_str in ele.text

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitors_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
                time.sleep(Base_Class.one_second)
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed.png")
                return False

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Visitors_Components().logout_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            logout_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout.png")
                return False
