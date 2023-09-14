from pathlib import Path
import pytest
from All_POM_Package.Tags_Module.Tags_Module_POM import Tags_Module_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Tags_Module(Base_Class):
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
            print("\nException in Test_Tags_Module/setup_method: ", ex)

    @pytest.mark.p1
    def test_TC_TAG_01(self):
        self.logger.info("test_TC_TAG_01 execution started..")
        if Tags_Module_pom(self.logger).create_tags_for_serious_event():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_01.png")
            self.logger.info("test_TC_TAG_01 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_02(self):
        self.logger.info("test_TC_TAG_02 execution started..")
        if Tags_Module_pom(self.logger).create_tags_for_non_serious_event():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_02.png")
            self.logger.info("test_TC_TAG_02 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_03(self):
        self.logger.info("test_TC_TAG_03 execution started..")
        if Tags_Module_pom(self.logger).tags_search_functionality():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_03.png")
            self.logger.info("test_TC_TAG_03 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_04(self):
        self.logger.info("test_TC_TAG_04 execution started..")
        if Tags_Module_pom(self.logger).filter_serious_event_tags_varify_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_04.png")
            self.logger.info("test_TC_TAG_04 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_05(self):
        self.logger.info("test_TC_TAG_05 execution started..")
        if Tags_Module_pom(self.logger).filter_non_serious_event_tags_varify_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_05.png")
            self.logger.info("test_TC_TAG_05 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_06(self):
        self.logger.info("test_TC_TAG_06 execution started..")
        if Tags_Module_pom(self.logger).duplicate_tags_not_create_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_06.png")
            self.logger.info("test_TC_TAG_06 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_07(self):
        self.logger.info("test_TC_TAG_07 execution started..")
        if Tags_Module_pom(self.logger).update_serious_event_tag_name():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_07.png")
            self.logger.info("test_TC_TAG_07 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_08(self):
        self.logger.info("test_TC_TAG_08 execution started..")
        if Tags_Module_pom(self.logger).delete_all_tags():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_08.png")
            self.logger.info("test_TC_TAG_08 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_09(self):
        self.logger.info("test_TC_TAG_09 execution started..")
        if Tags_Module_pom(self.logger).verify_deterred_tag_is_present_at_first():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_09.png")
            self.logger.info("test_TC_TAG_09 fail")
            assert False

    @pytest.mark.p2
    def test_TC_TAG_10(self):
        self.logger.info("test_TC_TAG_010 execution started..")
        if Tags_Module_pom(self.logger).close_panel_and_discard_changes_verify():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_10.png")
            self.logger.info("test_TC_TAG_10 fail")
            assert False
