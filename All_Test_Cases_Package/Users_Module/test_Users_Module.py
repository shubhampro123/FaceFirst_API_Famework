from pathlib import Path

import pytest

from All_POM_Package.Users_Module.Users_Module_POM import Users_Module_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Users_Module(Base_Class):
    logger = Base_Class.logger_object()

    def setup_method(self):
        try:
            print("\n setup start")
            self.d = Base_Class.d
            self.d.maximize_window()
            self.d.set_page_load_timeout(50)
            self.d.set_script_timeout(30)
            self.d.implicitly_wait(30)
            self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
            print("\nsetup end")

        except Exception as ex:
            print("\nException in Test_Users_Module_Test_Cases/setup_method: ", ex)

    @pytest.mark.p2
    def test_TC_US_001(self):
        self.logger.info("Users module = test_TC_US_001 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_view_the_user_on_cloud_menu():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_001.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_002(self):
        self.logger.info("Users module = test_TC_US_002 execution started..")
        if Users_Module_pom(self.logger).verify_user_opens_user_then_users_panel_should_display():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_002.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_003(self):
        self.logger.info("Users module = test_TC_US_003 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_and_open_action_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_003.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_004(self):
        self.logger.info("Users module = test_TC_US_004 execution started..")
        if Users_Module_pom(self.logger).verify_users_able_to_see_refresh():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_004.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_005(self):
        self.logger.info("Users module = test_TC_US_005 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_create_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_005.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_006(self):
        self.logger.info("Users module = test_TC_US_006 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_delete_selected_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_006.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_007(self):
        self.logger.info("Users module = test_TC_US_007 execution started..")
        if Users_Module_pom(self.logger).verify_user_clicks_refresh_then_it_should_refresh_the_users_list():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_007.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_008(self):
        self.logger.info("Users module = test_TC_US_008 execution started..")
        if Users_Module_pom(self.logger).verify_user_clicks_create_user_user_panel_should_be_displayed():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_008.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_009(self):
        self.logger.info("Users module = test_TC_US_009 execution started..")
        if Users_Module_pom(self.logger).verify_title_new_user_details_face_first_is_visible():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_009.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_010(self):
        self.logger.info("Users module = test_TC_US_010 execution started..")
        if Users_Module_pom(self.logger).verify_cancel_and_save_button_is_present():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_010.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_011(self):
        self.logger.info("Users module = test_TC_US_011 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_username_required_text_for_username():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_011.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_012(self):
        self.logger.info("Users module = test_TC_US_012 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_user_role_required_text_for_user_role():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_012.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_013(self):
        self.logger.info("Users module = test_TC_US_013 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_see_password_required_and_confirm_password_required_text_for_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_013.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_014(self):
        self.logger.info("Users module = test_TC_US_014 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_region_required_text_for_region():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_014.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_015(self):
        self.logger.info("Users module = test_TC_US_015 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_email_required_text_for_email():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_015.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_016(self):
        self.logger.info("Users module = test_TC_US_016 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_timezone_required_text_for_timezone():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_016.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_017(self):
        self.logger.info("Users module = test_TC_US_017 execution started..")
        if Users_Module_pom(self.logger).verify_enabled_checkbox_is_selected():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_017.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_018(self):
        self.logger.info("Users module = test_TC_US_018 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_select_disabled_checkbox():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_018.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_019(self):
        self.logger.info("Users module = test_TC_US_019 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_username_textbox_and_fill_username():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_019.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_020(self):
        self.logger.info("Users module = test_TC_US_020 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_first_name_textbox_and_fill_first_name():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_020.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_021(self):
        self.logger.info("Users module = test_TC_US_021 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_last_name_textbox_and_fill_last_name():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_021.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_022(self):
        self.logger.info("Users module = test_TC_US_022 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_user_role_dropdown_is_present_and_choose_the_user_roles():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_022.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_023(self):
        self.logger.info("Users module = test_TC_US_023 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_password_textbox_and_fill_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_023.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_024(self):
        self.logger.info("Users module = test_TC_US_024 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_company_textbox_and_enter_their_company_name():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_024.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_025(self):
        self.logger.info("Users module = test_TC_US_025 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_title_textbox_and_enter_title():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_025.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_026(self):
        self.logger.info("Users module = test_TC_US_026 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_region_popup_and_choose_a_region():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_026.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_027(self):
        self.logger.info("Users module = test_TC_US_027 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_department_textbox_and_enter_their_department_name():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_027.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_028(self):
        self.logger.info("Users module = test_TC_US_028 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_email_textbox_and_enter_a_valid_email():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_028.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_029(self):
        self.logger.info("Users module = test_TC_US_029 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_alert_email_and_enter_a_valid_alert_email():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_029.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_030(self):
        self.logger.info("Users module = test_TC_US_030 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_alert_phone_number_and_enter_a_valid_phone_number():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_030.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_031(self):
        self.logger.info("Users module = test_TC_US_031 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_timezone_dropdown_and_select_a_timezone():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_031.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_032(self):
        self.logger.info("Users module = test_TC_US_032 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_address_textbox_and_enter_their_address():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_032.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_033(self):
        self.logger.info("Users module = test_TC_US_033 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_address_2_textbox_and_enter_their_address():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_033.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_034(self):
        self.logger.info("Users module = test_TC_US_034 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_city_textbox_and_fill_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_034.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_035(self):
        self.logger.info("Users module = test_TC_US_035 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_state_textbox_and_fill_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_035.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_036(self):
        self.logger.info("Users module = test_TC_US_036 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_postal_code_textbox_and_fill_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_036.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_037(self):
        self.logger.info("Users module = test_TC_US_037 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_house_phone_number_textbox_and_enter_a_valid_phone_number():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_037.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_038(self):
        self.logger.info("Users module = test_TC_US_038 execution started..")
        if Users_Module_pom(self.logger).verify_users_able_to_see_work_phone_number_textbox_and_enter_a_valid_work_phone_number():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_038.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_039(self):
        self.logger.info("Users module = test_TC_US_039 execution started..")
        if Users_Module_pom(self.logger).verify_users_able_to_see_fax_phone_number_textbox_and_fill_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_039.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_040(self):
        self.logger.info("Users module = test_TC_US_040 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_phone_type_textbox_and_fill_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_040.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_041(self):
        self.logger.info("Users module = test_TC_US_041 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_phone_provider_dropdown_and_select_the_required_phone_provider():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_041.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_042(self):
        self.logger.info("Users module = test_TC_US_042 execution started..")
        if Users_Module_pom(self.logger).verify_alert_schedule_is_disabled():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_042.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_043(self):
        self.logger.info("Users module = test_TC_US_043 execution started..")
        if Users_Module_pom(self.logger).verify_notification_groups_is_disabled():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_043.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_044(self):
        self.logger.info("Users module = test_TC_US_044 execution started..")
        if Users_Module_pom(self.logger).verify_users_able_to_close_user_panel_on_clicking_cancel_button():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_044.png")
            assert False

    @pytest.mark.p2
    def test_TC_US_045(self):
        self.logger.info("Users module = test_TC_US_045 execution started..")
        if Users_Module_pom(self.logger).verify_users_able_to_close_users_pane():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_045.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_046(self):
        self.logger.info("Users module = test_TC_US_046 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_and_last_name_then_save_should_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_046.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_047(self):
        self.logger.info("Users module = test_TC_US_047 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_047.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_048(self):
        self.logger.info("Users module = test_TC_US_048 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_048.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_049(self):
        self.logger.info("Users module = test_TC_US_049 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_email_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_049.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_050(self):
        self.logger.info("Users module = test_TC_US_050 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_and_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_050.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_051(self):
        self.logger.info("Users module = test_TC_US_051 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_region_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_051.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_052(self):
        self.logger.info("Users module = test_TC_US_052 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_region_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_052.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_053(self):
        self.logger.info("Users module = test_TC_US_053 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_region_email_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_053.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_054(self):
        self.logger.info("Users module = test_TC_US_054 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_and_password_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_054.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_055(self):
        self.logger.info("Users module = test_TC_US_055 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_mame_last_name_password_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_055.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_056(self):
        self.logger.info("Users module = test_TC_US_056 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_password_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_056.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_057(self):
        self.logger.info("Users module = test_TC_US_057 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_password_email_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_057.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_058(self):
        self.logger.info("Users module = test_TC_US_058 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_password_and_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_058.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_059(self):
        self.logger.info("Users module = test_TC_US_059 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_password_region_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_059.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_060(self):
        self.logger.info("Users module = test_TC_US_060 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_password_region_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_060.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_061(self):
        self.logger.info("Users module = test_TC_US_061 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_last_name_password_region_email_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_061.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_062(self):
        self.logger.info("Users module = test_TC_US_062 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_first_name_last_name_and_user_role_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_062.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_063(self):
        self.logger.info("Users module = test_TC_US_063 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_063.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_064(self):
        self.logger.info("Users module = test_TC_US_064 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_064.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_065(self):
        self.logger.info("Users module = test_TC_US_065 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_email_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_065.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_066(self):
        self.logger.info("Users module = test_TC_US_066 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_and_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_066.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_067(self):
        self.logger.info("Users module = test_TC_US_067 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_region_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_067.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_068(self):
        self.logger.info("Users module = test_TC_US_068 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_region_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_068.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_069(self):
        self.logger.info("Users module = test_TC_US_069 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_region_email_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_069.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_070(self):
        self.logger.info("Users module = test_TC_US_070 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_and_password_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_070.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_071(self):
        self.logger.info("Users module = test_TC_US_071 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_password_and_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_071.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_072(self):
        self.logger.info("Users module = test_TC_US_072 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_password_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_072.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_073(self):
        self.logger.info("Users module = test_TC_US_073 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_password_email_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_073.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_074(self):
        self.logger.info("Users module = test_TC_US_074 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_password_and_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_074.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_075(self):
        self.logger.info("Users module = test_TC_US_075 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_first_name_last_name_user_role_password_region_time_zone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_075.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_076(self):
        self.logger.info("Users module = test_TC_US_076 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_first_name_last_name_user_role_password_region_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_076.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_077(self):
        self.logger.info("Users module = test_TC_US_077 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_first_name_last_name_user_role_password_region_email_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_077.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_078(self):
        self.logger.info("Users module = test_TC_US_078 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_username_first_name_and_last_name_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_078.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_079(self):
        self.logger.info("Users module = test_TC_US_079 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_username_first_name_last_name_and_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_079.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_080(self):
        self.logger.info("Users module = test_TC_US_080 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_username_first_name_last_name_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_080.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_081(self):
        self.logger.info("Users module = test_TC_US_081 execution started..")
        if Users_Module_pom(self.logger).user_fills_username_first_name_last_name_email_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_081.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_082(self):
        self.logger.info("Users module = test_TC_US_082 execution started..")
        if Users_Module_pom(self.logger).verify_user_fills_username_first_name_last_name_and_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_082.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_083(self):
        self.logger.info("Users module = test_TC_US_083 execution started..")
        if Users_Module_pom(self.logger).user_fills_username_first_name_last_name_region_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_083.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_084(self):
        self.logger.info("Users module = test_TC_US_084 execution started..")
        if Users_Module_pom(self.logger).user_fills_username_first_name_last_name_region_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_084.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_085(self):
        self.logger.info("Users module = test_TC_US_085 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_region_email_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_085.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_086(self):
        self.logger.info("Users module = test_TC_US_086 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_and_password_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_086.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_087(self):
        self.logger.info("Users module = test_TC_US_087 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_and_password_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_087.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_088(self):
        self.logger.info("Users module = test_TC_US_088 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_password_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_088.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_089(self):
        self.logger.info("Users module = test_TC_US_089 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_password_email_and_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_089.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_090(self):
        self.logger.info("Users module = test_TC_US_090 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_password_and_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_090.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_091(self):
        self.logger.info("Users module = test_TC_US_091 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_password_region_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_091.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_092(self):
        self.logger.info("Users module = test_TC_US_092 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_password_region_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_092.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_093(self):
        self.logger.info("Users module = test_TC_US_093 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_password_region_email_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_093.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_094(self):
        self.logger.info("Users module = test_TC_US_094 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_and_user_role_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_094.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_095(self):
        self.logger.info("Users module = test_TC_US_095 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_user_role_and_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_095.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_096(self):
        self.logger.info("Users module = test_TC_US_096 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_user_role_and_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_096.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_097(self):
        self.logger.info("Users module = test_TC_US_097 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_user_role_email_and_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_097.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_098(self):
        self.logger.info("Users module = test_TC_US_098 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_user_role_and_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_098.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_099(self):
        self.logger.info("Users module = test_TC_US_099 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_user_role_region_and_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_099.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_100(self):
        self.logger.info("Users module = test_TC_US_100 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_user_role_region_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_100.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_101(self):
        self.logger.info("Users module = test_TC_US_101 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_user_role_region_email_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_101.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_102(self):
        self.logger.info("Users module = test_TC_US_102 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_user_role_and_password_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_102.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_103(self):
        self.logger.info("Users module = test_TC_US_103 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_user_role_password_and_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_103.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_104(self):
        self.logger.info("Users module = test_TC_US_104 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_fills_username_first_name_last_name_user_role_password_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_104.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_105(self):
        self.logger.info("Users module = test_TC_US_105 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_lastname_user_role_password_email_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_105.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_106(self):
        self.logger.info("Users module = test_TC_US_106 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_last_name_user_role_password_region_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_106.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_107(self):
        self.logger.info("Users module = test_TC_US_107 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_firstname_lastname_user_role_password_region_timezone_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_107.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_108(self):
        self.logger.info("Users module = test_TC_US_108 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_first_name_lastname_user_role_password_region_email_save_display_error_message():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_108.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_109(self):
        self.logger.info("Users module = test_TC_US_109 execution started..")
        if Users_Module_pom(self.logger) \
                .user_fills_username_firstname_lastname_user_role_password_region_email_timezone_display_success_msg():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_109.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_110(self):
        self.logger.info("Users module = test_TC_US_110 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_create_a_new_user_by_filling_only_mandatory_fields():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_110.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_111(self):
        self.logger.info("Users module = test_TC_US_111 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_the_mandatory_details_filled_for_the_newly_created_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_111.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_112(self):
        self.logger.info("Users module = test_TC_US_112 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_create_a_new_users_by_filling_all_the_fields():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_112.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_113(self):
        self.logger.info("Users module = test_TC_US_113 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_113.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_114(self):
        self.logger.info("Users module = test_TC_US_114 execution started..")
        if Users_Module_pom(self.logger).verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_114.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_115(self):
        self.logger.info("Users module = test_TC_US_115 execution started..")
        if Users_Module_pom(self.logger).verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_115.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_116(self):
        self.logger.info("Users module = test_TC_US_116 execution started..")
        if Users_Module_pom(self.logger).verify_the_alert_schedule_is_enabled_after_creating_a_new_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_116.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_117(self):
        self.logger.info("Users module = test_TC_US_117 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_open_the_alert_schedule_after_creating_a_new_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_117.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_118(self):
        self.logger.info("Users module = test_TC_US_118 execution started..")
        if Users_Module_pom(self.logger).verify_the_notification_groups_is_enabled_after_creating_a_new_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_118.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_119(self):
        self.logger.info("Users module = test_TC_US_119 execution started..")
        if Users_Module_pom(self.logger).verify_user_able_to_open_the_notification_groups_after_creating_a_new_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_119.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_120(self):
        self.logger.info("Users module = test_TC_US_120 execution started..")
        if Users_Module_pom(self.logger) \
                .user_able_to_see_the_newly_created_users_details_username_firstname_lastname_email_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_120.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_121(self):
        self.logger.info("Users module = test_TC_US_121 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_see_if_the_enabled_is_displayed_for_users_marked_as_enabled_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_121.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_122(self):
        self.logger.info("Users module = test_TC_US_122 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_see_if_the_disabled_is_dispalyed_for_users_marked_as_disabled_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_122.png")
            assert False

    @pytest.mark.p1
    def test_TC_US_123(self):
        self.logger.info("Users module = test_TC_US_123 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_users_able_to_see_the_notification_groups_icon_for_the_newly_created_user_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_123.png")
            assert False

    def test_TC_US_124(self):
        self.logger.info("Users module = test_TC_US_124 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_for_newly_created_user_the_hover_text_is_visible_for_notification_groups_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_124.png")
            assert False

    def test_TC_US_125(self):
        self.logger.info("Users module = test_TC_US_125 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_open_the_notification_groups_for_the_newly_created_user_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_125.png")
            assert False

    def test_TC_US_126(self):
        self.logger.info("Users module = test_TC_US_126 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_see_the_details_icon_for_the_newly_created_user_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_126.png")
            assert False

    def test_TC_US_127(self):
        self.logger.info("Users module = test_TC_US_127 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_that_for_the_newly_created_user_the_hover_text_is_visible_for_details_icon_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_127.png")
            assert False

    def test_TC_US_128(self):
        self.logger.info("Users module = test_TC_US_128 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_open_the_details_for_the_newly_created_user_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_128.png")
            assert False

    def test_TC_US_129(self):
        self.logger.info("Users module = test_TC_US_129 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_see_the_alert_schedule_icon_for_the_newly_created_user_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_129.png")
            assert False

    def test_TC_US_130(self):
        self.logger.info("Users module = test_TC_US_130 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_for_the_newly_created_user_the_hover_text_is_visible_for_alert_schedule_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_130.png")
            assert False

    def test_TC_US_131(self):
        self.logger.info("Users module = test_TC_US_131 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_open_the_alert_schedule_for_the_newly_created_user_under_users_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_131.png")
            assert False

    def test_TC_US_132(self):
        self.logger.info("Users module = test_TC_US_132 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_edit_the_details_for_the_newly_created_user_details():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_132.png")
            assert False

    def test_TC_US_133(self):
        self.logger.info("Users module = test_TC_US_133 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_delete_the_newly_created_user():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_133.png")
            assert False

    def test_TC_US_134(self):
        self.logger.info("Users module = test_TC_US_134 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_should_not_be_able_to_create_user_which_already_exist():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_134.png")
            assert False

    def test_TC_US_135(self):
        self.logger.info("Users module = test_TC_US_135 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_should_not_be_able_to_create_user_if_password_and_confirm_password_does_not_match():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_135.png")
            assert False

    def test_TC_US_136(self):
        self.logger.info("Users module = test_TC_US_136 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_able_to_cancel_the_user_creation_after_filling_all_the_details():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_136.png")
            assert False

    def test_TC_US_137(self):
        self.logger.info("Users module = test_TC_US_137 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_when_user_close_user_panel_it_should_display_a_warning_popup():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_137.png")
            assert False

    def test_TC_US_138(self):
        self.logger.info("Users module = test_TC_US_138 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_users_sees_go_back_and_close_panel_and_discard_changes_in_warning_popup():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_138.png")
            assert False

    def test_TC_US_139(self):
        self.logger.info("Users module = test_TC_US_139 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_user_lands_on_the_same_panel_on_clicking_go_back():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_139.png")
            assert False

    def test_TC_US_140(self):
        self.logger.info("Users module = test_TC_US_140 execution started..")
        if Users_Module_pom(self.logger) \
                .verify_on_clicking_close_panel_and_discard_changes_user_panel_should_be_closed():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_US_140.png")
            assert False
