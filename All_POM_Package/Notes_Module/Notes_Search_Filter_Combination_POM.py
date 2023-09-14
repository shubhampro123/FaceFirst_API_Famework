import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Notes_Search_Filter_Combination_Read_INI import \
    Read_notes_search_filter_combination
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components


class Notes_search_filter_combination_pom:

    def __init__(self, logger):
        self.d = Base_Class.d
        self.log = logger
        self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
            time.sleep(Base_Class.three_second)
        except Exception as ex:
            self.d.save_screenshot(
                    f"{self.screenshots_path}\\login_failed_for_Notes_search_filter_combination_pom.png")
            self.log.info(f"login_before:  {ex}")
            return False

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()). \
                is_displayed():
            self.login_before()

    def click_on_notes_menu(self):
        notes = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().notes_menu_button_by_xpath())
        notes.click()

    def click_on_notes_search_button(self):
        time.sleep(Base_Class.one_second)
        search_button = self.d.find_element(By.XPATH,
                                            Read_notes_search_filter_combination().notes_search_button_by_xpath())
        search_button.click()

    def click_on_description_dropdown_option(self):
        time.sleep(Base_Class.one_second)
        description_option = self.d.find_element(By.XPATH,
                                                 Read_notes_search_filter_combination().
                                                 search_dropdown_description_option_by_xpath())
        description_option.click()

    def enter_location_or_store(self):
        location_or_store = self.d.find_element(By.XPATH,
                                                Read_notes_search_filter_combination().
                                                location_or_store_input_field_by_xpath())

        location_or_store.send_keys(Read_notes_search_filter_combination().get_location_or_store())

    def enter_case_or_subject(self):
        case_or_subject = self.d.find_element(By.XPATH,
                                              Read_notes_search_filter_combination().
                                              case_or_subject_input_field_by_xpath())
        case_or_subject.send_keys(Read_notes_search_filter_combination().get_case_or_subject())

    def click_on_filter_search_button(self):
        time.sleep(Base_Class.one_second)
        filter_search_button = self.d.find_element(By.XPATH,
                                                   Read_notes_search_filter_combination().
                                                   notes_filter_search_button_by_xpath())
        filter_search_button.click()
        return filter_search_button.is_enabled()

    def sort_by_case_or_subject(self):
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().sort_by_dropdown_by_xpath())
        select = Select(ele)
        sort_by = Read_notes_search_filter_combination().get_sort_by_case_or_subject()
        select.select_by_visible_text(sort_by)

    def sort_by_location_or_store(self):
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().sort_by_dropdown_by_xpath())
        select = Select(ele)
        sort_by = Read_notes_search_filter_combination().get_sort_by_location_or_store()
        select.select_by_visible_text(sort_by)

    def location_or_store_search_result_validation(self):
        time.sleep(Base_Class.one_second)
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                location_or_store_search_result_validation_by_xpath())
        actual_text = result_validation.text.lower()
        expected_text = Read_notes_search_filter_combination().get_location_or_store().lower()
        return expected_text in actual_text

    def case_or_subject_search_result_validation(self):
        time.sleep(Base_Class.one_second)
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                case_or_subject_search_result_validation_by_xpath())
        actual_text = result_validation.text.lower()
        expected_text = Read_notes_search_filter_combination().get_case_or_subject().lower()
        return expected_text in actual_text

    def sort_by_location_or_store_validation(self):
        time.sleep(Base_Class.one_second)
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                sort_by_result_validation_by_xpath())
        actual_text = result_validation.text.lower()
        expected_text = Read_notes_search_filter_combination().get_sort_by_location_or_store().lower()
        return expected_text in actual_text

    def sort_by_case_or_subject_validation(self):
        time.sleep(Base_Class.one_second)
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                sort_by_result_validation_by_xpath())
        actual_text = result_validation.text.lower()
        expected_text = Read_notes_search_filter_combination().get_sort_by_case_or_subject().lower()
        return expected_text in actual_text

        # close tab and logout method

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,Read_notes_search_filter_combination()
                                                    .close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
                time.sleep(Base_Class.one_second)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_panel_failed_event_search_filter_combination.png")
            self.log.info(f"close all panel one by one:  {ex}")
            return False

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().logout_btn_by_xpath())
            logout_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\Button_not_clickable_logout_pg_03.png")
            self.log.info(f"logout:  {ex}")
            return False

    ######################################### Business Methods #################################################

    def notes_with_no_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            if self.click_on_filter_search_button():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_no_filter_combination_failed.png")
                status.append(False)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_no_filter_combination_failed.png")
            self.log.info(f"notes_with_no_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_sort_by_Case_Subject_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            self.sort_by_case_or_subject()
            self.click_on_filter_search_button()
            if self.sort_by_case_or_subject_validation():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_"
                                       f"with_sort_by_case_Subject_filter_combination_failed.png")
                status.append(False)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_"
                                   f"with_sort_by_case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_sort_by_location_store_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.sort_by_location_or_store()
            self.click_on_filter_search_button()

            if self.sort_by_location_or_store_validation():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes"
                                       f"_with_sort_by_location_store_filter_combination_failed.png")
                status.append(False)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes"
                                   f"_with_sort_by_location_store_filter_combination_failed.png")
            self.log.info(f"notes_with_sort_by_location_store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination()
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_"
                                   f"Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Case_Subject_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_case_or_subject()

            self.click_on_filter_search_button()

            if self.case_or_subject_search_result_validation():
                status.append(True)
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\notes_with_Case_Subject_filter_combination_failed.png")
                status.append(False)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Case_Subject_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_case_or_subject()
            self.sort_by_case_or_subject()

            self.click_on_filter_search_button()

            status.append(self.case_or_subject_search_result_validation())
            status.append(self.sort_by_case_or_subject_validation())
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Case_Subject"
                                       f"_and_Sort_by_Case_Subject_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Case_Subject"
                                   f"_and_Sort_by_Case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Case_Subject_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_filter_Case_Subject_and_Sort_by_Location_Store_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_case_or_subject()
            self.sort_by_location_or_store()

            self.click_on_filter_search_button()

            status.append(self.case_or_subject_search_result_validation())
            status.append(self.sort_by_location_or_store_validation())
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_filter_Case_Subject_and"
                                       f"_Sort_by_Location_Store_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_filter_Case_Subject_and"
                                   f"_Sort_by_Location_Store_combination_failed.png")
            self.log.info(f"notes_with_filter_Case_Subject_and_Sort_by_Location_Store_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination()
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Case_Subject_Sort_by_"
                                   f"Location_Store_and_Sort_by_Core_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Case_Subject_Sort_"
                          f"by_Location_Store_and_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_location_or_store()

            self.click_on_filter_search_button()

            if self.location_or_store_search_result_validation():
                status.append(True)
            else:
                status.append(False)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_location_or_store()
            self.sort_by_case_or_subject()

            self.click_on_filter_search_button()

            status.append(self.location_or_store_search_result_validation())
            status.append(self.sort_by_case_or_subject_validation())
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_"
                                       f"and_Sort_by_Case_Subject_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_"
                                   f"and_Sort_by_Case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_and_Sort_by_Location_Store_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_location_or_store()
            self.sort_by_location_or_store()

            self.click_on_filter_search_button()

            status.append(self.location_or_store_search_result_validation())
            status.append(self.sort_by_location_or_store_validation())
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_and"
                                       f"_Sort_by_Location_Store_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_and"
                                   f"_Sort_by_Location_Store_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_and_Sort_by_Location_Store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination()
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_Sort_by_Location_Store_and"
                                   f"_Sort_by_Core_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_Sort_by_Location_Store_and"
                          f"_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_and_Case_Subject_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_location_or_store()
            self.enter_case_or_subject()

            self.click_on_filter_search_button()

            status.append(self.location_or_store_search_result_validation())
            status.append(self.case_or_subject_search_result_validation())
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_and"
                                       f"_Case_Subject_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_and"
                                   f"_Case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_and_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_Case_Subject_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_location_or_store()
            self.enter_case_or_subject()
            self.sort_by_case_or_subject()

            self.click_on_filter_search_button()

            status.append(self.location_or_store_search_result_validation())
            status.append(self.case_or_subject_search_result_validation())
            status.append(self.sort_by_case_or_subject_validation())
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_Case_Subject_and"
                                       f"_Sort_by_Case_Subject_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_Case_Subject_and"
                                   f"_Sort_by_Case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_Case_Subject_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_Case_Subject_and_Sort_by_Location_Store_filter_combination(self):
        try:
            status = []
            self.login()
            self.click_on_notes_menu()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()

            self.enter_location_or_store()
            self.enter_case_or_subject()
            self.sort_by_location_or_store()

            self.click_on_filter_search_button()

            status.append(self.location_or_store_search_result_validation())
            status.append(self.case_or_subject_search_result_validation())
            status.append(self.sort_by_location_or_store_validation())
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_Case_Subject_and"
                                       f"_Sort_by_Location_Store_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_Case_Subject_and"
                                   f"_Sort_by_Location_Store_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_Case_Subject"
                          f"_and_Sort_by_Location_Store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination()

            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_Case_Subject_"
                                   f"Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and"
                          f"_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def validate_notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        status = []
        self.login()
        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_case_or_subject()
        self.click_on_filter_search_button()
        status.append(self.sort_by_case_or_subject_validation())
        time.sleep(Base_Class.two_second)

        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_location_or_store()
        self.click_on_filter_search_button()
        status.append(self.sort_by_location_or_store_validation())
        return status

    def validate_notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        status = []
        self.login()
        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.enter_case_or_subject()
        self.click_on_filter_search_button()
        status.append(self.case_or_subject_search_result_validation())
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_case_or_subject()
        self.click_on_filter_search_button()
        status.append(self.sort_by_case_or_subject_validation())
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_location_or_store()
        self.click_on_filter_search_button()
        status.append(self.sort_by_location_or_store_validation())
        return status

    def validate_notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        status = []
        self.login()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.enter_location_or_store()
        self.click_on_filter_search_button()
        status.append(self.location_or_store_search_result_validation())
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_location_or_store()
        self.click_on_filter_search_button()
        status.append(self.sort_by_location_or_store_validation())
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_case_or_subject()
        self.click_on_filter_search_button()
        status.append(self.sort_by_case_or_subject_validation())
        return status

    def validate_notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        status = []
        self.login()
        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_case_or_subject()
        self.click_on_filter_search_button()
        status.append(self.sort_by_case_or_subject_validation())
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_location_or_store()
        self.click_on_filter_search_button()
        status.append(self.sort_by_location_or_store_validation())
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_case_or_subject()
        self.click_on_filter_search_button()
        status.append(self.sort_by_case_or_subject_validation())
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        self.click_on_notes_search_button()
        self.click_on_description_dropdown_option()
        self.sort_by_location_or_store()
        self.click_on_filter_search_button()
        status.append(self.sort_by_location_or_store_validation())
        return status











