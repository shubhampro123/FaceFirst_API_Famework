from pathlib import Path
import pytest
from All_POM_Package.Portal_Menu_Module.Portal_Menu_POM import Portal_Menu_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Portal_Menu_Test_Cases(Base_Class):
    logger = Base_Class.logger_object()

    def setup_method(self):
        try:
            self.d = Base_Class.d
            self.d.maximize_window()
            self.d.set_page_load_timeout(50)
            self.d.set_script_timeout(30)
            self.d.implicitly_wait(30)
            self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
        except Exception as ex:
            print(f"\nException in Test_Portal_Menu_Test_Cases/setup_method: {ex}")

    @pytest.mark.p1
    def test_TC_PM_24(self):
        self.logger.info("test_TC_PM_24 execution started..")
        if Portal_Menu_pom(self.logger).reset_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\reset_password.png")
            self.logger.info("test_TC_PM_24 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_26(self):
        self.logger.info("test_TC_PM_26 execution started..")
        if Portal_Menu_pom(self.logger).current_and_new_password_not_same_validation():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\current_and_new_password_not_same_validation.png")
            self.logger.info("test_TC_PM_26 fail")
            assert False

    @pytest.mark.p2
    def test_TC_PM_27(self):
        self.logger.info("test_TC_PM_27 execution started..")
        if Portal_Menu_pom(self.logger).set_upper_case_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_upper_case_password.png")
            self.logger.info("test_TC_PM_27 fail")
            assert False

    @pytest.mark.p2
    def test_TC_PM_28(self):
        self.logger.info("test_TC_PM_28 execution started..")
        if Portal_Menu_pom(self.logger).set_lower_case_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_lower_case_password.png")
            self.logger.info("test_TC_PM_28 fail")
            assert False

    @pytest.mark.p2
    def test_TC_PM_29(self):
        self.logger.info("test_TC_PM_29 execution started..")
        if Portal_Menu_pom(self.logger).set_special_character_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_special_character_password.png")
            self.logger.info("test_TC_PM_29 fail")
            assert False

    @pytest.mark.p2
    def test_TC_PM_30(self):
        self.logger.info("test_TC_PM_30 execution started..")
        if Portal_Menu_pom(self.logger).set_less_than_eight_character_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\set_less_than_eight_character_password.png")
            self.logger.info("test_TC_PM_30 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_1(self):
        self.logger.info("test_TC_PM_1 execution started..")
        if Portal_Menu_pom(self.logger).event_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_button_validation.png")
            self.logger.info("test_TC_PM_1 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_2(self):
        self.logger.info("test_TC_PM_2 execution started..")
        if Portal_Menu_pom(self.logger).tags_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\tags_button_validation.png")
            self.logger.info("test_TC_PM_2 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_3(self):
        self.logger.info("test_TC_PM_3 execution started..")
        if Portal_Menu_pom(self.logger).identify_enroll_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\identify_enroll_button_validation.png")
            self.logger.info("test_TC_PM_3 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_4(self):
        self.logger.info("test_TC_PM_4 execution started..")
        if Portal_Menu_pom(self.logger).detect_faces_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\detect_faces_button_validation.png")
            self.logger.info("test_TC_PM_4 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_5(self):
        self.logger.info("test_TC_PM_5 execution started..")
        if Portal_Menu_pom(self.logger).enrollments_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\enrollments_button_validation.png")
            self.logger.info("test_TC_PM_5 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_6(self):
        self.logger.info("test_TC_PM_6 execution started..")
        if Portal_Menu_pom(self.logger).enrollments_groups_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\enrollments_groups_button_validation.png")
            self.logger.info("test_TC_PM_6 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_7(self):
        self.logger.info("test_TC_PM_7 execution started..")
        if Portal_Menu_pom(self.logger).notification_groups_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\notification_groups_button_validation.png")
            self.logger.info("test_TC_PM_7 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_8(self):
        self.logger.info("test_TC_PM_8 execution started..")
        if Portal_Menu_pom(self.logger).visitors_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_button_validation.png")
            self.logger.info("test_TC_PM_8 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_9(self):
        self.logger.info("test_TC_PM_9 execution started..")
        if Portal_Menu_pom(self.logger).visitors_search_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_button_validation.png")
            self.logger.info("test_TC_PM_9 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_10(self):
        self.logger.info("test_TC_PM_10 execution started..")
        if Portal_Menu_pom(self.logger).visitors_search_button_job_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\visitors_search_button_job_validation.png")
            self.logger.info("test_TC_PM_10 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_11(self):
        self.logger.info("test_TC_PM_11 execution started..")
        if Portal_Menu_pom(self.logger).notes_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_validation.png")
            self.logger.info("test_TC_PM_11 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_12(self):
        self.logger.info("test_TC_PM_12 execution started..")
        if Portal_Menu_pom(self.logger).locations_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\locations_validation.png")
            self.logger.info("test_TC_PM_12 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_13(self):
        self.logger.info("test_TC_PM_13 execution started..")
        if Portal_Menu_pom(self.logger).users_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\users_validation.png")
            self.logger.info("test_TC_PM_13 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_14(self):
        self.logger.info("test_TC_PM_14 execution started..")
        if Portal_Menu_pom(self.logger).users_roles_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\users_roles_validation.png")
            self.logger.info("test_TC_PM_14 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_15(self):
        self.logger.info("test_TC_PM_15 execution started..")
        if Portal_Menu_pom(self.logger).zones_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\zones_button_validation.png")
            self.logger.info("test_TC_PM_15 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_16(self):
        self.logger.info("test_TC_PM_16 execution started..")
        if Portal_Menu_pom(self.logger).account_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\account_button_validation.png")
            self.logger.info("test_TC_PM_16 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_17(self):
        self.logger.info("test_TC_PM_17 execution started..")
        if Portal_Menu_pom(self.logger).reporting_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\reporting_button_validation.png")
            self.logger.info("test_TC_PM_17 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_18(self):
        self.logger.info("test_TC_PM_18 execution started..")
        if Portal_Menu_pom(self.logger).notifier_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\notifier_button_validation.png")
            self.logger.info("test_TC_PM_18 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_19(self):
        self.logger.info("test_TC_PM_19 execution started..")
        if Portal_Menu_pom(self.logger).dashboard_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\dashboard_button_validation.png")
            self.logger.info("test_TC_PM_19 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_31(self):
        self.logger.info("test_TC_PM_31 execution started..")
        if Portal_Menu_pom(self.logger).audit_reports_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\audit_reports_button_validation.png")
            self.logger.info("test_TC_PM_31 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_20(self):
        self.logger.info("test_TC_PM_20 execution started..")
        if Portal_Menu_pom(self.logger).close_all_panel_button():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_button.png")
            self.logger.info("test_TC_PM_20 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_21(self):
        self.logger.info("test_TC_PM_21 execution started..")
        if Portal_Menu_pom(self.logger).copyright_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\copyright_button_validation.png")
            self.logger.info("test_TC_PM_21 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_22(self):
        self.logger.info("test_TC_PM_22 execution started..")
        if Portal_Menu_pom(self.logger).profile_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\profile_button_validation.png")
            self.logger.info("test_TC_PM_22 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_23(self):
        self.logger.info("test_TC_PM_23 execution started..")
        if Portal_Menu_pom(self.logger).face_first_logo_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\face_first_logo_validation.png")
            self.logger.info("test_TC_PM_23 fail")
            assert False

    @pytest.mark.p1
    def test_TC_PM_25(self):
        self.logger.info("test_TC_PM_25 execution started..")
        if Portal_Menu_pom(self.logger).logout_button_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\logout_button_validation.png")
            self.logger.info("test_TC_PM_25 fail")
            assert False



    
