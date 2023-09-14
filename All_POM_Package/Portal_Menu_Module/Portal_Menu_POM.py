import time
from pathlib import Path
from selenium.webdriver.common.by import By
from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components


class Portal_Menu_pom:

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
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\portal_menu_login_failed.png")
            self.log.info(f"login_before:  {ex}")
            return False

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()). \
                is_displayed():
            self.login_before()

    def click_on_event_button(self):
        try:
            event_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_event_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", event_button)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_event_button_failed.png")
            self.log.info(f"click_on_event_button:  {ex}")

    def event_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_event_button()
            event_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_event_validation_by_xpath()
                                                   )
            actual_event_panel_text = event_validation.text
            expected_event_panel_text = Read_Portal_Menu_Components().event_panel_validation_text()
            status.append(actual_event_panel_text == expected_event_panel_text)
            self.log.info(f"event_validation.is_displayed :{event_validation.is_displayed()}")
            if event_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_button_validation_failed.png")
            self.log.info(f"event_button_validation:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def click_on_tags_button(self):
        try:
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", tags_button)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_tags_button_failed.png")
            self.log.info(f"click_on_tags_button:  {ex}")

    def tags_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_tags_button()
            tags_validation = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().portal_menu_tags_validation_by_xpath())
            actual_tags_panel_text = tags_validation.text
            expected_tags_panel_text = Read_Portal_Menu_Components().tags_panel_validation_text()
            status.append(actual_tags_panel_text == expected_tags_panel_text)
            self.log.info(f"tags_validation.is_displayed :{tags_validation.is_displayed()}")
            if tags_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\tags_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tags_button_validation_failed.png")
            self.log.info(f"tags_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_identify_enroll_button(self):
        try:
            identify_enroll_button = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_identify_enroll_btn_by_xpath())
            identify_enroll_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_identify_enroll_button_failed.png")
            self.log.info(f"click_on_identify_enroll_button:  {ex}")

    def identify_enroll_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_identify_enroll_button()
            identify_enroll_validation = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_indentify_enroll_validation_by_xpath())
            actual_identify_enroll_validation_text = identify_enroll_validation.text
            expected_identify_enroll_validation_text = Read_Portal_Menu_Components(). \
                identify_and_enroll_panel_validation_text()
            status.append(actual_identify_enroll_validation_text == expected_identify_enroll_validation_text)
            self.log.info(f"identify_enroll_validation.is_displayed :{identify_enroll_validation.is_displayed()}")
            if identify_enroll_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\identify_enroll_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\identify_enroll_button_validation_failed.png")
            self.log.info(f"identify_enroll_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_detect_faces_button(self):
        try:
            detect_faces_button = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().
                                                      portal_menu_detect_faces_btn_by_xpath())
            detect_faces_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_detect_faces_button_failed.png")
            self.log.info(f"click_on_detect_faces_button:  {ex}")

    def detect_faces_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_detect_faces_button()
            detect_faces_validation = self.d.find_element(By.XPATH,
                                                          Read_Portal_Menu_Components().
                                                          portal_menu_detect_faces_validation_by_xpath())
            actual_detect_faces_validation = detect_faces_validation.text
            expected_detect_faces_validation = Read_Portal_Menu_Components().detect_faces_validation_text()
            status.append(actual_detect_faces_validation == expected_detect_faces_validation)
            self.log.info(f"detect_faces_validation.is_displayed :{detect_faces_validation.is_displayed()}")
            if detect_faces_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\detect_faces_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\detect_faces_button_validation_failed.png")
            self.log.info(f"detect_faces_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_enrollments_button(self):
        try:
            enrollments_button = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().
                                                     portal_menu_enrollments_btn_by_xpath())
            enrollments_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_enrollments_button_failed.png")
            self.log.info(f"click_on_enrollments_button:  {ex}")

    def enrollments_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_enrollments_button()
            enrollments_validation = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_enrollments_validation_by_xpath())
            actual_enrollments_validation = enrollments_validation.text
            expected_enrollments_validation = Read_Portal_Menu_Components().enrollments_panel_validation_text()
            status.append(actual_enrollments_validation == expected_enrollments_validation)
            self.log.info(f"enrollments_validation.is_displayed :{enrollments_validation.is_displayed()}")
            if enrollments_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\enrollments_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\enrollments_button_validation_failed.png")
            self.log.info(f"enrollments_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_enrollments_groups_button(self):
        try:
            enrollments_groups_button = self.d.find_element(By.XPATH,
                                                            Read_Portal_Menu_Components().
                                                            portal_menu_enrollments_groups_btn_by_xpath())
            enrollments_groups_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_enrollments_groups_button_failed.png")
            self.log.info(f"click_on_enrollments_groups_button:  {ex}")

    def enrollments_groups_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_enrollments_groups_button()
            enrollments_groups_validation = self.d.find_element(By.XPATH,
                                                                Read_Portal_Menu_Components().
                                                                portal_menu_enrollments_groups_validation_by_xpath())
            actual_enrollments_groups_validation = enrollments_groups_validation.text
            expected_enrollments_groups_validation = Read_Portal_Menu_Components(). \
                enrollments_groups_panel_validation_text()
            status.append(actual_enrollments_groups_validation == expected_enrollments_groups_validation)
            self.log.info(f"enrollments_groups_validation.is_displayed :{enrollments_groups_validation.is_displayed()}")
            if enrollments_groups_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\enrollments_groups_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\enrollments_groups_button_validation_failed.png")
            self.log.info(f"enrollments_groups_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_notification_groups_button(self):
        try:
            notification_groups_button = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_notification_groups_btn_by_xpath())
            notification_groups_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_enrollments_groups_button_failed.png")
            self.log.info(f"click_on_enrollments_groups_button:  {ex}")

    def notification_groups_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_notification_groups_button()
            notification_groups_validation = self.d.find_element(By.XPATH,
                                                                 Read_Portal_Menu_Components().
                                                                 portal_menu_notification_groups_validation_by_xpath())
            actual_notification_groups_validation = notification_groups_validation.text
            expected_notification_groups_validation = Read_Portal_Menu_Components(). \
                notification_groups_panel_validation_text()
            status.append(actual_notification_groups_validation == expected_notification_groups_validation)
            self.log.info(f"notification_groups_validation.is_displayed :"
                          f"{notification_groups_validation.is_displayed()}")
            if notification_groups_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\notification_groups_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notification_groups_button_validation_failed.png")
            self.log.info(f"notification_groups_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_visitors_button(self):
        try:
            visitors_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().portal_menu_visitors_btn_by_xpath())
            visitors_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_visitors_button_failed.png")
            self.log.info(f"click_on_visitors_button:  {ex}")

    def visitors_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_visitors_button()
            visitors_validation = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().
                                                      portal_menu_visitors_validation_by_xpath())
            actual_visitors_validation = visitors_validation.text
            expected_visitors_validation = Read_Portal_Menu_Components().visitors_panel_validation_text()
            status.append(actual_visitors_validation == expected_visitors_validation)
            self.log.info(f"visitors_validation.is_displayed :{visitors_validation.is_displayed()}")
            if visitors_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\visitors_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_button_validation_failed.png")
            self.log.info(f"visitors_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_visitors_search_button(self):
        try:
            visitors_search_button = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_visitors_search_btn_by_xpath())
            visitors_search_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_visitors_search_button_failed.png")
            self.log.info(f"click_on_visitors_search_button:  {ex}")

    def visitors_search_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_visitors_search_button()
            visitors_search_validation = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_visitors_search_validation_by_xpath())
            actual_visitors_search_validation = visitors_search_validation.text
            expected_visitors_search_validation = Read_Portal_Menu_Components().visitor_search_panel_validation_text()
            status.append(actual_visitors_search_validation == expected_visitors_search_validation)
            self.log.info(f"visitors_search_validation.is_displayed :{visitors_search_validation.is_displayed()}")
            if visitors_search_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_button_validation_failed.png")
            self.log.info(f"visitors_search_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_visitors_search_job_button(self):
        try:
            visitors_search_job_button = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_visitors_search_job_btn_by_xpath())
            visitors_search_job_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_button_validation_failed.png")
            self.log.info(f"visitors_search_button_validation:  {ex}")

    def visitors_search_button_job_validation(self):
        try:
            status = []
            self.login()
            self.click_on_visitors_search_job_button()
            visitors_search_job_validation = self.d.find_element(By.XPATH,
                                                                 Read_Portal_Menu_Components().
                                                                 portal_menu_visitors_search_job_validation_by_xpath())
            actual_visitors_search_job_validation = visitors_search_job_validation.text
            expected_visitors_search_job_validation = Read_Portal_Menu_Components().visitor_search_jobs_panel_text()
            status.append(actual_visitors_search_job_validation == expected_visitors_search_job_validation)
            self.log.info(f"visitors_search_job_validation.is_displayed :"
                          f"{visitors_search_job_validation.is_displayed()}")
            if visitors_search_job_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_button_job_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_button_job_validation_failed.png")
            self.log.info(f"visitors_search_button_job_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_notes_button(self):
        try:
            notes_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_notes_btn_by_xpath())
            notes_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_notes_button_failed.png")
            self.log.info(f"click_on_notes_button:  {ex}")

    def notes_validation(self):
        try:
            status = []
            self.login()
            self.click_on_notes_button()
            notes_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().
                                                   portal_menu_notes_validation_by_xpath())
            actual_notes_validation = notes_validation.text
            expected_notes_validation = Read_Portal_Menu_Components().notes_panel_validation_text()
            status.append(actual_notes_validation == expected_notes_validation)
            self.log.info(f"notes_validation.is_displayed :{notes_validation.is_displayed()}")
            if notes_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\notes_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_validation_failed.png")
            self.log.info(f"notes_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_locations_button(self):
        try:
            locations_button = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_locations_btn_by_xpath())
            locations_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_locations_button_failed.png")
            self.log.info(f"click_on_locations_button:  {ex}")

    def locations_validation(self):
        try:
            status = []
            self.login()
            self.click_on_locations_button()
            locations_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       portal_menu_locations_validation_by_xpath())
            cancel_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().
                                                location_cancel_button())
            actual_locations_validation = locations_validation.text
            expected_locations_validation = Read_Portal_Menu_Components().locations_panel_validation_text()
            status.append(actual_locations_validation == expected_locations_validation)
            self.log.info(f"locations_validation.is_displayed :{locations_validation.is_displayed()}")
            if locations_validation.is_displayed():
                self.d.execute_script("arguments[0].click();", cancel_button)
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\locations_validation_failed.png")
                self.d.execute_script("arguments[0].click();", cancel_button)
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\locations_validation_failed.png")
            self.log.info(f"locations_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_users_button(self):
        try:
            users_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_users_btn_by_xpath())
            users_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_users_button_failed.png")
            self.log.info(f"click_on_users_button:  {ex}")

    def users_validation(self):
        try:
            status = []
            self.login()
            self.click_on_users_button()
            users_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_users_validation_by_xpath()
                                                   )
            actual_users_validation = users_validation.text
            expected_users_validation = Read_Portal_Menu_Components().user_panel_validation_text()
            status.append(actual_users_validation == expected_users_validation)
            self.log.info(f"users_validation.is_displayed :{users_validation.is_displayed()}")
            if users_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\users_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\users_validation_failed.png")
            self.log.info(f"users_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_users_role_button(self):
        try:
            users_roles_button = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().
                                                     portal_menu_users_roles_btn_by_xpath())
            users_roles_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_users_role_button_failed.png")
            self.log.info(f"click_on_users_role_button:  {ex}")

    def users_roles_validation(self):
        try:
            status = []
            self.login()
            self.click_on_users_role_button()
            users_roles_validation = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_users_roles_validation_by_xpath())
            actual_users_roles_validation = users_roles_validation.text
            expected_users_roles_validation = Read_Portal_Menu_Components().user_roles_validation_text()
            status.append(actual_users_roles_validation == expected_users_roles_validation)
            self.log.info(f"users_roles_validation.is_displayed :{users_roles_validation.is_displayed()}")
            if users_roles_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\users_roles_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\users_roles_validation_failed.png")
            self.log.info(f"users_roles_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_zones_button(self):
        try:
            zones_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_zones_btn_by_xpath())
            zones_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_zones_button_failed.png")
            self.log.info(f"click_on_zones_button:  {ex}")

    def zones_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_zones_button()
            zones_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_zones_validation_by_xpath()
                                                   )
            actual_zones_validation = zones_validation.text
            expected_zones_validation = Read_Portal_Menu_Components().zones_panel_validation_text()
            status.append(actual_zones_validation == expected_zones_validation)
            self.log.info(f"zones_validation.is_displayed :{zones_validation.is_displayed()}")
            if zones_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\zones_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\zones_button_validation_failed.png")
            self.log.info(f"zones_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_account_button(self):
        try:
            account_button = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().portal_menu_account_btn_by_xpath())
            account_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_account_button_failed.png")
            self.log.info(f"click_on_account_button:  {ex}")

    def account_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_account_button()
            account_validation = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().
                                                     portal_menu_account_validation_by_xpath())
            actual_account_validation = account_validation.text
            expected_account_validation = Read_Portal_Menu_Components().account_panel_validation_text()
            status.append(actual_account_validation == expected_account_validation)
            self.log.info(f"account_validation.is_displayed :{account_validation.is_displayed()}")
            if account_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\account_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\account_button_validation_failed.png")
            self.log.info(f"account_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_reporting_button(self):
        try:
            reporting_button = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_reporting_btn_by_xpath())
            reporting_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_reporting_button_failed.png")
            self.log.info(f"click_on_reporting_button:  {ex}")

    def reporting_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_reporting_button()
            reporting_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       portal_menu_reporting_validation_by_xpath())
            actual_reporting_validation = reporting_validation.text
            expected_reporting_validation = Read_Portal_Menu_Components().reporting_validation_text()
            status.append(actual_reporting_validation == expected_reporting_validation)
            self.log.info(f"reporting_validation.is_displayed :{reporting_validation.is_displayed()}")
            if reporting_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\reporting_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\reporting_button_validation_failed.png")
            self.log.info(f"reporting_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_notifier_button(self):
        try:
            notifier_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().portal_menu_notifier_btn_by_xpath())
            notifier_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_notifier_button_failed.png")
            self.log.info(f"click_on_notifier_button:  {ex}")

    def notifier_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_notifier_button()
            notifier_validation = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().
                                                      portal_menu_notifier_validation_by_xpath())
            close = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().
                                        notifier_close_button())
            actual_notifier_validation = notifier_validation.text
            expected_notifier_validation = Read_Portal_Menu_Components().notifier_panel_validation_text()
            status.append(actual_notifier_validation == expected_notifier_validation)
            self.log.info(f"notifier_validation.is_displayed :{notifier_validation.is_displayed()}")
            if notifier_validation.is_displayed():
                close.click()
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\notifier_button_validation_failed.png")
                close.click()
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notifier_button_validation_failed.png")
            self.log.info(f"notifier_button_validation:  {ex}")

    def click_on_dashboard_button(self):
        try:
            dashboard_button = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_dashboard_btn_by_xpath())
            dashboard_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_dashboard_button_failed.png")
            self.log.info(f"click_on_dashboard_button:  {ex}")

    def dashboard_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_dashboard_button()
            self.d.switch_to.window(self.d.window_handles[1])
            dashboard_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       portal_menu_dashboard_validation_by_xpath())
            actual_dashboard_validation = dashboard_validation.text
            excepted_dashboard_validation = Read_Portal_Menu_Components().dashboard_panel_validation_text()
            status.append(actual_dashboard_validation == excepted_dashboard_validation)
            self.log.info(f"dashboard_validation.is_displayed :{dashboard_validation.is_displayed()}")
            if dashboard_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\dashboard_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\dashboard_button_validation_failed.png")
            self.log.info(f"dashboard_button_validation:  {ex}")
        finally:
            self.d.close()
            self.d.switch_to.window(self.d.window_handles[0])

    def click_on_audit_report_button(self):
        try:
            audit_report_button = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().audit_log_reports_btn_xpath())
            audit_report_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_audit_report_button_failed.png")
            self.log.info(f"click_on_audit_report_button:  {ex}")

    def audit_reports_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_audit_report_button()
            self.d.switch_to.window(self.d.window_handles[1])
            audit_report_validation = self.d.find_element(By.XPATH,
                                                          Read_Portal_Menu_Components().
                                                          audit_log_reports_validation())
            self.log.info(f"actual audit_report_validation is displayed :{audit_report_validation.is_displayed()}")
            if audit_report_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\audit_reports_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\audit_reports_button_validation_failed.png")
            self.log.info(f"audit_reports_button_validation:  {ex}")
        finally:
            self.d.close()
            self.d.switch_to.window(self.d.window_handles[0])

    def click_on_copyright_button(self):
        try:
            copyright_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().copyright_btn_by_xpath())
            copyright_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_copyright_button_failed.png")
            self.log.info(f"click_on_copyright_button:  {ex}")

    def copyright_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_copyright_button()
            copyright_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().copyright_validation_by_xpath())
            status.append(copyright_validation.text.__contains__(
                Read_Portal_Menu_Components().copyright_version_text_validation()))
            status.append(copyright_validation.text.__contains__(
                Read_Portal_Menu_Components().copyright_year_text_validation()))
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\copyright_button_validation_failed.png")
            self.log.info(f"copyright_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_profile_button(self):
        try:
            profile_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().profile_btn_by_xpath())
            profile_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_profile_button_failed.png")
            self.log.info(f"click_on_profile_button:  {ex}")

    def profile_button_validation(self):
        try:
            status = []
            self.login()
            self.click_on_profile_button()
            profile_validation = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().profile_validation_by_xpath())
            actual_profile_validation = profile_validation.text
            excepted_profile_validation = Read_Portal_Menu_Components().validation_user_panel_text()
            status.append(actual_profile_validation == excepted_profile_validation)
            self.log.info(f"profile_validation.is_displayed :{profile_validation.is_displayed()}")
            if profile_validation.is_displayed():
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\profile_button_validation_failed.png")
                status.append(False)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\profile_button_validation_failed.png")
            self.log.info(f"profile_button_validation:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def click_on_logout_button(self):
        try:
            logout_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logout_btn_by_xpath())
            logout_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_logout_button_failed.png")
            self.log.info(f"click_on_logout_button:  {ex}")

    def face_first_logo_validation(self):
        try:
            self.login()
            logo = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logo_by_xpath())
            p = self.d.execute_script(
                "return arguments[0].complete " + "&& typeof arguments[0].naturalWidth != \"undefined\" " + "&& arguments[0].naturalWidth > 0",
                logo)
            result = p
            if result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\face_first_logo_validation_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\face_first_logo_validation_failed.png")
            self.log.info(f"face_first_logo_validation:  {ex}")

    def logout_button_validation(self):
        try:
            status = []
            self.login()
            logout_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logout_btn_by_xpath())
            actual_logout_button_text = logout_button.text
            expected_logout_button_text = Read_Portal_Menu_Components().logout_button_expected_text()
            status.append(actual_logout_button_text == expected_logout_button_text)
            self.d.execute_script("arguments[0].click();", logout_button)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\logout_button_validation_failed.png")
            self.log.info(f"logout_button_validation:  {ex}")

    def reset_password(self):
        try:
            status = []
            self.login()
            password = [Read_Portal_Menu_Components().new_password(), Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().new_password()]
            for i in range(2):
                self.click_on_profile_button()
                time.sleep(Base_Class.one_second)
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                edit_button.click()
                time.sleep(Base_Class.one_second)
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                save_btn.click()
                time.sleep(Base_Class.one_second)
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                status.append(actual_password_change_success_msg == expected_password_change_success_msg)
                status.append(password_updated.is_displayed())
            if status.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\reset_password_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\reset_password_failed.png")
            self.log.info(f"reset_password:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def current_and_new_password_not_same_validation(self):
        try:
            status = []
            self.login()
            self.click_on_profile_button()
            action_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
            action_button.click()
            time.sleep(Base_Class.one_second)
            edit_button = self.d.find_element(By.XPATH,
                                              Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
            edit_button.click()
            time.sleep(Base_Class.one_second)
            current_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().current_password_filed_by_xpath())
            name_field = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().rest_password_first_name_input())
            last_name_field = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().rest_password_last_name_input())
            if name_field.get_attribute("value") is "":
                name_field.send_keys(Read_Portal_Menu_Components().first_name())
            if last_name_field.get_attribute("value") is "":
                last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
            current_password.send_keys(Read_Portal_Menu_Components().get_password())
            new_password = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().new_password_filed_by_xpath())
            new_password.send_keys(Read_Portal_Menu_Components().get_password())
            confirm_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
            confirm_password.send_keys(Read_Portal_Menu_Components().get_password())
            save_btn = self.d.find_element(By.XPATH,
                                           Read_Portal_Menu_Components().save_new_password())
            save_btn.click()
            time.sleep(Base_Class.one_second)
            validation_msg = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().
                                                 current_and_new_password_not_same_validation())
            actual_validation_msg = validation_msg.text
            expected_validation_msg = Read_Portal_Menu_Components().current_psw_and_new_psw_not_same_validation()
            status.append(actual_validation_msg == expected_validation_msg)
            cancel_btn = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().user_panel_cancel_btn())
            cancel_btn.click()
            time.sleep(Base_Class.one_second)
            closed_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_panel_close_btn())
            closed_button.click()
            time.sleep(Base_Class.one_second)
            if status.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\"
                                       f"current_and_new_password_not_same_validation_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\current_and_new_password_not_same_validation_failed.png")
            self.log.info(f"current_and_new_password_not_same_validation:  {ex}")

    def set_upper_case_password(self):
        try:
            status = []
            self.login()
            password = [Read_Portal_Menu_Components().get_upper_case_password(),
                        Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().get_upper_case_password()]
            for i in range(2):
                self.click_on_profile_button()
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                edit_button.click()
                time.sleep(Base_Class.one_second)
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                save_btn.click()
                time.sleep(Base_Class.one_second)
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                status.append(actual_password_change_success_msg == expected_password_change_success_msg)
            if status.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\set_upper_case_password_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_upper_case_password_failed.png")
            self.log.info(f"set_upper_case_password:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def set_lower_case_password(self):
        try:
            status = []
            self.login()
            password = [Read_Portal_Menu_Components().get_lower_case_password(),
                        Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().get_lower_case_password()]
            for i in range(2):
                self.click_on_profile_button()
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                edit_button.click()
                time.sleep(Base_Class.one_second)
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                save_btn.click()
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                status.append(actual_password_change_success_msg == expected_password_change_success_msg)
            if status.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\set_lower_case_password_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_lower_case_password_failed.png")
            self.log.info(f"set_lower_case_password:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def set_special_character_password(self):
        try:
            status = []
            self.login()
            password = [Read_Portal_Menu_Components().get_special_character_password(),
                        Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().get_special_character_password()]
            for i in range(2):
                self.click_on_profile_button()
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                edit_button.click()
                time.sleep(Base_Class.one_second)
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                save_btn.click()
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                status.append(actual_password_change_success_msg == expected_password_change_success_msg)
            if status.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\set_special_character_password_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_special_character_password_failed.png")
            self.log.info(f"set_special_character_password:  {ex}")
        finally:
            self.close_all_panel_one_by_one()

    def set_less_than_eight_character_password(self):
        try:
            status = []
            self.login()
            self.click_on_profile_button()
            action_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
            action_button.click()
            time.sleep(Base_Class.one_second)
            edit_button = self.d.find_element(By.XPATH,
                                              Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
            edit_button.click()
            time.sleep(Base_Class.one_second)
            name_field = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().rest_password_first_name_input())
            last_name_field = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().rest_password_last_name_input())
            if name_field.get_attribute("value") is "":
                name_field.send_keys(Read_Portal_Menu_Components().first_name())
            if last_name_field.get_attribute("value") is "":
                last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
            current_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().current_password_filed_by_xpath())
            current_password.send_keys(Read_Portal_Menu_Components().get_password())
            new_password = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().new_password_filed_by_xpath())
            new_password.send_keys(Read_Portal_Menu_Components().get_less_than_eight_character_password())
            confirm_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
            confirm_password.send_keys(Read_Portal_Menu_Components().get_less_than_eight_character_password())
            save_btn = self.d.find_element(By.XPATH,
                                           Read_Portal_Menu_Components().save_new_password())
            save_btn.click()
            time.sleep(Base_Class.one_second)
            less_char_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       less_than_eight_character_validation_password())
            actual_less_char_validation = less_char_validation.text
            expected_less_char_validation = Read_Portal_Menu_Components().less_than_eight_char_password_validation()
            status.append(actual_less_char_validation == expected_less_char_validation)
            cancel_btn = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().user_panel_cancel_btn())
            cancel_btn.click()
            time.sleep(Base_Class.one_second)
            closed_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_panel_close_btn())
            closed_button.click()
            time.sleep(Base_Class.one_second)
            if status.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\set_less_than_eight_character_password_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_less_than_eight_character_password_failed.png")
            self.log.info(f"set_less_than_eight_character_password:  {ex}")

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Portal_Menu_Components().close_all_panel_list())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one:  {ex}")

    def close_all_panel_button(self):
        try:
            status = []
            self.login()
            self.click_on_enrollments_button()
            time.sleep(Base_Class.one_second)
            cloud_menu_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_cloud_menu_btn_by_xpath())
            cloud_menu_button.click()
            time.sleep(Base_Class.one_second)
            self.click_on_tags_button()
            cloud_menu_button.click()
            time.sleep(Base_Class.one_second)
            self.click_on_visitors_search_button()
            cloud_menu_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_cloud_menu_btn_by_xpath())
            cloud_menu_button.click()
            time.sleep(Base_Class.one_second)
            closed_all_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_closed_all_btn_by_xpath())
            actual_closed_all_panel_text = closed_all_button.text
            expected_closed_all_panel_text = Read_Portal_Menu_Components().close_all_panel_expected_text()
            status.append(actual_closed_all_panel_text == expected_closed_all_panel_text)
            closed_all_button.click()
            time.sleep(Base_Class.one_second)
            if status.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_button_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_button_failed.png")
            self.log.info(f"close_all_panel_button:  {ex}")
