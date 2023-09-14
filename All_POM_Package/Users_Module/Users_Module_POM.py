import random
import time
from pathlib import Path

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Users_Read_INI import Read_Users_Components

#######################  Selenium Methods  #######################

driver = Base_Class.d
action = ActionChains(driver)


def move_to_element(web_element):
    """
    moves the mouse cursor to a particular element
    :param web_element:
    :return:
    """
    action.move_to_element(web_element).perform()


def scroll_to_element(web_element):
    """
    scrolls the scrollbar to the particular element
    :param web_element:
    :return:
    """
    action.scroll_to_element(web_element).perform()


def javascript_executor_click(web_element):
    """
    click on a web element
    :param web_element:
    :return:
    """
    driver.execute_script("arguments[0].click();", web_element)


def select_options_visible_text(web_element, visible_text):
    """
    handles a drop-down using visible text
    :param web_element:
    :param visible_text: provide the visible text of the web element
    :return:
    """
    select = Select(web_element)
    select.select_by_visible_text(visible_text)


def select_options_value(web_element, value):
    """
    handles drop-down using value
    :param web_element:
    :param value: provide the value present in the value attribute
    :return:
    """
    select = Select(web_element)
    select.select_by_value(value)


def generate_random_number():
    return random.randint(1, 1000)


