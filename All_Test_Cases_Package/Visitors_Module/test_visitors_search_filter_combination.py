from pathlib import Path
import pytest
from All_POM_Package.Visitors_Module.Visitors_Search_Filter_Combination_POM import \
    Visitors_Search_Filter_Combination_POM
from All_Test_Cases_Package.conftest import Base_Class


class Test_visitors_search_filter_combination(Base_Class):
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
            print("\nException in Test_visitors_search_filter_combination/setup_method: ", ex)

    @pytest.mark.p1
    def test_TC_SVF_01(self):
        self.logger.info("test_TC_SVF_01 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_no_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_01_failed.png")
            self.logger.info("test_TC_SVF_01 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_02(self):
        self.logger.info("test_TC_SVF_02 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_02_failed.png")
            self.logger.info("test_TC_SVF_02 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_03(self):
        self.logger.info("test_TC_SVF_03 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_03_failed.png")
            self.logger.info("test_TC_SVF_03 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_04(self):
        self.logger.info("test_TC_SVF_04 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_04_failed.png")
            self.logger.info("test_TC_SVF_04 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_05(self):
        self.logger.info("test_TC_SVF_05 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_age_range_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_05_failed.png")
            self.logger.info("test_TC_SVF_05 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_06(self):
        self.logger.info("test_TC_SVF_06 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_age_range_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_06_failed.png")
            self.logger.info("test_TC_SVF_06 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_07(self):
        self.logger.info("test_TC_SVF_07 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_age_range_and_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_07_failed.png")
            self.logger.info("test_TC_SVF_07 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_08(self):
        self.logger.info("test_TC_SVF_08 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger)\
                .search_visitors_with_age_range_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_08_failed.png")
            self.logger.info("test_TC_SVF_08 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_09(self):
        self.logger.info("test_TC_SVF_09 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_datetime_range_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_09_failed.png")
            self.logger.info("test_TC_SVF_09 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_10(self):
        self.logger.info("test_TC_SVF_010 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_datetime_range_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_010_failed.png")
            self.logger.info("test_TC_SVF_010 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_11(self):
        self.logger.info("test_TC_SVF_011 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_datetime_range_and_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_011_failed.png")
            self.logger.info("test_TC_SVF_011 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_12(self):
        self.logger.info("test_TC_SVF_012 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger)\
                .search_visitors_with_datetime_range_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_012_failed.png")
            self.logger.info("test_TC_SVF_012 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_13(self):
        self.logger.info("test_TC_SVF_013 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger).search_visitors_with_datetime_and_age_range_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_013_failed.png")
            self.logger.info("test_TC_SVF_013 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_14(self):
        self.logger.info("test_TC_SVF_014 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger)\
                .search_visitors_with_datetime_age_range_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_014_failed.png")
            self.logger.info("test_TC_SVF_014 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_15(self):
        self.logger.info("test_TC_SVF_015 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger)\
                .search_visitors_with_datetime_age_range_and_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_015_failed.png")
            self.logger.info("test_TC_SVF_015 fail")
            assert False

    @pytest.mark.p1
    def test_TC_SVF_16(self):
        self.logger.info("test_TC_SVF_016 execution started..")
        if Visitors_Search_Filter_Combination_POM(self.logger)\
                .search_visitors_with_datetime_age_range_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_016_failed.png")
            self.logger.info("test_TC_SVF_016 fail")
            assert False



