import time
from pathlib import Path

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.visitor_search_jobs_read_INI import Read_Visitor_Search_jobs_Components


class Visitor_Search_jobs_Module_pom:

    def __init__(self, logger):
        self.d = Base_Class.d
        self.log = logger
        self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.three_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            if not username.is_displayed():
                self.d.get(Read_Portal_Menu_Components().get_url())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            print(ex)

    def click_on_visitor_search_jobs_btn(self):
        visitor_search_jobs_btn = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().
                                                      portal_menu_visitors_search_job_btn_by_xpath())
        self.d.execute_script("arguments[0].click();", visitor_search_jobs_btn)
        time.sleep(Base_Class.two_second)

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()).\
                is_displayed():
            self.login_before()
            time.sleep(Base_Class.two_second)

    #############################################################################################################

    def Verify_user_able_to_view_the_Visitor_Search_jobs_on_the_cloud_menu(self):
        result = []
        try:
            self.login()

            visitor_search_jobs_btn = self.d.find_element(By.XPATH,
                                                          Read_Portal_Menu_Components().
                                                          portal_menu_visitors_search_job_btn_by_xpath())
            result.append(visitor_search_jobs_btn.is_displayed())

            result.append(visitor_search_jobs_btn.is_enabled())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_001_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_001_exception.png")
            self.log.info(f"test_VSJ_001_exception:  {ex}")
            return False

    def verify_user_opens_vsj_then_visitor_search_jobs_panel_should_display(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(Base_Class.one_second)
            vsj_panel_title = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                  .visitor_search_jobs_panel_by_xpath())
            result.append(vsj_panel_title.is_displayed())
            result.append(vsj_panel_title.text == Read_Visitor_Search_jobs_Components().vsj_panel_title())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_002_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_002_exception.png")
            self.log.info(f"test_VSJ_002_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_and_open_search_dropdown(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(Base_Class.one_second)
            vsj_search_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                 .visitor_search_jobs_panel_search_button())
            result.append(vsj_search_btn.is_displayed())
            result.append(vsj_search_btn.is_enabled())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_003_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_003_exception.png")
            self.log.info(f"test_VSJ_003_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            

    def verify_users_able_to_see_and_open_action_dropdown(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(Base_Class.one_second)
            vsj_action_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                 .visitor_search_jobs_panel_action_button())
            result.append(vsj_action_btn.is_displayed())
            result.append(vsj_action_btn.is_enabled())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_004_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_004_exception.png")
            self.log.info(f"test_VSJ_004_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_the_visitor_search_job_contains_the_visitors_from_the_data_range(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            try:
                self.connection_error()
            except Exception as ex:
                self.click_on_cloud_menu()
                self.click_on_visitor_search_jobs_btn()
                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_005_exception.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_005_exception.png")
            self.log.info(f"test_VSJ_005_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_user_performs_visitor_search_with_date_and_org_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_006_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_006_exception.png")
            self.log.info(f"test_VSJ_006_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_visitor_in_selected_date_range_and_gender(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_007_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_007_exception.png")
            self.log.info(f"test_VSJ_007_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_selected_gender_visitors_in_date_range_and_Org_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_008_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_008_exception.png")
            self.log.info(f"test_VSJ_008_exception:  {ex}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_visitors_in_selected_date_range_and_age_range(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_009_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_009_exception.png")
            self.log.info(f"test_VSJ_009_exception:  {ex}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_visitors_in_date_range_and_age_range_and_org_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_010_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_010_exception.png")
            self.log.info(f"test_VSJ_010_exception:  {ex}")

            return False
        finally:
            self.close_all_panel_one_by_one()
            

    def verify_the_visitor_search_job_contains_the_selected_gender_visitors_in_date_range_and_age_range(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_011_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_011_exception.png")
            self.log.info(f"test_VSJ_011_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_gender_visitors_in_date_range_and_age_range_and_org_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_012_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_012_exception.png")
            self.log.info(f"test_VSJ_012_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_the_matching_visitors_max_count_should_be_50_search_with_image_only(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= 50)

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]
            result.append(int(max_number_counted) <= 50)

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_013_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_013_exception.png")
            self.log.info(f"test_VSJ_013_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_vsj_contains_the_count_of_matching_visitors_when_visitor_search_with_image_and_max_matches(self):
        result = []
        try:
            self.add_image_search()
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_014_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_014_exception.png")
            self.log.info(f"test_VSJ_014_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_threshold_greater_than_or_equal_to_threshold_with_image_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            print(max_count)
            max_number_counted = max_matches_text.split(" ")[0]
            print(max_number_counted)
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_015_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_015_exception.png")
            self.log.info(f"test_VSJ_015_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_threshold_when_search_threshold_with_image_threshold_and_max_matches(self):
        result = []
        try:
            self.add_image_search()
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            print(max_count)
            max_number_counted = max_matches_text.split(" ")[0]
            print(max_number_counted)
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_016_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_016_exception.png")
            self.log.info(f"test_VSJ_016_fexception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_gender_result_when_the_visitor_search_with_image_and_gender(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.click_on_visitor_search_jobs_btn()
            print(gender_data)

            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_017_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_017_exception.png")
            self.log.info(f"test_VSJ_017_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_visitors_and_gender_when_search_with_image_gender_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) == int(count_data))

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) == int(count_data))

            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_018_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_018_exception.png")
            self.log.info(f"test_VSJ_018_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_visitors_and_threshold_when_search_with_image_gender_and_threshold(self):
        result = []
        try:
            self.add_image_search()
            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))

            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_019_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_019_exception.png")
            self.log.info(f"test_VSJ_019_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_gender_threshold_max_matches_when_search_with_image_gender_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()
            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_020_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_020_exception.png")
            self.log.info(f"test_VSJ_020_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            

    def verify_that_the_vsj_contains_an_age_range_when_a_visitor_search_with_an_image_and_an_age_range(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            print(start_age)
            print(end_age)
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_021_exception.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_021_exception.png")
            self.log.info(f"test_VSJ_021_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_range_max_matches_when_visitor_search_with_image_age_range_max_matches(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) == int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(count_data))

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_022_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_022_exception.png")
            self.log.info(f"test_VSJ_022_exception:  {ex}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_range_and_threshold_when_visitor_search_with_image_age_range_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            threshold_data = self.set_thresh_hold_slider()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_023_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_023_exception.png")
            self.log.info(f"test_VSJ_023_exception:  {ex}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_threshold_and_max_of_matches_when_search_with_image_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_024_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_024_exception.png")
            self.log.info(f"test_VSJ_024_exception:  {ex}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_visitor_search_job_contains_age_gender_when_visitor_search_with_image_age_gender(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            print(start_age)
            print(end_age)
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_025_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_025_exception.png")
            self.log.info(f"test_VSJ_025_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_gender_and_max_matches_when_search_with_image_age_gender_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_026_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_026_exception.png")
            self.log.info(f"test_VSJ_026_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_gender_and_threshold_when_search_with_image_age_gender_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_027_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_027_exception.png")
            self.log.info(f"test_VSJ_027_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_gender_threshold_max_matches_search_image_age_gender_threshold_max_matches(
            self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_028_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_028_exception.png")
            self.log.info(f"test_VSJ_028_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_visitor_search_job_contains_region_when_visitor_search_with_image_and_region(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_region_from_match_list(zone_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_029_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_029_exception.png")
            self.log.info(f"test_VSJ_029_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_and_max_matches_when_visitor_search_with_image_region_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_030_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_030_exception.png")
            self.log.info(f"test_VSJ_030_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            

    def verify_vsj_contains_region_and_threshold_when_visitor_search_with_image_region_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_031_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_031_exception.png")
            self.log.info(f"test_VSJ_031_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_threshold_max_matches_when_search_with_image_region_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_032_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_032_exception.png")
            self.log.info(f"test_VSJ_031_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_and_gender_when_search_with_image_region_and_gender(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_033_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_033_exception.png")
            self.log.info(f"test_VSJ_033_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_gender_max_matches_when_search_with_image_region_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_034_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_034_exception.png")
            self.log.info(f"test_VSJ_034_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_gender_and_threshold_when_search_with_image_region_gender_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_035_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_035_exception.png")
            self.log.info(f"test_VSJ_035_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_gender_threshold_max_matches_search_image_region_gender_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_036_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_036_exception.png")
            self.log.info(f"test_VSJ_036_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_and_age_range_when_search_with_image_region_and_age_range(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_037_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_037_exception.png")
            self.log.info(f"test_VSJ_037_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_range_max_matches_when_search_with_image_region_age_range_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_038_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_038_exception.png")
            self.log.info(f"test_VSJ_038_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_threshold_matches_search_with_image_region_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_039_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_039_exception.png")
            self.log.info(f"test_VSJ_039_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_threshold_max_matches_search_with_image_region_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_040_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_040_exception.png")
            self.log.info(f"test_VSJ_040_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_range_gender_when_search_with_image_region_age_range_gender(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_041_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_041_exception.png")
            self.log.info(f"test_VSJ_041_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_gender_mx_matches_when_search_with_image_region_age_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_042_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_042_exception.png")
            self.log.info(f"test_VSJ_042_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_gender_threshold_when_search_with_image_region_age_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_043_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_043_exception.png")
            self.log.info(f"test_VSJ_043_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_region_age_gender_threshold_mx_matches_search_image_region_age_gender_threshold_mx_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_044_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_044_exception.png")
            self.log.info(f"test_VSJ_044_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_when_search_with_image_and_date_range(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_045_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_045_exception.png")
            self.log.info(f"test_VSJ_045_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_max_matches_when_search_with_image_and_date_range_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(count_data))
            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            print(result)

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_046_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_046_exception.png")
            self.log.info(f"test_VSJ_046_exception:  {ex}")
            return False

        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_threshold_when_search_with_image_and_date_range_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            print(result)

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_047_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_047_exception.png")
            self.log.info(f"test_VSJ_047_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_threshold_max_matches_search_image_date_range_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_cloud_menu()
            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_048_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_048_exception.png")
            self.log.info(f"test_VSJ_048_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_gender_when_search_with_image_date_range_and_gender(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_049_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_049_exception.png")
            self.log.info(f"test_VSJ_049_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_gender_max_matches_search_with_image_date_range_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_050_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_050_exception.png")
            self.log.info(f"test_VSJ_050_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            

    def verify_vsj_contains_date_range_gender_threshold_search_with_image_date_range_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_051_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_051_exception.png")
            self.log.info(f"test_VSJ_051_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_range_gender_threshold_mx_matches_search_image_date_range_gender_threshold_mx_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_052_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_052_exception.png")
            self.log.info(f"test_VSJ_052_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_age_when_search_with_image_date_range_and_age(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_053_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_053_exception.png")
            self.log.info(f"test_VSJ_053_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_age_and_max_matches_when_search_image_date_range_age_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_054_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_054_exception.png")
            self.log.info(f"test_VSJ_054_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_age_and_threshold_when_search_image_date_range_age_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_055_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_055_exception.png")
            self.log.info(f"test_VSJ_055_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_threshold_max_matches_search_image_date_range_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_056_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_056_exception.png")
            self.log.info(f"test_VSJ_056_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_gender_when_search_with_image_date_range_age_and_gender(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_057_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_057_exception.png")
            self.log.info(f"test_VSJ_057_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_gender_max_matches_search_with_image_date_range_age_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_058_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_058_exception.png")
            self.log.info(f"test_VSJ_058_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_gender_threshold_search_with_image_date_range_age_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_059_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_059_exception.png")
            self.log.info(f"test_VSJ_059_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_age_gender_threshold_matches_search_image_date_range_age_gender_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(Base_Class.two_second)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_060_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_060_exception.png")
            self.log.info(f"test_VSJ_060_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_when_search_with_image_date_range_region(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_061_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_061_exception.png")
            self.log.info(f"test_VSJ_061_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_max_matches_when_search_with_image_date_range_region_max_matches(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_062_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_062_exception.png")
            self.log.info(f"test_VSJ_062_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_max_matches_search_image_date_region_age_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_063_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_063_exception.png")
            self.log.info(f"test_VSJ_063_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_threshold_max_matches_search_image_date_region_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(int(max_number) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_064_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_064_exception.png")
            self.log.info(f"test_VSJ_064_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_gender_when_search_with_image_date_region_and_gender(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_065_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_065_exception.png")
            self.log.info(f"test_VSJ_065_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_gender_max_matches_search_with_image_date_region_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_066_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_066_exception.png")
            self.log.info(f"test_VSJ_066_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_gender_threshold_search_with_image_date_region_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_067_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_067_exception.png")
            self.log.info(f"test_VSJ_067_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_region_gender_threshold_matches_search_image_date_region_gender_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_068_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_068_exception.png")
            self.log.info(f"test_VSJ_068_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_and_age_when_search_with_image_date_region_and_age(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_region_from_match_list(zone_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_069_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_069_exception.png")
            self.log.info(f"test_VSJ_069_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_max_matches_when_search_with_image_date_region_age_max_matches(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_070_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_070_exception.png")
            self.log.info(f"test_VSJ_070_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            

    def verify_vsj_contains_date_region_age_threshold_when_search_with_image_date_region_age_threshold(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_071_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_071_exception.png")
            self.log.info(f"test_VSJ_071_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_threshold_matches_search_image_date_region_age_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_072_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_072_exception.png")
            self.log.info(f"test_VSJ_072_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_when_search_with_image_date_region_age_and_gender(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_073_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_073_exception.png")
            self.log.info(f"test_VSJ_073_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_matches_search_image_date_region_age_gender_and_matches(
            self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_074_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_074_exception.png")
            self.log.info(f"test_VSJ_074_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_threshold_search_image_date_region_age_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_075_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_075_exception.png")
            self.log.info(f"test_VSJ_075_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_region_age_gender_threshold_max_search_image_date_region_age_gender_threshold_max(self):
        result = []
        try:
            self.add_image_search()

            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_date(date, month, year, hour, minute, period))
            result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_076_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_076_exception.png")
            self.log.info(f"test_VSJ_076_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_for_visitor_search_with_meta_data_single_edge_or_store_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()
            date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.nats_checkbox()

            self.click_on_submit_search_button()
            try:
                self.connection_error()
            except Exception as ex:

                self.click_on_cloud_menu()

                self.click_on_visitor_search_jobs_btn()

                result.append(self.verify_date(date, month, year, hour, minute, period))
                result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_077_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_077_exception.png")
            self.log.info(f"test_VSJ_077_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_visitor_search_with_an_image_the_default_match_count_should_be_50(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(50))

            self.click_on_visitor_search_jobs_btn()

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]
            result.append(int(max_number_counted) <= int(50))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_078_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_078_exception.png")
            self.log.info(f"test_VSJ_078_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_vs_with_image_the_visitor_search_result_should_be_listed_in_descending_order(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.close_all_panel_one_by_one()

            self.click_on_visitor_search_jobs_btn()

            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                              visitor_search_jobs_panel_view_results())
            view_result.click()

            result.append(self.score_list_in_descending_order())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_079_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_079_exception.png")
            self.log.info(f"test_VSJ_079_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_view_result_button_is_visible_and_clickable_in_the_visitor_search_jobs_panel(self):
        result = []
        try:
            self.add_image_search()

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()

            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_jobs_panel_view_results())

            result.append(view_result.is_enabled())

            result.append(view_result.is_displayed())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_080_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_080_exception.png")
            self.log.info(f"test_VSJ_080_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            

    def verify_the_visitors_search_results_according_to_the_selected_max_match_count(self):
        result = []
        try:
            self.add_image_search()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) == int(count_data))

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_081_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_81_exception.png")
            self.log.info(f"test_VSJ_081_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitors_search_results_match_score_it_should_be_in_descending_order(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()

            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                              visitor_search_jobs_panel_view_results())
            view_result.click()

            time.sleep(Base_Class.one_second)

            result.append(self.score_list_in_descending_order())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_082_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_082_exception.png")
            self.log.info(f"test_VSJ_082_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_action_button_on_the_visitor_search_jobs_panel_is_visible_and_clickable(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            action_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                .visitor_search_jobs_panel_action_button())
            result.append(action_button.is_displayed())
            result.append(action_button.is_enabled())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_084_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_084_exception.png")
            self.log.info(f"test_VSJ_084_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_action_dropdown_options_cancel_jobs_delete_jobs_refresh_change_refresh_visible_clickable(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            action_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                .visitor_search_jobs_panel_action_button())
            action_button.click()

            cancel_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_jobs_panel_cancel_jobs())
            delete_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_jobs_panel_delete_jobs())
            refresh_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                               .visitor_search_jobs_panel_refresh())
            refresh_rate_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                    .visitor_search_jobs_panel_show_panel_refresh_rate())

            result.append(cancel_text.is_displayed())
            result.append(cancel_text.is_enabled())
            result.append(delete_text.is_displayed())
            result.append(delete_text.is_enabled())
            result.append(refresh_text.is_displayed())
            result.append(refresh_text.is_enabled())
            result.append(refresh_rate_text.is_displayed())
            result.append(refresh_rate_text.is_enabled())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_085_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_085_exception.png")
            self.log.info(f"test_VSJ_085_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_view_result_panel_Location_identify_enrollments_track_faces_identify_visitors_visible_clickble(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()

            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .completed_job_view_result_button())
            view_result.click()
            time.sleep(Base_Class.one_second)
            location_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                 .visitor_search_result_panel_location_by_xpath())
            result.append(location_button.is_enabled())
            result.append(location_button.is_displayed())

            identify_within_enrollments = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                 .visitor_search_result_panel_identify_within_enrollments())
            result.append(identify_within_enrollments.is_enabled())
            result.append(identify_within_enrollments.is_displayed())

            extend_menu = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                 .visitor_search_result_panel_extend_menu_by_xpath())
            result.append(extend_menu.is_enabled())
            result.append(extend_menu.is_displayed())
            extend_menu.click()

            track_faces = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_result_panel_track_faces_by_xpath())
            result.append(track_faces.is_enabled())
            result.append(track_faces.is_displayed())

            identify_within_visitors = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_result_panel_identify_within_visitors_xpath())
            result.append(identify_within_visitors.is_enabled())
            result.append(identify_within_visitors.is_displayed())

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_086_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_086_exception.png")
            self.log.info(f"test_VSJ_086_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    ################################# generic methods ##############################################

    def nats_checkbox(self):
        """
        This function is used to enable and disable NATS
        :return:
        """
        time.sleep(Base_Class.one_second)
        NATS_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().nats_checkbox_xpath())
        NATS_checkbox.click()
        time.sleep(Base_Class.one_second)

    def close_all_panel_one_by_one(self):
        try:
            time.sleep(Base_Class.one_second)
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_jobs_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            print(ex)

    def verify_image_from_match_list(self):
        time.sleep(Base_Class.one_second)
        ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().image_match_list_by_xpath())
        for e in ele:
            if not e.is_displayed():
                return False
            else:
                return True

    def verify_region_from_match_list(self, zone_data):
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                  .visitor_search_jobs_panel_search_constraints())
        ac_zone_txt = ele.text

        if zone_data.upper() not in ac_zone_txt:
            return False
        else:
            return True

        # lower result zone text validation code
        # match_region = self.d.find_elements(By.XPATH,
        #                                     Read_Visitor_Search_jobs_Components().match_region_by_xpath())
        #
        # for x in match_region:
        #     if x.text != zone_data:
        #         result = False
        #         break

    def verify_date(self, date, month, year, hour, minute, period):
        time.sleep(Base_Class.two_second)
        month_to_mm = {
            "January": "JAN",
            "February": "FEB",
            "March": "MAR",
            "April": "APR",
            "May": "MAY",
            "June": "JUN",
            "July": "JUL",
            "August": "AUG",
            "September": "SEP",
            "October": "OCT",
            "November": "NOV",
            "December": "DEC"
        }
        mon = month_to_mm.get(month)

        exp_asser = "{mon} {date}, {year} {hour}:{minu} {pe}"
        exp_asser = exp_asser.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=period)

        ac_start_date = self.d.find_element(By.XPATH,
                                            Read_Visitor_Search_jobs_Components().
                                            visitor_search_jobs_panel_search_constraints())
        ac_ass_date = ac_start_date.text.upper()
        if exp_asser.upper() in ac_ass_date:
            return True
        else:
            return False

    def close_all_the_panels(self):
        """
        This function is used to close all the visitor search panels
        :return:
        """
        close_icon = self.d.find_elements(By.XPATH,
                                          Read_Visitor_Search_jobs_Components().
                                          close_all_visitor_search_panel_by_xpath())
        for x in close_icon:
            x.click()

    def select_zone(self, zone):
        """
        This function is used to handle the zone drop-down and select the required options
        :return:
        """
        zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_by_xpath())
        zone_ele.click()
        time.sleep(Base_Class.two_second)
        zone_text_list = self.d.find_elements(By.XPATH,
                                              Read_Visitor_Search_jobs_Components().zone_text_list_xpath())
        expected_zone_text = zone.upper()
        try:
            for i in range(len(zone_text_list)):
                actual_zone_text = zone_text_list.__getitem__(i).text
                # expected_zone_text = Read_Visitor_Search_jobs_Components().get_zone().upper()
                if expected_zone_text.upper() in actual_zone_text.upper():
                    zone_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_save_button_xpath())
            self.d.execute_script("arguments[0].click();", save)
        except Exception as ex:
            str(ex)
        # zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_by_xpath())
        # zone_ele.click()
        # time.sleep(Base_Class.one_second
        # root_selection = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().root_selection_xpath())
        # assert root_selection.is_displayed()
        # self.d.execute_script("arguments[0].click();", root_selection)
        # save = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_save_button_xpath())
        # self.d.execute_script("arguments[0].click();", save)

    def select_start_age(self, start_age):
        """
        This function is used to select the start age
        :param start_age:
        :return:
        """
        start_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().start_age_by_xpath())
        s = Select(start_age_ele)
        s.select_by_visible_text(start_age)
        time.sleep(Base_Class.one_second)

    def select_end_age(self, end_age):
        """
        This function is used to select the end age
        :param end_age:
        :return:
        """
        end_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().end_age_by_xpath())
        s = Select(end_age_ele)
        s.select_by_visible_text(end_age)
        time.sleep(Base_Class.one_second)

    def validate_age_matches_list(self, start_age, end_age):
        """
        This function is used to validate the age
        :param start_age:
        :param end_age:
        :return:
        """
        time.sleep(Base_Class.one_second)
        age_range = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().
                                         visitor_search_jobs_panel_search_constraints())

        if start_age in age_range and end_age in age_range:
            return True
        else:
            return False

    def validate_age_matches_list_in_visitor_search_results(self, start_age, end_age):
        """
        This function is used to validate the age
        :param start_age:
        :param end_age:
        :return:
        """
        time.sleep(Base_Class.one_second)
        age_range = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                        visitor_search_result_panel_search_constraints())
        age_range = age_range.text
        if start_age in age_range and end_age in age_range:
            return True
        else:
            return False

    def compare_thresh_hold_value_with_score(self):
        """
        This function is used to compare the threshhold value with actual score
        :return:
        """
        # slider = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().slider_icon_by_xpath())
        # slider_value_str = str(slider.get_attribute("style"))
        # slider_value_text = slider_value_str.split(" ")[1].strip()
        # slider_value_text = re.sub("[% ;]", "", slider_value_text)
        #
        # match_list_score = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().score_by_xpath())
        # for ele in match_list_score:
        #     score = ele.text
        #     score = int(score.split(".")[1][0:2])
        #     if not score >= int(slider_value_text):
        #         return False
        #     else:
        #         return True
        pass

    def set_thresh_hold_slider(self):
        """
        This function is used to set the threshold value
        :return:
        """
        slider_pixel = Read_Visitor_Search_jobs_Components().slider_value_data_input()
        slider_pixel_value = int(slider_pixel)

        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().slider_icon_by_xpath())
        action = ActionChains(self.d)
        action.drag_and_drop_by_offset(slider, -80, 0).perform()

        action.drag_and_drop_by_offset(slider, slider_pixel_value, 0).perform()
        return slider_pixel

    def select_count(self, count_data):
        """
        This function is used to select the count from the count dropdown
        :param count_data:
        :return:
        """
        max_match = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().max_of_matches_by_xpath())
        select = Select(max_match)

        select.select_by_visible_text(count_data)
        time.sleep(Base_Class.one_second)

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """
        submit_btn = self.d.find_element(By.XPATH,
                                         Read_Visitor_Search_jobs_Components().submit_search_button_by_xpath())
        submit_btn.click()

    def verify_gender_match_list(self, expected_gender):
        """
        This function is used to the verify te gender with the actual match list
        :param expected_gender:
        :return:
        """
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().search_constraints_by_xpath())
        ac_gender_txt = ele.text
        ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_matches_found())

        if (expected_gender.upper() not in ac_gender_txt) or (not ele2.is_displayed()):
            return False
        else:
            return True

        # match_gender_list = self.d.find_elements(By.XPATH,
        #                                          Read_Visitor_Search_jobs_Components().matches_gender_by_xpath())
        # ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_matches_found())
        # for ele in match_gender_list:
        #     gender = ele.text
        #     if (expected_gender.upper() not in gender) or (not ele2.is_displayed()):
        #         return False
        #     else:
        #         return True

    def verify_gender_match_list_in_visitors(self, expected_gender):
        """
        This function is used to the verify te gender with the actual match list
        :param expected_gender:
        :return:
        """
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                  .visitor_search_result_panel_search_constraints())
        ac_gender_txt = ele.text

        if expected_gender.upper() not in ac_gender_txt:
            return False
        else:
            return True

    def select_gender(self, gender_data):
        """
        This function helps us to select the gender dropdown
        :return:
        """
        gender_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().select_gender_by_xpath())

        s = Select(gender_ele)
        s.select_by_value(gender_data)
        time.sleep(Base_Class.one_second)

    def refresh_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the match has been found
        :return:
        """
        refresh_icon = self.d.find_element(By.XPATH,
                                           Read_Visitor_Search_jobs_Components().refresh_icon_by_xpath())
        while refresh_icon.is_displayed():
            time.sleep(Base_Class.one_second)

    def submitting_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the submitting is not complete
        :return:
        # """
        # submit_icon = self.d.find_element(By.XPATH,
        #                                   Read_Visitor_Search_jobs_Components().submitting_archive_search_wait_icon())
        # while submit_icon.is_displayed():
        #
        pass

    def add_image_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        self.login()
        self.click_on_visitor_search()
        upload_photo = self.d.find_element(By.XPATH,
                                           Read_Visitor_Search_jobs_Components().photo_upload_container_by_xpath())
        upload_photo.click()
        time.sleep(Base_Class.one_second)
        file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\img1.png"
        # file_path = f"{os.environ['WORKSPACE']}/Test_Data/img/img1.png"
        # file_path = Path(__file__).parent / "img1.png"
        # script_directory = Path(__file__).parent
        # file_path = script_directory / ".." / ".." / "Test_Data" / "img" / "img1.png"
        ##############################
        # file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Try1\\Test_Data\\img\\img1.png"
        # file_path = 'C:\\Users\\baps\\Pictures\\uim.png'
        # file_path = 'D:\Chrome_Download\img1.png'

        pyautogui.write(file_path)
        # pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(Base_Class.one_second)
        pyautogui.press('enter')
        time.sleep(Base_Class.one_second)
        # configure_search = self.d.find_element(By.XPATH,
        #                                        Read_Visitor_Search_jobs_Components().configure_search_by_xpath())
        # configure_search.click()
        # configure_search.click()

    def compare_count_match(self, count_data):
        """
        This function is used to compare the count provided with the actual no. of match count
        :param count_data:
        :return:
        """
        # match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().matches_found_by_xpath())
        # match_found_count = int(match_found.text)

        #
        pass

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):

        # click on the form calendar popup
        if strategy == "from":
            start_check_bx = self.d.find_element(By.XPATH,
                                                 Read_Visitor_Search_jobs_Components().
                                                 start_date_checkbox_by_xpath())
            start_check_bx.click()
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                    start_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
            start_date_txt_bx.click()
        else:
            # click on the to calender pop up
            end_check_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                               end_date_checkbox_by_xpath())
            end_check_bx.click()
            end_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().end_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", end_date_txt_bx)
            end_date_txt_bx.click()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                             calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                        calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                    start_date_by_xpath())
            start_date_txt_bx.click()
        else:
            # click on the to calender pop up
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                                    end_date_by_xpath())
            start_date_txt_bx.click()

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
        month_year = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                         calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_jobs_Components().
                                                  calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_jobs_Components().
                                                  calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        date = self.d.find_element(By.XPATH,
                                   "(//td[@class='day' or @class='day weekend' or @class='day active' "
                                   "or @class='day active today'])[" + str(date) + "]")
        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().calender_tick_icon_by_xpath())

        tick_icon.click()

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH,
                                               Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().hour_down_by_xpath())

            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_down_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                    .clock_min_down_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_down_button)
            current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH,
                                               Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().hour_down_by_xpath())
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        print(cur_min)
        while int(cur_min) != int(minute):
            clock_up_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                  .clock_min_up_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_up_button)
            current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def verify_date_range(self, start_year, end_year):
        month_to_num = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }
        date_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().match_date_list_by_xpath())
        ac_date = int()
        ac_month = int()
        ac_year = int()
        for x in date_list:
            dt = x.text
            b = dt.split(" ")
            ac_year = int(b[2])
        ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_matches_found())
        if (start_year <= ac_year <= end_year) or (ele2.is_displayed()):
            return True
        else:
            return False

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().logout_btn_by_xpath())
            logout_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            print(ex)

    def check_if_match_is_found(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_match_found_by_xpath())
        if ele.is_displayed():
            return False
        else:
            return True

    def verify_Must_specify_start_and_end_date_for_meta_data_only_search(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                  start_end_date_validation_msg_verify_xpath())
        actual_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_jobs_Components().meta_data_without_date_validation_msg().strip(). \
            lower()

        time.sleep(Base_Class.two_second)
        alert = self.d.switch_to.alert
        error_msg1 = alert.text
        alert.accept()
        if (ele.is_displayed() and actual_validation_text == expected_validation_text) or (
                error_msg1 == Read_Visitor_Search_jobs_Components().connection_error()):
            return True
        else:
            return False

    def verify_limited_to_30_min_interval_validation(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                  limited_to_30_min_interval_validation())
        actutal_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_jobs_Components().limited_to_30_meta_data_search_validation().strip(). \
            lower()
        print(actutal_validation_text)
        print(expected_validation_text)
        if ele.is_displayed() and actutal_validation_text == expected_validation_text:
            return True
        else:
            return False

    def verify_max_matches_not_display(self):
        """
        This function is used validate the max matches element
        :return:
        """
        max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().max_of_matches_by_xpath())
        if not max_matches.is_displayed():
            return True
        else:
            return False

    def verify_threshold_not_display(self):
        """
        This function is used validate the threshold element
        :return:
        """
        threshold = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().threshold_slider_by_xpath())
        if not threshold.is_displayed():
            return True
        else:
            return False

    def click_on_visitor_search(self):
        visitor_search_btn = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().
                                                 portal_menu_visitors_search_btn_by_xpath())
        self.d.execute_script("arguments[0].click();", visitor_search_btn)
        time.sleep(Base_Class.two_second)

    def click_on_cloud_menu(self):
        click_on_cloud_menu = visitor_search_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                                       .cloud_menu_by_xpath())
        click_on_cloud_menu.click()

        self.d.execute_script("arguments[0].click();", visitor_search_btn)
        time.sleep(Base_Class.one_second)

    def connection_error(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().
                                  start_end_date_validation_msg_verify_xpath())
        actual_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_jobs_Components().meta_data_without_date_validation_msg().strip(). \
            lower()

        time.sleep(Base_Class.two_second)
        alert = self.d.switch_to.alert
        error_msg1 = alert.text
        alert.accept()
        if (ele.is_displayed() and actual_validation_text == expected_validation_text) or (
                error_msg1 == Read_Visitor_Search_jobs_Components().connection_error()):
            return True
        else:
            return False

    def score_list_in_descending_order(self):
        score_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().
                                          visitor_search_result_panel_scores())

        score = []
        for x in score_list:
            score.append(x.text.split(" ")[1])
        for i in range(len(score) - 1):
            if score[i] < score[i + 1]:
                return False
            return True