class Users_Module_pom:

    def __init__(self, logger):
        self.d = Base_Class.d
        self.log = logger
        self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID,
                                                     Read_Portal_Menu_Components().get_loginButton()).is_displayed():
            self.login_before()

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.three_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            if not username.is_displayed():
                self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.three_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            javascript_executor_click(login_btn)
            time.sleep(Base_Class.three_second)

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(login_failed_for_users_menu_failed.png")
            self.log.info(f"login_before_failed: {ex}")
            return False

    def verify_user_able_to_view_the_user_on_cloud_menu(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            users_menu = self.d.find_element(By.XPATH, Read_Users_Components().users_cloud_menu_by_xpath())
            ac_result.append(users_menu.is_displayed())
            exp = Read_Users_Components().users_cloud_menu_validation_text()
            act = users_menu.text
            self.log.info(f"Text Expected : {exp}")
            self.log.info(f"Text Displayed : {act}")
            print(exp)
            print(act)
            ac_result.append(users_menu.text == Read_Users_Components().users_cloud_menu_validation_text())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_view_the_user_on_cloud_menu_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_view_the_user_on_cloud_menu_failed.png")
            self.log.info(f"verify_user_able_to_view_the_user_on_cloud_menu_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_opens_user_then_users_panel_should_display(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            users_panel = self.d.find_element(By.XPATH, Read_Users_Components().users_panel_title_by_xpath())
            ac_result.append(users_panel.is_displayed())
            ac_result.append(users_panel.text == Read_Users_Components().users_panel_title_validation_text())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_opens_user_then_users_panel_should_display_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_opens_user_then_users_panel_should_display_failed.png")
            self.log.info(f"verify_user_opens_user_then_users_panel_should_display_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_and_open_action_dropdown(self):
        try:
            ex_result = [True, True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            ac_result.append(action_btn.text == Read_Users_Components().action_dropdown_validation_text())
            ac_result.append(action_btn.is_displayed())
            ac_result.append(action_btn.is_enabled())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_and_open_action_dropdown_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_and_open_action_dropdown_failed.png")
            self.log.info(f"verify_user_able_to_see_and_open_action_dropdown_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_see_refresh(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            action_btn.click()
            refresh = self.d.find_element(By.XPATH, Read_Users_Components().refresh_by_xpath())
            ac_result.append(refresh.text == Read_Users_Components().refresh_validation_text())
            ac_result.append(refresh.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_see_refresh_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_able_to_see_refresh_failed.png")
            self.log.info(f"verify_users_able_to_see_refresh_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_create_user(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            action_btn.click()
            create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
            ac_result.append(create_user.text == Read_Users_Components().create_user_validation_text())
            ac_result.append(create_user.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_create_user_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_create_user_failed.png")
            self.log.info(f"verify_user_able_to_see_create_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_delete_selected_user(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_btn()
            delete_user = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
            ac_result.append(delete_user.text == Read_Users_Components().delete_selected_user_validation_text())
            ac_result.append(delete_user.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_delete_selected_user_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_delete_selected_user_failed.png")
            self.log.info(f"verify_user_able_to_see_delete_selected_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_clicks_refresh_then_it_should_refresh_the_users_list(self):
        try:
            ex_result = [True, True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            refresh = self.d.find_element(By.XPATH, Read_Users_Components().refresh_by_xpath())
            ac_result.append(refresh.is_enabled())
            try:
                self.click_on_action_refresh_option()
                ac_result.append(True)
            except Exception as e:
                ac_result.append(False)
            updating_indicator = self.d.find_element(By.XPATH, Read_Users_Components().updating_indicator_by_xpath())
            ac_result.append(updating_indicator.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_clicks_refresh_then_it_should_"
                    f"refresh_the_users_list_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_clicks_refresh_then_it_should_refresh_the_users_list_failed.png")
            self.log.info(f"verify_user_clicks_refresh_then_it_should_refresh_the_users_list_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_clicks_create_user_user_panel_should_be_displayed(self):
        try:
            ex_result = [True, True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
            ac_result.append(create_user.is_enabled())
            self.click_on_action_create_user_option()
            user_panel_title = self.d.find_element(By.XPATH, Read_Users_Components().users_panel_title_by_xpath())
            ac_result.append(user_panel_title.text == Read_Users_Components().users_panel_title_validation_text())
            ac_result.append(user_panel_title.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_clicks_create_user_user_panel_should_be_displayed_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_clicks_create_user_user_panel_should_be_displayed_failed.png")
            self.log.info(f"verify_user_clicks_create_user_user_panel_should_be_displayed_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_title_new_user_details_face_first_is_visible(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            user_panel_header = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_header_by_xpath())
            ac_result.append(user_panel_header.text == Read_Users_Components().user_panel_header_validation_text())
            ac_result.append(user_panel_header.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_title_new_user_details_face_first_is_visible_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_title_new_user_details_face_first_is_visible_failed.png")
            self.log.info(f"verify_title_new_user_details_face_first_is_visible_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_cancel_and_save_button_is_present(self):
        try:
            ex_result = [True, True, True, True, True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
            save = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_save_button_by_xpath())
            ac_result.append(cancel.text == Read_Users_Components().user_panel_cancel_btn_validation_text())
            ac_result.append(save.text == Read_Users_Components().user_panel_save_btn_validation_text())
            ac_result.append(cancel.is_displayed())
            ac_result.append(save.is_displayed())
            ac_result.append(cancel.is_enabled())
            ac_result.append(save.is_enabled())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_cancel_and_save_button_is_present_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_cancel_and_save_button_is_present_failed.png")
            self.log.info(f"verify_cancel_and_save_button_is_present_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_username_required_text_for_username(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            user_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_name_by_xpath())
            user_name_txt_bx.clear()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().user_name_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().user_name_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_username_required_text_for_username_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_username_required_text_for_username_failed.png")
            self.log.info(f"verify_user_able_to_see_username_required_text_for_username_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_user_role_required_text_for_user_role(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().user_role_error_msg())
            ac_result.append(error_msg.text == Read_Users_Components().user_role_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_user_role_required_text_for_user_role_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_user_role_required_text_for_user_role_failed.png")
            self.log.info(f"verify_user_able_to_see_user_role_required_text_for_user_role_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_password_required_and_confirm_password_required_text_for_password(self):
        try:
            ex_result = [True, True, True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
            new_password.clear()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().new_password_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().new_password_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().confirm_password_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_password_required_"
                    f"and_confirm_password_required_text_for_password_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_password_required_"
                f"and_confirm_password_required_text_for_password_failed.png")
            self.log.info(f"verify_user_able_to_see_password_required_and_"
                          f"confirm_password_required_text_for_password_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_region_required_text_for_region(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().region_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().region_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_region_required_text_for_region_failed.png")

                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_region_required_text_for_region_failed.png")
            self.log.info(f"verify_user_able_to_see_region_required_text_for_region_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_email_required_text_for_email(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().email_error_msg_by_xpath())
            scroll_to_element(error_msg)
            ac_result.append(error_msg.text == Read_Users_Components().email_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_email_required_text_for_email_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_email_required_text_for_email_failed.png")
            self.log.info(f"verify_user_able_to_see_email_required_text_for_email_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_timezone_required_text_for_timezone(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_error_msg_by_xpath())
            scroll_to_element(error_msg)
            ac_result.append(error_msg.text == Read_Users_Components().time_zone_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_timezone_required_text_for_timezone_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_timezone_required_text_for_timezone_failed.png")
            self.log.info(f"verify_user_able_to_see_timezone_required_text_for_timezone_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_enabled_checkbox_is_selected(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            checkbox = self.d.find_element(By.XPATH, Read_Users_Components().enabled_by_xpath())
            checkbox_value = checkbox.get_attribute("class")
            ac_result.append("checked" in checkbox_value)
            ac_result.append(checkbox.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_enabled_checkbox_is_selected_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_enabled_checkbox_is_selected_failed.png")
            self.log.info(f"verify_enabled_checkbox_is_selected_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_select_disabled_checkbox(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            checkbox = self.d.find_element(By.XPATH, Read_Users_Components().disabled_by_xpath())
            checkbox.click()
            checkbox_value = checkbox.get_attribute("class")
            ac_result.append("checked" in checkbox_value)
            ac_result.append(checkbox.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_select_disabled_checkbox_failed.png")

                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_select_disabled_checkbox_failed.png")
            self.log.info(f"verify_user_able_to_select_disabled_checkbox_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_username_textbox_and_fill_username(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().user_name_input_data()
            user_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_name_by_xpath())
            ac_result.append(user_name_txt_bx.is_enabled())
            user_name_txt_bx.send_keys(expected)
            actual = user_name_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_username_textbox_and_fill_username_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_username_textbox_and_fill_username_failed.png")
            self.log.info(f"verify_user_able_to_see_username_textbox_and_fill_username_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_first_name_textbox_and_fill_first_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().first_name_input_data()
            first_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().first_name_by_xpath())
            ac_result.append(first_name_txt_bx.is_enabled())
            first_name_txt_bx.send_keys(expected)
            actual = first_name_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_first_name_textbox_and_fill_first_name_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_first_name_textbox_and_fill_first_name_failed.png")
            self.log.info(f"verify_user_able_to_see_first_name_textbox_and_fill_first_name_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_last_name_textbox_and_fill_last_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().last_name_input_data()
            last_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().last_name_by_xpath())
            ac_result.append(last_name_txt_bx.is_enabled())
            last_name_txt_bx.send_keys(expected)
            actual = last_name_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_last_name_textbox_and_fill_last_name_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_last_name_textbox_and_fill_last_name_failed.png")
            self.log.info(f"verify_user_able_to_see_last_name_textbox_and_fill_last_name_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_user_role_dropdown_is_present_and_choose_the_user_roles(self):
        try:
            result = bool
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
            user_role.click()
            time.sleep(Base_Class.two_second)
            user_role_ele_with_options_ele = self.d \
                .find_elements(By.XPATH, Read_Users_Components().user_role_options_by_xpath())
            user_role_ele_options = []
            for e in user_role_ele_with_options_ele:
                user_role_ele_options.append(e.text)
            select = Select(user_role)
            for e in user_role_ele_options:
                select.select_by_visible_text(e)
                time.sleep(Base_Class.one_second)
                if not e == select.first_selected_option.text:
                    result = False
                    break
            result = True
            if result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_user_role_dropdown_is_present_and_"
                    f"choose_the_user_roles_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_user_role_dropdown_is_present_and_"
                f"choose_the_user_roles_failed.png")
            self.log.info(f"verify_user_able_to_see_user_role_dropdown_is_present_"
                          f"and_choose_the_user_roles_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_password_textbox_and_fill_password(self):
        try:
            ex_result = [True, True, True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().password_data_input()
            new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
            confirm_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
            ac_result.append(new_password.is_enabled())
            ac_result.append(confirm_password.is_enabled())
            new_password.send_keys(expected)
            confirm_password.send_keys(expected)
            actual = new_password.get_attribute("value")
            ac_result.append(expected == actual)
            actual = confirm_password.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_password_textbox_and_fill_password_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_password_textbox_and_fill_password_failed.png")
            self.log.info(f"verify_user_able_to_see_password_textbox_and_fill_password_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_company_textbox_and_enter_their_company_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().company_input_data()
            company_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().company_by_xpath())
            ac_result.append(company_txt_bx.is_enabled())
            company_txt_bx.send_keys(expected)
            actual = company_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_company_textbox_and_enter_their"
                    f"_company_name_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_company_textbox_and_enter_their"
                f"_company_name_failed.png")
            self.log.info(f"verify_user_able_to_see_company_textbox_and_enter_their_company_name_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_title_textbox_and_enter_title(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().title_input_data()
            title_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().title_by_xpath())
            ac_result.append(title_txt_bx.is_enabled())
            title_txt_bx.send_keys(expected)
            actual = title_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_title_textbox_and_enter_title_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_title_textbox_and_enter_title_failed.png")
            self.log.info(f"verify_user_able_to_see_title_textbox_and_enter_title_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_region_popup_and_choose_a_region(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            region = Read_Users_Components().region_data_input()
            self.select_region(region)
            if self.validate_region(region):
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_region_popup_and_choose_a_region_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_region_popup_and_choose_a_region_failed.png")
            self.log.info(f"verify_user_able_to_see_region_popup_and_choose_a_region_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_department_textbox_and_enter_their_department_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().department_input_data()
            department_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().department_by_xpath())
            ac_result.append(department_txt_bx.is_enabled())
            department_txt_bx.send_keys(expected)
            actual = department_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_department_textbox_"
                    f"and_enter_their_department_name_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_department_textbox_"
                f"and_enter_their_department_name_failed.png")
            self.log.info(f"verify_user_able_to_see_department_textbox_and_enter_their_department_name_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_email_textbox_and_enter_a_valid_email(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().email_input_data()
            email_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
            ac_result.append(email_txt_bx.is_enabled())
            email_txt_bx.send_keys(expected)
            actual = email_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_email_textbox_and_enter_a_valid_email_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_email_textbox_and_enter_a_valid_email_failed.png")
            self.log.info(f"verify_user_able_to_see_email_textbox_and_enter_a_valid_email_failed: {ex}")
            return False
        finally:

            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_alert_email_and_enter_a_valid_alert_email(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().alert_email_input_data()
            alert_email_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().alert_email_by_xpath())
            ac_result.append(alert_email_txt_bx.is_enabled())
            alert_email_txt_bx.send_keys(expected)
            actual = alert_email_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_alert_email_and_enter_a_valid_alert_email_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_alert_email_and_enter_a_valid_alert_email_failed.png")
            self.log.info(f"verify_user_able_to_see_alert_email_and_enter_a_valid_alert_email_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_alert_phone_number_and_enter_a_valid_phone_number(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().alert_phone_no_input_data()
            alert_ph_no_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().alert_phone_number_by_xpath())
            ac_result.append(alert_ph_no_txt_bx.is_enabled())
            alert_ph_no_txt_bx.send_keys(expected)
            actual = alert_ph_no_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_alert_phone_number_and_"
                    f"enter_a_valid_phone_number_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_alert_phone_number_and_"
                f"enter_a_valid_phone_number_failed.png")
            self.log.info(f"verify_user_able_to_see_alert_phone_number_and_enter_a_valid_phone_number_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_timezone_dropdown_and_select_a_timezone(self):
        try:
            result = bool
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time_zone = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
            time_zone.click()
            time_zone_options_ele = self.d.find_elements(By.XPATH, Read_Users_Components().time_zone_options_by_xpath())
            time_zone_options = []
            select = Select(time_zone)
            for ele in time_zone_options_ele:
                value = ele.get_attribute("value")
                time_zone_options.append(value)
                select.select_by_value(value)
                ac = select.first_selected_option.get_attribute("value")
                if not value == ac:
                    result = False
                    break
            result = True
            if result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_timezone_dropdown_"
                    f"and_select_a_timezone_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_timezone_dropdown_and_select_a_timezone_failed.png")
            self.log.info(f"verify_user_able_to_see_timezone_dropdown_and_select_a_timezone_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_address_textbox_and_enter_their_address(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().address_input_data()
            address_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().address_by_xpath())
            ac_result.append(address_txt_bx.is_enabled())
            address_txt_bx.send_keys(expected)
            actual = address_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_address_textbox_and_"
                    f"enter_their_address_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_address_textbox_and_enter_their_address_failed.png")
            self.log.info(f"verify_user_able_to_see_address_textbox_and_enter_their_address_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_address_2_textbox_and_enter_their_address(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().address2_input_data()
            address2_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().address2_by_xpath())
            ac_result.append(address2_txt_bx.is_enabled())
            address2_txt_bx.send_keys(expected)
            actual = address2_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_address_2_textbox_"
                    f"and_enter_their_address_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_address_2_textbox_and_enter_their_address_failed.png")
            self.log.info(f"verify_user_able_to_see_address_2_textbox_and_enter_their_address_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_city_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().city_input_data()
            city_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().city_by_xpath())
            ac_result.append(city_txt_bx.is_enabled())
            city_txt_bx.send_keys(expected)
            actual = city_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_city_textbox_and_fill_it_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_city_textbox_and_fill_it_failed.png")
            self.log.info(f"verify_user_able_to_see_city_textbox_and_fill_it_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_state_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().state_input_data()
            state_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().state_by_xpath())
            ac_result.append(state_txt_bx.is_enabled())
            state_txt_bx.send_keys(expected)
            actual = state_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_state_textbox_and_fill_it_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_state_textbox_and_fill_it_failed.png")
            self.log.info(f"verify_user_able_to_see_state_textbox_and_fill_it_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_postal_code_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().postal_code_input_data()
            postal_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().postal_code_by_xpath())
            ac_result.append(postal_txt_bx.is_enabled())
            postal_txt_bx.send_keys(expected)
            actual = postal_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_postal_code_textbox_and_fill_it_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_postal_code_textbox_and_fill_it_failed.png")
            self.log.info(f"verify_user_able_to_see_postal_code_textbox_and_fill_it_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_house_phone_number_textbox_and_enter_a_valid_phone_number(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().home_phone_no_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().home_phone_number_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_house_phone_number_textbox_"
                    f"and_enter_a_valid_phone_number_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_house_phone_number_textbox_"
                f"and_enter_a_valid_phone_number_failed.png")
            self.log.info(f"verify_user_able_to_see_house_phone_number_textbox_and_"
                          f"enter_a_valid_phone_number_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_users_able_to_see_work_phone_number_textbox_and_enter_a_valid_work_phone_number(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().work_phone_no_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().work_phone_number_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_see_work_phone_number_textbox_and_enter"
                    f"_a_valid_work_phone_number_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_able_to_see_work_phone_number_textbox_and_enter"
                f"_a_valid_work_phone_number_failed.png")
            self.log.info(f"verify_users_able_to_see_work_phone_number_textbox_and_enter_a_valid_work_"
                          f"phone_number_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_users_able_to_see_fax_phone_number_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().fax_phone_no_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().fax_phone_number_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_see_fax_phone_number_textbox_and_fill_it_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_able_to_see_fax_phone_number_textbox_and_fill_it_failed.png")
            self.log.info(f"verify_users_able_to_see_fax_phone_number_textbox_and_fill_it_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_phone_type_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().phone_type_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().phone_type_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_phone_type_textbox_and_fill_it_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_phone_type_textbox_and_fill_it_failed.png")
            self.log.info(f"verify_user_able_to_see_phone_type_textbox_and_fill_it_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_phone_provider_dropdown_and_select_the_required_phone_provider(self):
        try:
            status = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            ph_prov_bx = self.d.find_element(By.XPATH, Read_Users_Components().phone_provider_drop_dwn_by_xpath())
            select = Select(ph_prov_bx)
            options = select.options
            print(options)
            for option in options:
                value = option.get_attribute("text")
                select.select_by_visible_text(value)
                time.sleep(Base_Class.two_second)
                if not value == select.first_selected_option.text:
                    status.append(False)
            if False in status:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_phone_provider_dropdown_and_select_the_"
                    f"required_phone_provider_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_phone_provider_dropdown_and_select_the_"
                f"required_phone_provider_failed.png")
            self.log.info(f"verify_user_able_to_see_phone_provider_dropdown_and_select_the_required_phone"
                          f"_provider_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_alert_schedule_is_disabled(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
            if not btn.is_enabled():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_alert_schedule_is_disabled_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_alert_schedule_is_disabled_failed.png")
            self.log.info(f"verify_alert_schedule_is_disabled_failed: {ex}")
            return False
        finally:

            self.close_single_panel()

    def verify_notification_groups_is_disabled(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            btn = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_btn_by_xpath())
            if not btn.is_enabled():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_notification_groups_is_disabled_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_notification_groups_is_disabled_failed.png")
            self.log.info(f"verify_notification_groups_is_disabled_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_close_user_panel_on_clicking_cancel_button(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
            panel_count = len(panel_list)
            cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
            cancel.click()
            panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
            new_panel_count = len(panel_list)
            if new_panel_count < panel_count:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_close_user_panel_on_clicking_"
                    f"cancel_button_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_able_to_close_user_panel_on_clicking_cancel_button_failed.png")
            self.log.info(f"verify_users_able_to_close_user_panel_on_clicking_cancel_button_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_close_users_pane(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
            cancel.click()
            close_btn = self.d.find_element(By.XPATH, Read_Users_Components().users_panel_close_panel_btn())
            javascript_executor_click(close_btn)
            users_cloud_menu = self.d. \
                find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_users_btn_by_xpath())
            if users_cloud_menu.is_displayed():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_close_users_pane_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_able_to_close_users_pane_failed.png")
            self.log.info(f"verify_users_able_to_close_users_pane_failed: {ex}")
            return False

    def verify_user_fills_first_name_and_last_name_then_save_should_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_close_users_pane_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_and_last_name_then"
                f"_save_should_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_and_last_name_then_save_should_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                    f"time_zone_save_display_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                f"time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_and_time_zone_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                    f"email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                f"email_save_display_error_message_failed.png")
            self.log.info(
                f"verify_user_fills_first_name_last_name_and_email_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_email_and"
                    f"_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_email_and"
                f"_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_email_and_"
                          f"time_zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                    f"region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                f"region_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_and_region_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_region_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_region_and_"
                    f"time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_region_and_"
                f"time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_region_and_time_"
                          f"zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_region_"
                    f"and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_region_"
                f"and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_region_and_email_save_d"
                          f"isplay_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_region_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_region_"
                    f"email_and_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_region_"
                f"email_and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_region_email_and_time_"
                          f"zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                    f"password_save_display_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                f"password_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_and_password_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_mame_last_name_password_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_mame_last_name_password_"
                    f"and_time_zone_save_display_error_message_failed.png")
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_mame_last_name_password_"
                f"and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_mame_last_name_password_and_time_"
                          f"zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                    f"and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                f"and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_password_and_email_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                    f"email_and_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                f"email_and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_password_email_and_"
                          f"time_zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_"
                    f"password_and_region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_"
                f"password_and_region_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_password_and_"
                          f"region_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_region_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                    f"region_and_time_zone_save_display_error_message_failed.png")

                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                f"region_and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_password_region_and_"
                          f"time_zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                    f"region_and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_password_"
                f"region_and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_password_region_and_email_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_last_name_password_region_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_last_name_password_region_"
                    f"email_and_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_last_name_password_region_"
                f"email_and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_last_name_password_region_email_and_time_"
                          f"zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_user_role_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                    f"user_role_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_and_"
                f"user_role_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_and_user_role_save_display_"
                          f"error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"and_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_and_time_zone_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_"
                    f"user_role_and_email_save_display_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_"
                f"user_role_and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_and_"
                          f"email_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_"
                    f"role_email_and_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_"
                f"role_email_and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_email_and_"
                          f"time_zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_"
                    f"role_and_region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_"
                f"role_and_region_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_and_region_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_region_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"region_and_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"region_and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_region_and_time_"
                          f"zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"region_and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"region_and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_region_and_"
                          f"email_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_region_email_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"region_email_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"region_email_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_region_"
                          f"email_time_zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_and_"
                    f"password_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_and_"
                f"password_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_and_password_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"password_and_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"password_and_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_password_and_time_"
                          f"zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"password_and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"password_and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_password_and_email_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_email_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"password_email_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"password_email_time_zone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_password_email_"
                          f"time_zone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                    f"password_and_region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_"
                f"password_and_region_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_password_and_"
                          f"region_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_first_name_last_name_user_role_password_region_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_first_name_last_name_user_role_password_"
                    f"region_time_zone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_first_name_last_name_user_role_password_"
                f"region_time_zone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_first_name_last_name_user_role_password_region_time_zone_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_region_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_password_"
                    f"region_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_first_name_last_name_user_role_password_"
                f"region_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_first_name_last_name_user_role_password_region_email_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_first_name_last_name_user_role_password_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_first_name_last_name_user_role_password_region_"
                    f"email_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_first_name_last_name_user_role_password_region_"
                f"email_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_first_name_last_name_user_role_password_region_email_"
                          f"timezone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_and_last_name_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_first_name_last_name_user_role_password_"
                    f"region_email_timezone_save_display_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_first_name_last_name_user_role_password_"
                f"region_email_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_first_name_last_name_user_role_password_region_email_"
                          f"timezone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_"
                    f"timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_"
                f"timezone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_and_timezone_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_"
                    f"email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_"
                f"email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_and_email_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_email_timezone_"
                    f"save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_email_timezone_"
                f"save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_email_timezone_save_display_"
                          f"error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_"
                    f"region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_"
                f"region_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_and_region_save_display_"
                          f"error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_region_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_region_timezone_"
                    f"save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_region_timezone_"
                f"save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_region_timezone_save_display_"
                          f"error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            return self.validate_error_message()
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_region_and_email_"
                f"save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_region_and_email_save_display_"
                          f"error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_region_"
                    f"email_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_region_"
                f"email_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_region_email_timezone_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_"
                    f"name_and_password_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_"
                f"name_and_password_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_and_password_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_password_"
                    f"and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_password_"
                f"and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_password_and_email_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_password_email_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_password_email_"
                    f"and_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_password_email_"
                f"and_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_password_email_and_timezone_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_"
                    f"password_and_region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_"
                f"password_and_region_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_password_and_region_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_region_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_password_"
                    f"region_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_password_"
                f"region_timezone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_password_region_timezone_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_password_"
                    f"region_and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_password_"
                f"region_and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_password_region_and_email_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_password_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_password_region_"
                    f"email_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_password_region_"
                f"email_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_password_region_email_timezone_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_user_role_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_user_"
                    f"role_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_and_user_"
                f"role_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_and_user_role_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_"
                    f"role_and_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_"
                f"role_and_timezone_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_user_role_and_timezone_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_role_"
                    f"and_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_role_"
                f"and_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_user_role_and_"
                          f"email_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_email_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_email_"
                    f"and_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_email_"
                f"and_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_user_role_email_and_timezone_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_"
                    f"role_and_region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_"
                f"role_and_region_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_user_role_and_region_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_region_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_"
                    f"region_and_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_"
                f"region_and_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_user_role_region_and_"
                          f"timezone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_region_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_"
                    f"role_region_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user_"
                f"role_region_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_user_role_region_email_"
                          f"save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_region_email_"
                    f"timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_region_email_"
                f"timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_user_role_region_email_timezone_save_"
                          f"display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user"
                    f"_role_and_password_save_display_error_message_failed.png")

                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_user"
                f"_role_and_password_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_user_"
                          f"role_and_password_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_password_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_"
                    f"password_and_timezone_save_display_error_message_failed.png")

                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_role_"
                f"password_and_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_user_role_"
                          f"password_and_timezone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_password_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_"
                    f"user_role_password_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_fills_username_first_name_last_name_"
                f"user_role_password_email_save_display_error_message_failed.png")
            self.log.info(f"verify_user_fills_username_first_name_last_name_user_"
                          f"role_password_email_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_lastname_user_role_password_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_lastname_"
                    f"user_role_password_email_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_lastname_"
                f"user_role_password_email_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_lastname_user_role_password"
                          f"_email_timezone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_password_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_"
                    f"role_password_region_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_last_name_user_"
                f"role_password_region_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_last_name_user_role_password_"
                          f"region_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_firstname_lastname_user_role_password_region_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_firstname_lastname_user_role_"
                    f"password_region_timezone_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_firstname_lastname_user_role_"
                f"password_region_timezone_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_firstname_lastname_user_role_password_"
                          f"region_timezone_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_lastname_user_role_password_region_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_first_name_lastname_user_"
                    f"role_password_region_email_save_display_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_first_name_lastname_user_"
                f"role_password_region_email_save_display_error_message_failed.png")
            self.log.info(f"user_fills_username_first_name_lastname_user_role_password_"
                          f"region_email_save_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_firstname_lastname_user_role_password_region_email_timezone_display_success_msg(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)
            if self.validate_successful_message(user_name=username):
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_fills_username_firstname_lastname_user_role"
                    f"_password_region_email_timezone_display_success_msg_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_fills_username_firstname_lastname_user_role"
                f"_password_region_email_timezone_display_success_msg_failed.png")
            self.log.info(f"user_fills_username_firstname_lastname_user_role_password_region_"
                          f"email_timezone_display_success_msg_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_create_a_new_user_by_filling_only_mandatory_fields(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)
            if self.check_if_user_is_created(user_name=username):
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_create_a_new_user_by_filling_"
                    f"only_mandatory_fields_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_create_a_new_user_by_filling_"
                f"only_mandatory_fields_failed.png")
            self.log.info(f"verify_user_able_to_create_a_new_user_by_filling_only_mandatory_fields_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_the_mandatory_details_filled_for_the_newly_created_user(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)
            if self.check_if_users_able_to_see_mandatory_details(username, first_name, last_name, user_role, region,
                                                                 email, time_zone):
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_the_mandatory_details"
                    f"_filled_for_the_newly_created_user_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_the_mandatory_details"
                f"_filled_for_the_newly_created_user_failed.png")
            self.log.info(f"verify_user_able_to_see_the_mandatory_details_filled"
                          f"_for_the_newly_created_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_create_a_new_users_by_filling_all_the_fields(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            company = Read_Users_Components().company_input_data()
            self.enter_company(company)

            title = Read_Users_Components().title_input_data()
            self.enter_title(title)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            department = Read_Users_Components().department_input_data()
            self.enter_department(department)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            alert_email = Read_Users_Components().alert_email_input_data()
            self.enter_alert_email(alert_email)

            alert_phone_no = Read_Users_Components().alert_phone_no_input_data()
            self.enter_alert_phone_no(alert_phone_no)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            address = Read_Users_Components().address_input_data()
            self.enter_address(address)

            address2 = Read_Users_Components().address2_input_data()
            self.enter_address2(address2)

            city = Read_Users_Components().city_input_data()
            self.enter_city(city)

            state = Read_Users_Components().state_input_data()
            self.enter_state(state)

            postal_code = Read_Users_Components().postal_code_input_data()
            self.enter_postal_code(postal_code)

            home_ph_no = Read_Users_Components().home_phone_no_input_data()
            self.enter_home_ph_no(home_ph_no)

            work_ph_no = Read_Users_Components().work_phone_no_input_data()
            self.enter_work_ph_no(work_ph_no)

            fax_ph_no = Read_Users_Components().fax_phone_no_input_data()
            self.enter_fax_ph_no(fax_ph_no)

            phone_type = Read_Users_Components().phone_type_input_data()
            self.enter_phone_type(phone_type)

            phone_provider = Read_Users_Components().phone_provider_input_data()
            self.select_phone_provider(phone_provider)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_user_is_created(user_name=username):
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_create_a_new_users_by_"
                    f"filling_all_the_fields_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_create_a_new_users_by_filling_all_the_fields_failed.png")
            self.log.info(f"verify_user_able_to_create_a_new_users_by_filling_all_the_fields_failed: {ex}")
            return False

        finally:
            self.close_single_panel()

    def verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            company = Read_Users_Components().company_input_data()
            self.enter_company(company)

            title = Read_Users_Components().title_input_data()
            self.enter_title(title)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            department = Read_Users_Components().department_input_data()
            self.enter_department(department)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            alert_email = Read_Users_Components().alert_email_input_data()
            self.enter_alert_email(alert_email)

            alert_phone_no = Read_Users_Components().alert_phone_no_input_data()
            self.enter_alert_phone_no(alert_phone_no)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            address = Read_Users_Components().address_input_data()
            self.enter_address(address)

            address2 = Read_Users_Components().address2_input_data()
            self.enter_address2(address2)

            city = Read_Users_Components().city_input_data()
            self.enter_city(city)

            state = Read_Users_Components().state_input_data()
            self.enter_state(state)

            postal_code = Read_Users_Components().postal_code_input_data()
            self.enter_postal_code(postal_code)

            home_ph_no = Read_Users_Components().home_phone_no_input_data()
            self.enter_home_ph_no(home_ph_no)

            work_ph_no = Read_Users_Components().work_phone_no_input_data()
            self.enter_work_ph_no(work_ph_no)

            fax_ph_no = Read_Users_Components().fax_phone_no_input_data()
            self.enter_fax_ph_no(fax_ph_no)

            phone_type = Read_Users_Components().phone_type_input_data()
            self.enter_phone_type(phone_type)

            phone_provider = Read_Users_Components().phone_provider_input_data()
            self.select_phone_provider(phone_provider)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_users_able_to_see_all_details(user_name=username):
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_all_the_details_"
                    f"filled_for_the_newly_created_user_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_all_the_details_"
                f"filled_for_the_newly_created_user_failed.png")
            self.log.info(f"verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            self.select_disabled()
            self.select_enabled()

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)
            if self.check_if_user_marked_as_enabled():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_if_user_creates_a_new_users_marked_as_"
                    f"enabled_it_should_reflect_as_enabled_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_if_user_creates_a_new_users_marked_as_"
                f"enabled_it_should_reflect_as_enabled_failed.png")
            self.log.info(f"verify_if_user_creates_a_new_users_marked_as_enabled_it_"
                          f"should_reflect_as_enabled_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            self.select_disabled()

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)
            if self.check_if_user_marked_as_disabled():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_if_user_creates_a_new_users_marked_as_"
                    f"disabled_it_should_reflect_as_disabled_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_if_user_creates_a_new_users_marked_as_"
                f"disabled_it_should_reflect_as_disabled_failed.png")
            self.log.info(f"verify_if_user_creates_a_new_users_marked_as_disabled_it_"
                          f"should_reflect_as_disabled_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_the_alert_schedule_is_enabled_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)
            if self.check_if_alert_schedule_is_enabled():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_the_alert_schedule_is_enabled_after_creating_a_new_user_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_the_alert_schedule_is_enabled_after_creating_a_new_user_failed.png")
            self.log.info(f"verify_the_alert_schedule_is_enabled_after_creating_a_new_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_alert_schedule_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.verify_user_able_to_open_the_alert_schedule():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_open_the_alert_"
                    f"schedule_after_creating_a_new_user_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_open_the_alert_"
                f"schedule_after_creating_a_new_user_failed.png")
            self.log.info(f"verify_user_able_to_open_the_alert_schedule_after_creating_a_new_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_the_notification_groups_is_enabled_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_notification_groups_is_enabled():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_the_notification_groups_is_enabled_"
                    f"after_creating_a_new_user_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_the_notification_groups_is_enabled_"
                f"after_creating_a_new_user_failed.png")
            self.log.info(f"verify_the_notification_groups_is_enabled_after_creating_a_new_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_notification_groups_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.verify_user_able_to_open_the_notification_groups():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_open_the_notification_"
                    f"groups_after_creating_a_new_user_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_open_the_notification_"
                f"groups_after_creating_a_new_user_failed.png")
            self.log.info(f"verify_user_able_to_open_the_notification_groups_after_creating_a_new_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def user_able_to_see_the_newly_created_users_details_username_firstname_lastname_email_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.verify_user_details_under_users_panel():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(user_able_to_see_the_newly_created_users_details"
                    f"_username_firstname_lastname_email_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(user_able_to_see_the_newly_created_users_details"
                f"_username_firstname_lastname_email_under_users_panel_failed.png")
            self.log.info(f"user_able_to_see_the_newly_created_users_details_username_"
                          f"firstname_lastname_email_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_if_the_enabled_is_displayed_for_users_marked_as_enabled_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_users_marked_as_enabled_under_users_panel():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_if_the_enabled_is_displayed"
                    f"_for_users_marked_as_enabled_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_if_the_enabled_is_displayed"
                f"_for_users_marked_as_enabled_under_users_panel_failed.png")
            self.log.info(f"verify_user_able_to_see_if_the_enabled_is_displayed_for_users_marked"
                          f"_as_enabled_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_if_the_disabled_is_dispalyed_for_users_marked_as_disabled_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            time.sleep(Base_Class.one_second)
            self.select_disabled()
            time.sleep(Base_Class.one_second)
            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_users_marked_as_disabled_under_users_panel():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_if_the_disabled_is_dispalyed_"
                    f"for_users_marked_as_disabled_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_if_the_disabled_is_dispalyed_"
                f"for_users_marked_as_disabled_under_users_panel_failed.png")
            self.log.info(f"verify_user_able_to_see_if_the_disabled_is_dispalyed_for_users_marked_"
                          f"as_disabled_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_see_the_notification_groups_icon_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_notification_groups_icon():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_see_the_notification_groups_icon_for_the"
                    f"_newly_created_user_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_able_to_see_the_notification_groups_icon_for_the"
                f"_newly_created_user_under_users_panel_failed.png")
            self.log.info(f"verify_users_able_to_see_the_notification_groups_icon_for_the_newly_created"
                          f"_user_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_for_newly_created_user_the_hover_text_is_visible_for_notification_groups_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_hover_text_notification_groups_icon():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_for_newly_created_user_the_hover_text_is_visible_"
                    f"for_notification_groups_under_users_panel_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_for_newly_created_user_the_hover_text_is_visible_"
                f"for_notification_groups_under_users_panel_failed.png")
            self.log.info(f"verify_for_newly_created_user_the_hover_text_is_visible_for_notification_"
                          f"groups_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_notification_groups_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_notification_groups_can_be_opened():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_open_the_notification_groups_for"
                    f"_the_newly_created_user_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_open_the_notification_groups_for"
                f"_the_newly_created_user_under_users_panel_failed.png")
            self.log.info(f"verify_user_able_to_open_the_notification_groups_for_the_newly_"
                          f"created_user_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_the_details_icon_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_details_icon():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_the_details_icon_for_the_newly"
                    f"_created_user_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_the_details_icon_for_the_newly"
                f"_created_user_under_users_panel_failed.png")
            self.log.info(f"verify_user_able_to_see_the_details_icon_for_the_newly_created"
                          f"_user_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_that_for_the_newly_created_user_the_hover_text_is_visible_for_details_icon_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_hover_text_details_icon():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_that_for_the_newly_created_user_the_hover"
                    f"_text_is_visible_for_details_icon_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_that_for_the_newly_created_user_the_hover"
                f"_text_is_visible_for_details_icon_under_users_panel_failed.png")
            self.log.info(f"verify_that_for_the_newly_created_user_the_hover_text_is"
                          f"_visible_for_details_icon_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_details_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_details_can_be_opened():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_open_the_details_for_the_"
                    f"newly_created_user_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_open_the_details_for_the_"
                f"newly_created_user_under_users_panel_failed.png")
            self.log.info(f"verify_user_able_to_open_the_details_for_the_newly_created"
                          f"_user_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_the_alert_schedule_icon_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_alert_schedule_icon():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_see_the_alert_schedule_icon_"
                    f"for_the_newly_created_user_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_see_the_alert_schedule_icon_"
                f"for_the_newly_created_user_under_users_panel_failed.png")
            self.log.info(f"verify_user_able_to_see_the_alert_schedule_icon_for_the_newly_"
                          f"created_user_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_for_the_newly_created_user_the_hover_text_is_visible_for_alert_schedule_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_hover_text_alert_schedule():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_for_the_newly_created_user_the_hover_"
                    f"text_is_visible_for_alert_schedule_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_for_the_newly_created_user_the_hover_"
                f"text_is_visible_for_alert_schedule_under_users_panel_failed.png")
            self.log.info(f"verify_for_the_newly_created_user_the_hover_text_is_visible_"
                          f"for_alert_schedule_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_alert_schedule_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_alert_schedule_can_be_opened():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_open_the_alert_schedule_"
                    f"for_the_newly_created_user_under_users_panel_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_open_the_alert_schedule_"
                f"for_the_newly_created_user_under_users_panel_failed.png")
            self.log.info(f"verify_user_able_to_open_the_alert_schedule_for_the_newly_"
                          f"created_user_under_users_panel_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_edit_the_details_for_the_newly_created_user_details(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_users_able_to_edit_details():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_edit_the_details_for_"
                    f"the_newly_created_user_details_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_edit_the_details_for_"
                f"the_newly_created_user_details_failed.png")
            self.log.info(f"verify_user_able_to_edit_the_details_for_the_newly_created_user_details_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_delete_the_newly_created_user(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_users_able_to_delete_a_user():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_delete_the_newly_created_user_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_delete_the_newly_created_user_failed.png")
            self.log.info(f"verify_user_able_to_delete_the_newly_created_user_failed: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_should_not_be_able_to_create_user_which_already_exist(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_users_not_be_able_to_create_user_which_already_exist():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_should_not_be_able_to_create_"
                    f"user_which_already_exist_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_should_not_be_able_to_create_user_which_already_exist_failed.png")
            self.log.info(f"verify_user_should_not_be_able_to_create_user_which_already_exist_failed: {ex}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_should_not_be_able_to_create_user_if_password_and_confirm_password_does_not_match(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            confirm_passwrd = Read_Users_Components().confirm_password_data_input()
            self.enter_mis_match_password(password, confirm_passwrd)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)
            self.click_on_save_btn()
            time.sleep(Base_Class.two_second)

            if self.check_if_error_msg_displayed_for_password_mismatch():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_able_to_close_users_pane_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_able_to_close_users_pane_failed.png")
            self.log.info(f"verify_users_able_to_close_users_pane_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_cancel_the_user_creation_after_filling_all_the_details(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(Base_Class.two_second)

            if self.check_if_users_able_to_cancel():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_able_to_cancel_the_user"
                    f"_creation_after_filling_all_the_details_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_able_to_cancel_the_user"
                f"_creation_after_filling_all_the_details_failed.png")
            self.log.info(f"verify_user_able_to_cancel_the_user_creation_after_filling_all_the_details_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_when_user_close_user_panel_it_should_display_a_warning_popup(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(Base_Class.two_second)
            ex_pop_up = self.d.find_element(By.XPATH, Read_Users_Components().close_pop_up_by_xpath()).text.strip()
            ac_pop_up = Read_Users_Components().close_panel_pop_validation_text()
            if ex_pop_up == ac_pop_up:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_when_user_close_user_panel_it_should_"
                    f"display_a_warning_popup_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_when_user_close_user_panel_it_should_"
                f"display_a_warning_popup_failed.png")
            self.log.info(f"verify_when_user_close_user_panel_it_should_display_a_warning_popup_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_users_sees_go_back_and_close_panel_and_discard_changes_in_warning_popup(self):
        try:
            result = []
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(Base_Class.two_second)
            go_back = self.d.find_element(By.XPATH, Read_Users_Components().close_pop_up_go_back_btn_by_xpath())
            discard = self.d.find_element(By.XPATH, Read_Users_Components().close_panel_and_discard_changes_by_xpath())
            result.append(go_back.is_displayed())
            result.append(go_back.is_enabled())
            result.append(discard.is_displayed())
            result.append(discard.is_enabled())
            go_back.click()
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_users_sees_go_back_and_close_"
                    f"panel_and_discard_changes_in_warning_popup_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_users_sees_go_back_and_close_"
                f"panel_and_discard_changes_in_warning_popup_failed.png")
            self.log.info(
                f"verify_users_sees_go_back_and_close_panel_and_discard_changes_in_warning_popup_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_lands_on_the_same_panel_on_clicking_go_back(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            ex = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_title_by_xpath()).text
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(Base_Class.two_second)
            go_back = self.d.find_element(By.XPATH, Read_Users_Components().close_pop_up_go_back_btn_by_xpath())
            go_back.click()
            ac = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_title_by_xpath()).text
            if ex == ac:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_user_lands_on_the_same_panel_on_clicking_go_back_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_user_lands_on_the_same_panel_on_clicking_go_back_failed.png")
            self.log.info(f"verify_user_lands_on_the_same_panel_on_clicking_go_back_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_on_clicking_close_panel_and_discard_changes_user_panel_should_be_closed(self):
        try:
            self.login()
            time.sleep(Base_Class.two_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(Base_Class.two_second)
            ex = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_save_button_by_xpath()).text
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(Base_Class.two_second)
            discard = self.d.find_element(By.XPATH, Read_Users_Components().close_panel_and_discard_changes_by_xpath())
            discard.click()
            panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
            new_panel_count = len(panel_list)
            if new_panel_count == 1:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(verify_on_clicking_close_panel_and_"
                    f"discard_changes_user_panel_should_be_closed_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_on_clicking_close_panel_and_"
                f"discard_changes_user_panel_should_be_closed_failed.png")
            self.log.info(f"verify_on_clicking_close_panel_and_discard_changes_"
                          f"user_panel_should_be_closed_failed: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    ########################### Resuable Methods  #######################

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Users_Components().logout_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            logout_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(click_on_logout_button_failed.png")
            self.log.info(
                f"click_on_logout_button_failed: {ex}")
            return False

    def click_user_on_cloud_menu(self):
        """
        This function clicks on users on the cloud menu
        """
        users = self.d.find_element(By.XPATH, Read_Users_Components().users_cloud_menu_by_xpath())
        users.click()

    def click_on_action_btn(self):
        """
        clicks on action button
        """
        action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
        action_btn.click()

    def click_on_action_refresh_option(self):
        """
        clicks on refresh
        """
        self.click_on_action_btn()
        time.sleep(Base_Class.two_second)
        refresh = self.d.find_element(By.XPATH, Read_Users_Components().refresh_by_xpath())
        refresh.click()

    def click_on_action_create_user_option(self):
        """
        clicks on create user
        """
        self.click_on_action_btn()
        time.sleep(Base_Class.two_second)
        create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
        create_user.click()

    def click_on_action_delete_option(self):
        """
        clicks on delete selected user
        """
        self.click_on_action_btn()
        time.sleep(Base_Class.two_second)
        delete = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
        delete.click()
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH, Read_Users_Components().delete_confirmation_yes_by_xpath()).click()

    def click_on_save_btn(self):
        """
        clicks on save button
        """
        save = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_save_button_by_xpath())
        save.click()

    def click_on_cancel_btn(self):
        """
        clicks on cancel button
        """
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()

    def select_enabled(self):
        """
        selects enabled checkbox
        """
        checkbox = self.d.find_element(By.XPATH, Read_Users_Components().enabled_by_xpath())
        checkbox.click()

    def select_disabled(self):
        """
        selects disabled checkbox
        """
        checkbox = self.d.find_element(By.XPATH, Read_Users_Components().disabled_by_xpath())
        checkbox.click()

    def enter_user_name(self, user_name):
        """
        fills user name field
        :param user_name:
        """
        user_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_name_by_xpath())
        user_name_txt_bx.send_keys(user_name)

    def enter_first_name(self, first_name):
        """
        fills first name field
        :param first_name:
        """
        first_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().first_name_by_xpath())
        first_name_txt_bx.send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        fills last name field
        :param last_name:
        """
        last_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().last_name_by_xpath())
        last_name_txt_bx.send_keys(last_name)

    def select_user_role(self, role_data_text):
        """
        handles user role drop down using visible text of the element
        :param role_data_text:
        :return:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
        select_options_visible_text(user_role_ele, role_data_text)

    def enter_password(self, password):
        """
        fills password field
        :param password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
        confirm_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        confirm_password.send_keys(password)

    def enter_mis_match_password(self, password, confirm_password):
        """
        fills password field
        :param password:
        :param confirm_password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
        conf_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        conf_password.send_keys(confirm_password)

    def enter_company(self, company):
        company_ele = self.d.find_element(By.XPATH, Read_Users_Components().company_by_xpath())
        company_ele.send_keys(company)

    def enter_title(self, title):
        title_ele = self.d.find_element(By.XPATH, Read_Users_Components().title_by_xpath())
        title_ele.send_keys(title)

    def enter_department(self, department):
        department_ele = self.d.find_element(By.XPATH, Read_Users_Components().department_by_xpath())
        department_ele.send_keys(department)

    def validate_required_user_role_is_selected(self, required_option):
        """
        validate the user role provided is selected.
        :param required_option:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
        select = Select(user_role_ele)
        if select.first_selected_option.text == required_option:
            return True
        else:
            return False

    def select_region(self, region_text):
        """
        This function is used to handle the region drop-down and select the required options
        :param region_text:
        :return:
        """
        region_ele = self.d.find_element(By.XPATH, Read_Users_Components().region_by_xpath())
        region_ele.click()
        time.sleep(Base_Class.two_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Users_Components().region_list_by_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                actual_zone_text = region_text_list.__getitem__(i).text
                print(actual_zone_text)
                print(expected_region_text)
                if expected_region_text.upper() in actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Users_Components().region_save_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", save)
        except Exception as ex:
            str(ex)

    def validate_region(self, region_text):
        """
        validate the selected region is correct
        :param region_text:
        :return:
        """
        region_output = self.d.find_element(By.XPATH, Read_Users_Components().region_selected_by_xpath())
        return region_output.text.lower() in str(region_text).lower()

    def select_time_zone(self, use_value):
        """
        selects time zone using the value of the element
        :param use_value:
        :return:
        """
        time_zone = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
        select_options_value(time_zone, use_value)

    def enter_email(self, email):
        """
        fills email field
        :param email:
        """
        email_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
        email_txt_bx.send_keys(email)

    def enter_alert_email(self, alert_email):
        """
        fills email field
        :param alert_email:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_email_by_xpath())
        ele.send_keys(alert_email)

    def enter_alert_phone_no(self, alert_phone_no):
        """
        fills email field
        :param alert_phone_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_phone_number_by_xpath())
        ele.send_keys(alert_phone_no)

    def enter_address(self, address):
        """
        fills email field
        :param address:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().address_by_xpath())
        ele.send_keys(address)

    def enter_city(self, city):
        """
        fills email field
        :param city:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().city_by_xpath())
        ele.send_keys(city)

    def enter_state(self, state):
        """
        fills email field
        :param state:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().state_by_xpath())
        ele.send_keys(state)

    def enter_postal_code(self, postal_code):
        """
        fills email field
        :param postal_code:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().postal_code_by_xpath())
        ele.send_keys(postal_code)

    def enter_home_ph_no(self, home_ph_no):
        """
        fills email field
        :param home_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().home_phone_number_by_xpath())
        ele.send_keys(home_ph_no)

    def enter_work_ph_no(self, work_ph_no):
        """
        fills email field
        :param work_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().work_phone_number_by_xpath())
        ele.send_keys(work_ph_no)

    def enter_fax_ph_no(self, fax_ph_no):
        """
        fills email field
        :param fax_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().fax_phone_number_by_xpath())
        ele.send_keys(fax_ph_no)

    def enter_phone_type(self, phone_type):
        """
        fills email field
        :param phone_type:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().phone_type_by_xpath())
        ele.send_keys(phone_type)

    def enter_address2(self, address2):
        """
        fills email field
        :param address2:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().address2_by_xpath())
        ele.send_keys(address2)

    def select_phone_provider(self, phone_provider):
        ph_prov_bx = self.d.find_element(By.XPATH, Read_Users_Components().phone_provider_drop_dwn_by_xpath())
        select = Select(ph_prov_bx)
        select.select_by_visible_text(phone_provider)

    def validate_required_time_zone_is_selected(self, required_option):
        """
        checks if the required time zone is selected
        :param required_option:
        """
        time_zone_ele = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
        select = Select(time_zone_ele)
        selected_option = select.first_selected_option
        selected_value = selected_option.get_attribute("value")
        if selected_value == required_option:
            return True
        else:
            return False

    def validate_error_message(self):
        """
        checks if the error message "PLEASE NOTE: Required Fields Are Incomplete" is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Users_Components().error_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Users_Components().error_msg_validation_text())
        ac_result.append(ele.is_displayed())
        if ex_result == ac_result:
            return True
        else:
            return False

    def validate_successful_message(self, user_name):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Users_Components().success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_user_is_created(self, user_name):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Users_Components().success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(user_name)
        time.sleep(Base_Class.one_second)
        user = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath())
        ac_result.append(user_name == user.text)

        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_users_able_to_see_mandatory_details(self, ex_user_name, ex_first_name, ex_last_name, ex_user_role,
                                                     ex_region, ex_email, ex_time_zone):
        """
        checks if user details shows mandatory details that has been filled during the user creation process.
        """
        ex_result = [True, True, True, True, True, True, True]
        ac_result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        firstname = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text
        lastname = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text
        user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_details_user_role_by_xpath()).text
        region = self.d.find_element(By.XPATH, Read_Users_Components().user_details_region_by_xpath()).text
        email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        time_zone = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath()).text
        ac_result.append(True if ex_user_name == username else False)
        ac_result.append(True if ex_first_name == firstname else False)
        ac_result.append(True if ex_last_name == lastname else False)
        ac_result.append(True if ex_user_role == user_role.lower() else False)
        ac_result.append(True if region in ex_region else False)
        ac_result.append(True if ex_email == email else False)
        ac_result.append(True if ex_time_zone == time_zone else False)

        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_users_able_to_see_all_details(self, user_name):
        """
        checks if user details shows all details that has been filled during the user creation process.
        """
        ex_user_name = user_name
        ex_first_name = Read_Users_Components().first_name_input_data().strip()

        ex_last_name = Read_Users_Components().last_name_input_data().strip()

        ex_user_role = Read_Users_Components().user_role_input_data().strip()

        ex_company = Read_Users_Components().company_input_data().strip()

        ex_title = Read_Users_Components().title_input_data().strip()

        ex_region = Read_Users_Components().region_data_input()

        ex_department = Read_Users_Components().department_input_data().strip()

        ex_email = Read_Users_Components().email_input_data().strip()

        ex_alert_email = Read_Users_Components().alert_email_input_data().strip()

        ex_alert_phone_no = Read_Users_Components().alert_phone_no_input_data().strip()

        ex_time_zone = Read_Users_Components().time_zone_input_data().strip()

        ex_address = Read_Users_Components().address_input_data().strip()

        ex_address2 = Read_Users_Components().address2_input_data().strip()

        ex_city = Read_Users_Components().city_input_data().strip()

        ex_state = Read_Users_Components().state_input_data().strip()

        ex_postal_code = Read_Users_Components().postal_code_input_data().strip()

        ex_home_ph_no = Read_Users_Components().home_phone_no_input_data().strip()

        ex_work_ph_no = Read_Users_Components().work_phone_no_input_data().strip()

        ex_fax_ph_no = Read_Users_Components().fax_phone_no_input_data().strip()

        ac_user_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text

        ac_first_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text

        ac_last_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text

        ac_user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_details_user_role_by_xpath()).text

        ac_company = self.d.find_element(By.XPATH, Read_Users_Components().user_details_company_by_xpath()).text

        ac_title = self.d.find_element(By.XPATH, Read_Users_Components().user_details_title_by_xpath()).text

        ac_region = self.d.find_element(By.XPATH, Read_Users_Components().user_details_region_by_xpath()).text

        ac_department = self.d.find_element(By.XPATH, Read_Users_Components().user_details_department_by_xpath()).text

        ac_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text

        ac_alert_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_alert_email_by_xpath()).text

        ac_alert_phone_no = self.d.find_element(By.XPATH,
                                                Read_Users_Components().user_details_alert_ph_no_by_xpath()).text

        ac_time_zone = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath()).text

        ac_address = self.d.find_element(By.XPATH, Read_Users_Components().user_details_address_by_xpath()).text

        ac_address2 = self.d.find_element(By.XPATH, Read_Users_Components().user_details_address2_by_xpath()).text

        ac_city = self.d.find_element(By.XPATH, Read_Users_Components().user_details_city_by_xpath()).text

        ac_state = self.d.find_element(By.XPATH, Read_Users_Components().user_details_state_by_xpath()).text

        ac_postal_code = self.d.find_element(By.XPATH, Read_Users_Components().user_details_postal_code_by_xpath()).text

        ac_home_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_home_ph_no_by_xpath()).text

        ac_work_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_work_ph_no_by_xpath()).text

        ac_fax_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_fax_ph_no_by_xpath()).text

        ac_result = [True if ex_user_name == ac_user_name.strip() else False,
                     True if ex_first_name == ac_first_name.strip() else False,
                     True if ex_last_name == ac_last_name.strip() else False,
                     True if ex_user_role == ac_user_role.strip().lower() else False,
                     True if ex_company == ac_company.strip() else False,
                     True if ex_title == ac_title.strip() else False,
                     True if ac_region in ex_region else False,
                     True if ex_department == ac_department.strip() else False,
                     True if ex_email == ac_email.strip() else False,
                     True if ex_alert_email == ac_alert_email.strip() else False,
                     True if ex_alert_phone_no == ac_alert_phone_no.strip() else False,
                     True if ex_time_zone == ac_time_zone.strip() else False,
                     True if ex_address == ac_address.strip() else False,
                     True if ex_address2 == ac_address2.strip() else False,
                     True if ex_city == ac_city.strip() else False,
                     True if ex_state == ac_state.strip() else False,
                     True if ex_postal_code == ac_postal_code.strip() else False,
                     True if ex_home_ph_no == ac_home_ph_no.strip() else False,
                     True if ex_work_ph_no == ac_work_ph_no.strip() else False,
                     True if ex_fax_ph_no == ac_fax_ph_no.strip() else False]

        if False in ac_result:
            return False
        else:
            return True

    def check_if_user_marked_as_enabled(self):
        """
        checks if user marked as enabled in user panel(User details)
        """
        enabled = self.d.find_element(By.XPATH, Read_Users_Components().user_details_enabled_by_xpath())
        return enabled.is_displayed()

    def check_if_user_marked_as_disabled(self):
        """
        checks if user marked as disabled in user panel(User details)
        """

        disabled = self.d.find_element(By.XPATH, Read_Users_Components().users_details_disabled_by_xpath())
        return disabled.is_displayed()

    def check_if_alert_schedule_is_enabled(self):
        """
        checks if alert schedule is enabled when a new user is created.
        """
        alert_schedule_btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
        return alert_schedule_btn.is_enabled()

    def verify_user_able_to_open_the_alert_schedule(self):
        """
        checks if alert schedule panel pops up.
        """
        exp = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        alert_schedule_btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
        alert_schedule_btn.click()
        alert_panel_text = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath()).text
        act = alert_panel_text.replace("(", "").replace(")", "")
        return exp == act

    def check_if_notification_groups_is_enabled(self):
        """
        checks if notification groups is enabled when a new user is created.
        """
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        return notification_groups_btn.is_enabled()

    def verify_user_able_to_open_the_notification_groups(self):
        """
        checks if notification groups panel pops up.
        """
        exp = Read_Users_Components().notification_group_title_validation_text()
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        act = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_title_by_xpath()).text
        return exp == act

    def verify_user_details_under_users_panel(self):
        """
        check user details under users_panel
        1. username
        2. first name
        3. last name
        4. email
        """
        result = []
        ex_username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        first_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text
        last_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text
        ex_first_last_name = first_name + " " + last_name
        ex_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(ex_username)
        time.sleep(Base_Class.two_second)
        ac_username = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath()).text
        ac_first_last_name = self.d \
            .find_element(By.XPATH, Read_Users_Components().users_list_board_first_and_last_name_by_xpath()).text
        ac_email = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_email_by_xpath()).text
        result.append(ex_username == ac_username)
        result.append(ex_first_last_name == ac_first_last_name)
        result.append(ex_email == ac_email)
        return False not in result

    def check_users_marked_as_enabled_under_users_panel(self):
        """
        checks if user marked as enabled in Users panel.
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        enabled_list_board = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_enabled_by_xpath())
        return enabled_list_board.is_displayed()

    def check_users_marked_as_disabled_under_users_panel(self):
        """
        checks if user marked as disabled in Users panel.
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        disabled_list_board = self.d.find_element(By.XPATH,
                                                  Read_Users_Components().users_list_board_disabled_by_xpath())
        return disabled_list_board.is_displayed()

    def check_notification_groups_icon(self):
        """
        check notification groups icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        notification_groups_icon = self.d.find_element(By.XPATH,
                                                       Read_Users_Components().notification_group_icon_by_xpath())
        result.append(notification_groups_icon.is_displayed())
        result.append(notification_groups_icon.is_enabled())
        return False not in result

    def check_hover_text_notification_groups_icon(self):
        """
        checks hover text for notification groups icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_by_xpath())
        move_to_element(ele)
        time.sleep(Base_Class.one_second)
        exp = Read_Users_Components().notification_group_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        act = hover_ele.text.split(":")[0]
        result.append(exp == act)
        return False not in result

    def check_if_notification_groups_can_be_opened(self):
        """
        checks notification groups icon can be opened
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_by_xpath())
        ele.click()
        time.sleep(Base_Class.one_second)
        title = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_title_by_xpath()).text
        return Read_Users_Components().notification_group_title_validation_text() == title

    def check_details_icon(self):
        """
        check details icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        result.append(details_icon.is_displayed())
        result.append(details_icon.is_enabled())
        return False not in result

    def check_hover_text_details_icon(self):
        """
        checks hover text for details icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        move_to_element(details_icon)
        time.sleep(Base_Class.one_second)
        exp = Read_Users_Components().details_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        act = hover_ele.text
        result.append(exp == act)
        return False not in result

    def check_if_details_can_be_opened(self):
        """
        checks details icon can be opened and user panel should pop up
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        ele.click()
        time.sleep(Base_Class.one_second)
        title = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_title_by_xpath()).text
        return Read_Users_Components().user_panel_title_validation_text() == title

    def check_alert_schedule_icon(self):
        """
        check alert schedule icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        result.append(details_icon.is_displayed())
        result.append(details_icon.is_enabled())
        return False not in result

    def check_hover_text_alert_schedule(self):
        """
        checks hover text for alert schedule icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        alert_icon = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        move_to_element(alert_icon)
        time.sleep(Base_Class.one_second)
        exp = Read_Users_Components().alert_schedule_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        act = hover_ele.text
        result.append(exp == act)
        return False not in result

    def check_if_alert_schedule_can_be_opened(self):
        """
        checks Alert Schedule icon can be opened and alert panel should pop up.
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        ele.click()
        time.sleep(Base_Class.one_second)
        exp_title = username
        title = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath()).text
        act_title = title.replace("(", "").replace(")", "")
        exp_sub_title = Read_Users_Components().alert_panel_sub_title_validation_text()
        act_sub_title = self.d.find_element(By.XPATH,
                                            Read_Users_Components().alert_panel_sub_title_by_xpath()).text.strip()
        result.append(exp_title == act_title)
        result.append(exp_sub_title == act_sub_title)
        return False not in result

    def check_if_users_able_to_edit_details(self):
        """
        check if users able to edit details.
        """
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH, Read_Users_Components().user_details_action_btn()).click()
        self.d.find_element(By.XPATH, Read_Users_Components().user_details_action_edit_user()).click()
        time.sleep(Base_Class.one_second)
        email = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
        email.clear()
        exp_email = Read_Users_Components().update_email_input_data()
        email.send_keys(exp_email)
        self.click_on_save_btn()
        time.sleep(Base_Class.one_second)
        act_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        return exp_email == act_email

    def check_if_users_able_to_delete_a_user(self):
        """
        check if users able to delete a user
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(Base_Class.one_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components().users_check_box_by_xpath())
        check_box.click()
        time.sleep(Base_Class.two_second)
        self.click_on_action_delete_option()
        time.sleep(Base_Class.one_second)
        search_box.send_keys(username)
        time.sleep(Base_Class.two_second)
        msg = self.d.find_element(By.XPATH, Read_Users_Components().filter_message_by_xpath())
        result.append(msg.is_displayed())
        result.append(msg.text == Read_Users_Components().filter_msg_validation_text())
        return False not in result

    def check_users_not_be_able_to_create_user_which_already_exist(self):
        """
        check if users not be able to create user which already exist
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text

        self.click_on_action_create_user_option()
        time.sleep(Base_Class.two_second)

        self.enter_user_name(username)

        first_name = Read_Users_Components().first_name_input_data()
        self.enter_first_name(first_name)

        last_name = Read_Users_Components().last_name_input_data()
        self.enter_last_name(last_name)

        user_role = Read_Users_Components().user_role_input_data()
        self.select_user_role(user_role)

        password = Read_Users_Components().password_data_input()
        self.enter_password(password)

        region = Read_Users_Components().region_data_input()
        self.select_region(region)

        email = Read_Users_Components().email_input_data()
        self.enter_email(email)

        time_zone = Read_Users_Components().time_zone_input_data()
        self.select_time_zone(time_zone)

        time.sleep(Base_Class.two_second)
        self.click_on_save_btn()

        time.sleep(Base_Class.two_second)
        error_msg = self.d.find_element(By.XPATH, Read_Users_Components().user_name_exists_by_xpath())
        result.append(error_msg.is_displayed())
        result.append(error_msg.text == Read_Users_Components().user_name_exists_validation_text())
        return False not in result

    def check_if_error_msg_displayed_for_password_mismatch(self):
        """
        check if error msg displayed for password mismatch
        """
        result = []
        error_msg = self.d.find_element(By.XPATH, Read_Users_Components().password_mis_match_by_xpath())
        result.append(error_msg.is_displayed())
        result.append(error_msg.text == Read_Users_Components().password_mis_match_validation_text())
        return False not in result

    def check_if_users_able_to_cancel(self):
        """
        check if users able to cancel
        """
        panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
        new_panel_count = len(panel_list)
        return new_panel_count == 1

    def close_all_panel_one_by_one(self):
        try:
            time.sleep(Base_Class.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_one_by_one_list())

            for i in close_panel_list:
                i.click()
                time.sleep(Base_Class.one_second)
                if self.d.find_element(By.XPATH,
                                       Read_Users_Components().user_close_panel_and_discard_Changes()).is_displayed():
                    self.d.find_element(By.XPATH,
                                        Read_Users_Components().user_close_panel_and_discard_Changes()).click()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(close_all_panel_one_by_one_failed.png")

    def close_single_panel(self):
        try:
            time.sleep(Base_Class.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
            time.sleep(Base_Class.one_second)

            return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(close_all_panel_one_by_one_failed.png")
