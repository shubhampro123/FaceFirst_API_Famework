import time
from pathlib import Path
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from All_POM_Package.Portal_Menu_Module.Portal_Menu_POM import Portal_Menu_pom
from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.Excel_Config_Files import XLUtils
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Tags_Read_INI import Read_Tags_Components

# Test data from excel sheet
test_data = f"{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_Excel\\Test_Data_XLSX.xlsx"


class Tags_Module_pom:

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
            self.d.save_screenshot(f"{self.screenshots_path}\\tags_menu_login_failed.png")
            self.log.info(f"login_before:  {ex}")
            return False

    def create_tags_for_serious_event(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            self.login()
            result = []
            self.click_on_tags_menu()
            for r in range(3, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2)
                time.sleep(Base_Class.one_second)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_name)
                time.sleep(Base_Class.one_second)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()
                result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                serious_event_checkbox.click()
                time.sleep(Base_Class.one_second)
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                time.sleep(Base_Class.one_second)
                duplicate_tag = self.d.find_element(By.XPATH,
                                                    Read_Tags_Components().
                                                    tag_name_already_exists_validation_by_xpath())
                if duplicate_tag.is_displayed():
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().
                                                        close_panel_and_discard_changes_btn_by_xpath())
                    close_warning.click()
                    time.sleep(Base_Class.one_second)

                else:
                    success_msg = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().tag_create_success_msg_by_xpath())
                    tag_create_success_actual_validation_msg = success_msg.text
                    tag_create_success_expected_validation_msg = Read_Tags_Components(). \
                        create_tag_success_msg_expected()
                    result.append(tag_create_success_actual_validation_msg ==
                                  tag_create_success_expected_validation_msg)
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    time.sleep(Base_Class.one_second)
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\create_tags_for_serious_event_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\create_tags_for_serious_event_failed.png")
            self.log.info(f"create_tags_for_serious_event:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def create_tags_for_non_serious_event(self):
        rows = XLUtils.getRowCount(test_data, 'non_serious_event_tags_data')
        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            for r in range(3, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'non_serious_event_tags_data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_name)
                time.sleep(Base_Class.one_second)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()
                time.sleep(Base_Class.one_second)
                result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                time.sleep(Base_Class.one_second)
                duplicate_tag = self.d.find_element(By.XPATH,
                                                    Read_Tags_Components().
                                                    tag_name_already_exists_validation_by_xpath())
                if duplicate_tag.is_displayed():
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().
                                                        close_panel_and_discard_changes_btn_by_xpath())
                    close_warning.click()

                else:
                    success_msg = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().tag_create_success_msg_by_xpath())
                    tag_create_success_actual_validation_msg = success_msg.text
                    tag_create_success_expected_validation_msg = Read_Tags_Components(). \
                        create_tag_success_msg_expected()
                    assert tag_create_success_actual_validation_msg == tag_create_success_expected_validation_msg
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\create_tags_for_non_serious_event_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\create_tags_for_non_serious_event_failed.png")
            self.log.info(f"create_tags_for_non_serious_event:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def filter_serious_event_tags_varify_it(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')

        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            serious_event_tags_expected = []
            for r in range(2, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2)
                serious_event_tags_expected.insert(r - 1, tags_name)
                serious_event_tags_expected = [x.lower() for x in serious_event_tags_expected]
                serious_event_tags_expected.sort()
            filter_btn = self.d.find_element(By.XPATH, Read_Tags_Components().filter_btn_by_xpath())
            filter_btn.click()
            time.sleep(Base_Class.one_second)
            serious_event_filter = self.d.find_element(By.XPATH,
                                                       Read_Tags_Components().serious_event_filter_btn_by_xpath())
            serious_event_filter.click()
            time.sleep(Base_Class.one_second)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text
                tag.lower()
                serious_event_tags_name_list_actual.append(tag)
                serious_event_tags_name_list_actual = [x.lower() for x in serious_event_tags_name_list_actual]
                serious_event_tags_name_list_actual.sort()
            time.sleep(Base_Class.one_second)
            result.append(serious_event_tags_expected == serious_event_tags_name_list_actual)
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\filter_serious_event_tags_varify_it_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\filter_serious_event_tags_varify_it_failed.png")
            self.log.info(f"filter_serious_event_tags_varify_it:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def filter_non_serious_event_tags_varify_it(self):
        rows = XLUtils.getRowCount(test_data, 'non_serious_event_tags_data')
        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            non_serious_event_tags_expected = []
            for r in range(2, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'non_serious_event_tags_data', r, 2)
                non_serious_event_tags_expected.insert(r - 1, tags_name)
                non_serious_event_tags_expected = [x.lower() for x in non_serious_event_tags_expected]
                non_serious_event_tags_expected.sort()
            non_serious_event_tags_expected = non_serious_event_tags_expected[
                                              1:len(non_serious_event_tags_expected) + 1]
            filter_dropdown = self.d.find_element(By.XPATH, Read_Tags_Components().filter_dropdown_by_xpath())
            filter_dropdown.click()
            time.sleep(Base_Class.one_second)
            non_serious_ele = self.d.find_element(By.XPATH, Read_Tags_Components().non_serious_element_by_xpath())
            non_serious_ele.click()
            time.sleep(Base_Class.one_second)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text.strip()
                tag = tag.lower()
                serious_event_tags_name_list_actual.append(tag)
            serious_event_tags_name_list_actual = serious_event_tags_name_list_actual[
                                                  1:len(serious_event_tags_name_list_actual) + 1]
            serious_event_tags_name_list_actual = [x.lower() for x in serious_event_tags_name_list_actual]
            serious_event_tags_name_list_actual.sort()
            time.sleep(Base_Class.one_second)
            result.append(non_serious_event_tags_expected == serious_event_tags_name_list_actual)
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\filter_non_serious_event_tags_varify_it_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\filter_non_serious_event_tags_varify_it_failed.png")
            self.log.info(f"filter_non_serious_event_tags_varify_it_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def duplicate_tags_not_create_validation(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            for r in range(2, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_name)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()
                result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                serious_event_checkbox.click()
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                try:
                    tag_name_already_exists = self.d.find_element(By.XPATH,
                                                                  Read_Tags_Components().
                                                                  tag_name_already_exists_validation_by_xpath())
                    actual_duplicate_tag_validation_msg = tag_name_already_exists.text
                    expected_duplicate_tag_validation_msg = Read_Tags_Components(). \
                        expected_duplicate_tag_validation_msg()
                    if tag_name_already_exists.is_displayed():
                        result.append(actual_duplicate_tag_validation_msg == expected_duplicate_tag_validation_msg)
                        close_panel = self.d.find_element(By.XPATH,
                                                          Read_Tags_Components().close_create_tag_panel_by_xpath())
                        close_panel.click()
                        close_panel_and_discard_changes_btn = self.d \
                            .find_element(By.XPATH,
                                          Read_Tags_Components().
                                          close_panel_and_discard_changes_btn_by_xpath())
                        close_panel_and_discard_changes_btn.click()
                    else:
                        close_panel = self.d.find_element(By.XPATH,
                                                          Read_Tags_Components().close_create_tag_panel_by_xpath())
                        close_panel.click()
                except Exception as ex:
                    self.log.info(f"duplicate_tags_not_create_validation_failed:  {ex}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\duplicate_tags_not_create_validation_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\duplicate_tags_not_create_validation_failed.png")
            self.log.info(f"duplicate_tags_not_create_validation_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def update_serious_event_tag_name(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            exp_tag_name = []
            tags_name = []
            for r in range(2, rows + 1):
                exp_tag_name.insert(r - 2, XLUtils.read_data(test_data, 'serious_event_tags_data', r, 3))
            for r in range(2, rows + 1):
                tags_name.insert(r - 2, XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2))
            exp_tag_name = exp_tag_name[1:len(exp_tag_name) + 1]
            tags_name = tags_name[1:len(tags_name) + 1]
            filter_btn = self.d.find_element(By.XPATH, Read_Tags_Components().filter_btn_by_xpath())
            filter_btn.click()
            serious_event_filter = self.d.find_element(By.XPATH,
                                                       Read_Tags_Components().serious_event_filter_btn_by_xpath())
            serious_event_filter.click()
            time.sleep(Base_Class.one_second)
            edit_btn_list = self.d.find_elements(By.XPATH,
                                                 Read_Tags_Components().tags_edit_button_by_xpath())
            time.sleep(Base_Class.one_second)
            for i in range(0, len(edit_btn_list)):
                try:
                    ac_tg_name = str(tags_name[i]).lower().strip()
                    ele = self.d.find_element(By.XPATH, "//p[normalize-space(text())='" + str(
                        ac_tg_name) + "']/following-sibling::div[@class='right-margin-menu']/descendant::div["
                                      "@data-toggle='tooltip']")
                    self.d.execute_script("arguments[0].click();", ele)
                    time.sleep(Base_Class.one_second)
                    action_btn = self.d.find_element(By.XPATH,
                                                     Read_Tags_Components().edit_tag_action_btn_by_xpath())
                    self.d.execute_script("arguments[0].click();", action_btn)
                    time.sleep(Base_Class.one_second)
                except Exception as ex:
                    self.log.info(f"update_serious_event_tag_name_failed:  {ex}")
                edit_btn = self.d.find_element(By.XPATH, Read_Tags_Components().edit_btn_by_xpath())
                self.d.execute_script("arguments[0].click();", edit_btn)
                time.sleep(Base_Class.one_second)
                tag_name_field = self.d.find_element(By.XPATH,
                                                     Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name_field.send_keys(Keys.CONTROL, 'a')
                tag_name_field.send_keys(Keys.DELETE)
                tag_name_field.send_keys(exp_tag_name[i])
                time.sleep(Base_Class.one_second)
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                time.sleep(Base_Class.one_second)
                updated_tags = self.d.find_element(By.XPATH, Read_Tags_Components().update_tag_validation())
                result.append(updated_tags.text.lower() == str(exp_tag_name[i]).lower())
                time.sleep(Base_Class.one_second)
                close_panel = self.d.find_element(By.XPATH,
                                                  Read_Tags_Components().close_create_tag_panel_by_xpath())
                close_panel.click()
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\update_serious_event_tag_name_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\update_serious_event_tag_name_failed.png")
            self.log.info(f"update_serious_event_tag_name_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def delete_all_tags(self):
        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            time.sleep(Base_Class.one_second)
            tags_checkbox = self.d.find_elements(By.XPATH,
                                                 Read_Tags_Components().tag_select_checkbox_list_by_xpath())
            try:
                for i in range(2, len(tags_checkbox)):
                    tags_checkbox[i].click()
            except Exception as ex:
                self.log.info(f"delete_all_tags:  {ex}")
            time.sleep(Base_Class.one_second)
            action_button = self.d.find_element(By.XPATH, Read_Tags_Components().tags_action_btn_by_xpath())
            action_button.click()
            time.sleep(Base_Class.one_second)
            delete_btn = self.d.find_element(By.XPATH,
                                             Read_Tags_Components().delete_btn_by_xpath())
            delete_btn.click()
            time.sleep(Base_Class.one_second)
            delete_yes_btn = self.d.find_element(By.XPATH,
                                                 Read_Tags_Components().yes_delete_selected())
            delete_yes_btn.click()
            time.sleep(Base_Class.two_second)
            tags_checkbox = self.d.find_elements(By.XPATH,
                                                 Read_Tags_Components().tag_select_checkbox_list_by_xpath())
            result.append(tags_checkbox.__len__() < 3)
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\delete_all_tags_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\delete_all_tags_failed.png")
            self.log.info(f"delete_all_tags_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_deterred_tag_is_present_at_first(self):
        try:
            result = []
            self.login()
            self.click_on_tags_menu()
            deterred_tag = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            actual_deterred_tag = deterred_tag[0].text
            expected_deterred_tag = Read_Tags_Components().expected_deterred_tag()
            result.append(actual_deterred_tag.lower() == expected_deterred_tag.lower())
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\verify_deterred_tag_is_present_at_first_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\verify_deterred_tag_is_present_at_first_failed.png")
            self.log.info(f"verify_deterred_tag_is_present_at_first_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def tags_search_functionality(self):
        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            search_box = self.d.find_element(By.XPATH, Read_Tags_Components().tags_search_field_by_xpath())
            search_box.send_keys(Read_Tags_Components().tag_search_input())
            time.sleep(Base_Class.one_second)
            search_result = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            actual_tag_result = search_result[0].text
            expected_tag_result = Read_Tags_Components().tag_search_result_expected()
            result.append(actual_tag_result == expected_tag_result)
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\tags_search_functionality_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tags_search_functionality_failed.png")
            self.log.info(f"tags_search_functionality:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def close_panel_and_discard_changes_verify(self):
        try:
            self.login()
            self.click_on_tags_menu()
            result = []
            action_button = self.d.find_element(By.XPATH, Read_Tags_Components().close_and_discard_panel_btn())
            action_button.click()
            time.sleep(Base_Class.one_second)
            create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
            create_button.click()
            time.sleep(Base_Class.one_second)
            tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
            tag_name.send_keys(Read_Tags_Components().close_panel_and_discard_changes_input())
            close_panel = self.d.find_element(By.XPATH, Read_Tags_Components().close_create_tag_panel_by_xpath())
            close_panel.click()
            time.sleep(Base_Class.one_second)
            warning_msg = self.d.find_element(By.XPATH,
                                              Read_Tags_Components().expected_discard_changes_warning_by_xpath())
            actual_warning_msg = warning_msg.text
            excepted_warning_msg = Read_Tags_Components().expected_discard_changes_warning()
            assert actual_warning_msg == excepted_warning_msg
            uncommitted_changes_msg = self.d.find_element(By.XPATH,
                                                          Read_Tags_Components().
                                                          expected_uncommitted_changes_msg_by_xpath())
            time.sleep(Base_Class.one_second)
            actual_uncommitted_changes_msg = uncommitted_changes_msg.text
            excepted_uncommitted_changes_msg = Read_Tags_Components().expected_uncommitted_changes_msg()
            result.append(actual_uncommitted_changes_msg == excepted_uncommitted_changes_msg)
            close_panel_btn = self.d.find_element(By.XPATH,
                                                  Read_Tags_Components().close_panel_btn_text_validation())
            actual_close_panel_btn_text = close_panel_btn.text
            excepted_close_panel_btn_text = Read_Tags_Components().expected_close_panel_btn_text()
            result.append(actual_close_panel_btn_text == excepted_close_panel_btn_text)
            close_panel_and_discard_changes_btn = self.d.find_element(By.XPATH,
                                                                      Read_Tags_Components().
                                                                      close_panel_and_discard_changes_btn_by_xpath())
            close_panel_and_discard_changes_btn.click()
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\close_panel_and_discard_changes_verify_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_panel_and_discard_changes_verify_failed.png")
            self.log.info(f"close_panel_and_discard_changes_verify_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def create_tags_for_serious_event_without_login(self):
        rows = XLUtils.getRowCount(test_data, 'Tags_Data')
        try:
            result = []
            for r in range(3, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'Tags_Data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                action_button.click()
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_name)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()
                result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                serious_event_checkbox.click()
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                duplicate_tag = self.d.find_element(By.XPATH,
                                                    Read_Tags_Components().
                                                    tag_name_already_exists_validation_by_xpath())
                if duplicate_tag.is_displayed():
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().
                                                        close_panel_and_discard_changes_btn_by_xpath())
                    close_warning.click()
                else:
                    success_msg = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                    result.append(success_msg.is_displayed())
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\"
                                       f"create_tags_for_serious_event_without_login_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\create_tags_for_serious_event_without_login_failed.png")
            self.log.info(f"create_tags_for_serious_event_without_login_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def close_all_panel(self):
        try:
            cloud_menu_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_cloud_menu_btn_by_xpath())
            cloud_menu_button.click()
            closed_all_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_closed_all_btn_by_xpath())
            closed_all_button.click()
            return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_failed.png")
            self.log.info(f"close_all_panel_failed:  {ex}")
            return False

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH, Read_Portal_Menu_Components().close_all_panel_list())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed:  {ex}")

    def click_on_tags_menu(self):
        tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
        tags_button.click()

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()). \
                is_displayed():
            self.login_before()

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Tags_Components().logout_btn_by_xpath())
            logout_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\Button_not_clickable_logout_pg_03.png")
            self.log.info(f"logout:  {ex}")
            return False
