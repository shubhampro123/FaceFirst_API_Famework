from pathlib import Path
import pytest
from All_POM_Package.Visitor_search_jobs_Module.visitor_search_jobs_module_POM import Visitor_Search_jobs_Module_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Visitor_Search_jobs_Module:
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
            print("\nException in Test_Visitor_Search_Jobs_Module/setup_method: ", ex)

    ############################ ALL TEST CASES #######################

    @pytest.mark.p2
    def test_VSJ_001(self):
        self.logger.info("Visitor search jobs module = test_VSJ_001 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                Verify_user_able_to_view_the_Visitor_Search_jobs_on_the_cloud_menu():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_001.png")
            self.logger.info("test_VSJ_001 execution failed..")
            assert False

    @pytest.mark.p2
    def test_VSJ_002(self):
        self.logger.info("Visitor search jobs module = test_VSJ_002 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_user_opens_vsj_then_visitor_search_jobs_panel_should_display():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_002.png")
            self.logger.info("test_VSJ_002 execution failed..")
            assert False

    @pytest.mark.p2
    def test_VSJ_003(self):
        self.logger.info("Visitor search jobs module = test_VSJ_003 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger).verify_user_able_to_see_and_open_search_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_003.png")
            self.logger.info("test_VSJ_003 execution failed..")
            assert False

    @pytest.mark.p2
    def test_VSJ_004(self):
        self.logger.info("Visitor search jobs module = test_VSJ_004 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger).verify_users_able_to_see_and_open_action_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_004.png")
            self.logger.info("test_VSJ_004 execution failed..")
            assert False

    @pytest.mark.p2
    def test_VSJ_005(self):
        self.logger.info("Visitor search jobs module = test_VSJ_005 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                Verify_the_visitor_search_job_contains_the_visitors_from_the_data_range():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_005.png")
            self.logger.info("test_VSJ_005 execution failed..")
            assert False

    @pytest.mark.p2
    def test_VSJ_006(self):
        self.logger.info("Visitor search jobs module = test_VSJ_006 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitor_search_job_contains_user_performs_visitor_search_with_date_and_org_selection():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_006.png")
            self.logger.info("test_VSJ_006 execution failed..")
            assert False

    def test_VSJ_007(self):
        self.logger.info("Visitor search jobs module = test_VSJ_007 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitor_search_job_contains_the_visitor_in_selected_date_range_and_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_007.png")
            self.logger.info("test_VSJ_007 execution failed..")
            assert False

    def test_VSJ_008(self):
        self.logger.info("Visitor search jobs module = test_VSJ_008 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitor_search_job_contains_the_selected_gender_visitors_in_date_range_and_Org_selection():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_008.png")
            self.logger.info("test_VSJ_008 execution failed..")
            assert False

    def test_VSJ_009(self):
        self.logger.info("Visitor search jobs module = test_VSJ_009 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitor_search_job_contains_the_visitors_in_selected_date_range_and_age_range():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_009.png")
            self.logger.info("test_VSJ_009 execution failed..")
            assert False

    def test_VSJ_010(self):
        self.logger.info("Visitor search jobs module = test_VSJ_010 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitor_search_job_contains_the_visitors_in_date_range_and_age_range_and_org_selection():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_010.png")
            self.logger.info("test_VSJ_010 execution failed..")
            assert False

    def test_VSJ_011(self):
        self.logger.info("Visitor search jobs module = test_VSJ_011 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitor_search_job_contains_the_selected_gender_visitors_in_date_range_and_age_range():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_011.png")
            self.logger.info("test_VSJ_011 execution failed..")
            assert False

    def test_VSJ_012(self):
        self.logger.info("Visitor search jobs module = test_VSJ_012 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitor_search_job_contains_gender_visitors_in_date_range_and_age_range_and_org_selection():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_012.png")
            self.logger.info("test_VSJ_012 execution failed..")
            assert False

    def test_VSJ_013(self):
        self.logger.info("Visitor search jobs module = test_VSJ_013 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_vsj_contains_the_matching_visitors_max_count_should_be_50_search_with_image_only():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_013.png")
            self.logger.info("test_VSJ_013 execution failed..")
            assert False

    def test_VSJ_014(self):
        self.logger.info("Visitor search jobs module = test_VSJ_014 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_vsj_contains_the_count_of_matching_visitors_when_visitor_search_with_image_and_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_014.png")
            self.logger.info("test_VSJ_014 execution failed..")
            assert False

    def test_VSJ_015(self):
        self.logger.info("Visitor search jobs module = test_VSJ_015 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_vsj_contains_threshold_greater_than_or_equal_to_threshold_with_image_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_015.png")
            self.logger.info("test_VSJ_015 execution failed..")
            assert False

    def test_VSJ_016(self):
        self.logger.info("Visitor search jobs module = test_VSJ_016 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_threshold_when_search_threshold_with_image_threshold_and_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_016.png")
            self.logger.info("test_VSJ_016 execution failed..")
            assert False

    def test_VSJ_017(self):
        self.logger.info("Visitor search jobs module = test_VSJ_017 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_vsj_contains_gender_result_when_the_visitor_search_with_image_and_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_017.png")
            self.logger.info("test_VSJ_017 execution failed..")
            assert False

    def test_VSJ_018(self):
        self.logger.info("Visitor search jobs module = test_VSJ_018 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_vsj_contains_visitors_and_gender_when_search_with_image_gender_and_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_018.png")
            self.logger.info("test_VSJ_018 execution failed..")
            assert False

    def test_VSJ_019(self):
        self.logger.info("Visitor search jobs module = test_VSJ_019 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_vsj_contains_visitors_and_threshold_when_search_with_image_gender_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_019.png")
            self.logger.info("test_VSJ_019 execution failed..")
            assert False

    def test_VSJ_020(self):
        self.logger.info("Visitor search jobs module = test_VSJ_020 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_gender_threshold_max_matches_when_search_with_image_gender_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_020.png")
            self.logger.info("test_VSJ_020 execution failed..")
            assert False

    def test_VSJ_021(self):
        self.logger.info("Visitor search jobs module = test_VSJ_021 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_vsj_contains_an_age_range_when_a_visitor_search_with_an_image_and_an_age_range():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_021.png")
            self.logger.info("test_VSJ_021 execution failed..")
            assert False

    def test_VSJ_022(self):
        self.logger.info("Visitor search jobs module = test_VSJ_022 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_age_range_max_matches_when_visitor_search_with_image_age_range_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_022.png")
            self.logger.info("test_VSJ_022 execution failed..")
            assert False

    def test_VSJ_023(self):
        self.logger.info("Visitor search jobs module = test_VSJ_023 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_age_range_and_threshold_when_visitor_search_with_image_age_range_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_023.png")
            self.logger.info("test_VSJ_023 execution failed..")
            assert False

    def test_VSJ_024(self):
        self.logger.info("Visitor search jobs module = test_VSJ_024 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_age_threshold_and_max_of_matches_when_search_with_image_age_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_024.png")
            self.logger.info("test_VSJ_024 execution failed..")
            assert False

    def test_VSJ_025(self):
        self.logger.info("Visitor search jobs module = test_VSJ_025 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_visitor_search_job_contains_age_gender_when_visitor_search_with_image_age_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_025.png")
            self.logger.info("test_VSJ_025 execution failed..")
            assert False

    def test_VSJ_026(self):
        self.logger.info("Visitor search jobs module = test_VSJ_026 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_age_gender_and_max_matches_when_search_with_image_age_gender_and_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_026.png")
            self.logger.info("test_VSJ_026 execution failed..")
            assert False

    def test_VSJ_027(self):
        self.logger.info("Visitor search jobs module = test_VSJ_027 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_age_gender_and_threshold_when_search_with_image_age_gender_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_027.png")
            self.logger.info("test_VSJ_027 execution failed..")
            assert False

    def test_VSJ_028(self):
        self.logger.info("Visitor search jobs module = test_VSJ_028 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_age_gender_threshold_max_matches_search_image_age_gender_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_028.png")
            self.logger.info("test_VSJ_028 execution failed..")
            assert False

    def test_VSJ_029(self):
        self.logger.info("Visitor search jobs module = test_VSJ_029 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_visitor_search_job_contains_region_when_visitor_search_with_image_and_region():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_029.png")
            self.logger.info("test_VSJ_029 execution failed..")
            assert False

    def test_VSJ_030(self):
        self.logger.info("Visitor search jobs module = test_VSJ_030 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_and_max_matches_when_visitor_search_with_image_region_and_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_030.png")
            self.logger.info("test_VSJ_030 execution failed..")
            assert False

    def test_VSJ_031(self):
        self.logger.info("Visitor search jobs module = test_VSJ_031 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_and_threshold_when_visitor_search_with_image_region_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_031.png")
            self.logger.info("test_VSJ_031 execution failed..")
            assert False

    def test_VSJ_032(self):
        self.logger.info("Visitor search jobs module = test_VSJ_032 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_threshold_max_matches_when_search_with_image_region_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_032.png")
            self.logger.info("test_VSJ_032 execution failed..")
            assert False

    def test_VSJ_033(self):
        self.logger.info("Visitor search jobs module = test_VSJ_033 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_and_gender_when_search_with_image_region_and_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_033.png")
            self.logger.info("test_VSJ_033 execution failed..")
            assert False

    def test_VSJ_034(self):
        self.logger.info("Visitor search jobs module = test_VSJ_034 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_gender_max_matches_when_search_with_image_region_gender_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_034.png")
            self.logger.info("test_VSJ_034 execution failed..")
            assert False

    def test_VSJ_035(self):
        self.logger.info("Visitor search jobs module = test_VSJ_035 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_gender_and_threshold_when_search_with_image_region_gender_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_035.png")
            self.logger.info("test_VSJ_035 execution failed..")
            assert False

    def test_VSJ_036(self):
        self.logger.info("Visitor search jobs module = test_VSJ_036 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_gender_threshold_max_matches_search_image_region_gender_threshold_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_036.png")
            self.logger.info("test_VSJ_036 execution failed..")
            assert False

    def test_VSJ_037(self):
        self.logger.info("Visitor search jobs module = test_VSJ_037 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_and_age_range_when_search_with_image_region_and_age_range():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_037.png")
            self.logger.info("test_VSJ_037 execution failed..")
            assert False

    def test_VSJ_038(self):
        self.logger.info("Visitor search jobs module = test_VSJ_038 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_age_range_max_matches_when_search_with_image_region_age_range_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_038.png")
            self.logger.info("test_VSJ_038 execution failed..")
            assert False

    def test_VSJ_039(self):
        self.logger.info("Visitor search jobs module = test_VSJ_039 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_age_range_max_matches_when_search_with_image_region_age_range_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_039.png")
            self.logger.info("test_VSJ_039 execution failed..")
            assert False

    def test_VSJ_040(self):
        self.logger.info("Visitor search jobs module = test_VSJ_040 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_age_threshold_matches_search_with_image_region_age_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_040.png")
            self.logger.info("test_VSJ_040 execution failed..")
            assert False

    def test_VSJ_041(self):
        self.logger.info("Visitor search jobs module = test_VSJ_041 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_age_range_gender_when_search_with_image_region_age_range_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_041.png")
            self.logger.info("test_VSJ_041 execution failed..")
            assert False

    def test_VSJ_042(self):
        self.logger.info("Visitor search jobs module = test_VSJ_042 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_age_gender_mx_matches_when_search_with_image_region_age_gender_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_042.png")
            self.logger.info("test_VSJ_042 execution failed..")
            assert False

    def test_VSJ_043(self):
        self.logger.info("Visitor search jobs module = test_VSJ_043 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_region_age_gender_threshold_when_search_with_image_region_age_gender_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_043.png")
            self.logger.info("test_VSJ_043 execution failed..")
            assert False

    def test_VSJ_044(self):
        self.logger.info("Visitor search jobs module = test_VSJ_044 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_region_age_gender_threshold_mx_matches_search_image_region_age_gender_threshold_mx_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_044.png")
            self.logger.info("test_VSJ_044 execution failed..")
            assert False

    def test_VSJ_045(self):
        self.logger.info("Visitor search jobs module = test_VSJ_045 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_when_search_with_image_and_date_range():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_045.png")
            self.logger.info("test_VSJ_045 execution failed..")
            assert False

    def test_VSJ_046(self):
        self.logger.info("Visitor search jobs module = test_VSJ_046 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_and_max_matches_when_search_with_image_and_date_range_and_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_046.png")
            self.logger.info("test_VSJ_046 execution failed..")
            assert False

    def test_VSJ_047(self):
        self.logger.info("Visitor search jobs module = test_VSJ_047 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_and_threshold_when_search_with_image_and_date_range_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_047.png")
            self.logger.info("test_VSJ_047 execution failed..")
            assert False

    def test_VSJ_048(self):
        self.logger.info("Visitor search jobs module = test_VSJ_048 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_threshold_max_matches_search_image_date_range_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_048.png")
            self.logger.info("test_VSJ_048 execution failed..")
            assert False

    def test_VSJ_049(self):
        self.logger.info("Visitor search jobs module = test_VSJ_049 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_and_gender_when_search_with_image_date_range_and_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_049.png")
            self.logger.info("test_VSJ_049 execution failed..")
            assert False

    def test_VSJ_050(self):
        self.logger.info("Visitor search jobs module = test_VSJ_050 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_gender_max_matches_search_with_image_date_range_gender_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_050.png")
            self.logger.info("test_VSJ_050 execution failed..")
            assert False

    def test_VSJ_051(self):
        self.logger.info("Visitor search jobs module = test_VSJ_051 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_gender_threshold_search_with_image_date_range_gender_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_051.png")
            self.logger.info("test_VSJ_051 execution failed..")
            assert False

    def test_VSJ_052(self):
        self.logger.info("Visitor search jobs module = test_VSJ_052 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_date_range_gender_threshold_mx_matches_search_image_date_range_gender_threshold_mx_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_052.png")
            self.logger.info("test_VSJ_052 execution failed..")
            assert False

    def test_VSJ_053(self):
        self.logger.info("Visitor search jobs module = test_VSJ_053 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_and_age_when_search_with_image_date_range_and_age():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_053.png")
            self.logger.info("test_VSJ_053 execution failed..")
            assert False

    def test_VSJ_054(self):
        self.logger.info("Visitor search jobs module = test_VSJ_054 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_age_and_max_matches_when_search_image_date_range_age_and_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_054.png")
            self.logger.info("test_VSJ_054 execution failed..")
            assert False

    def test_VSJ_055(self):
        self.logger.info("Visitor search jobs module = test_VSJ_055 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_range_age_and_threshold_when_search_image_date_range_age_and_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_055.png")
            self.logger.info("test_VSJ_055 execution failed..")
            assert False

    def test_VSJ_056(self):
        self.logger.info("Visitor search jobs module = test_VSJ_056 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_age_threshold_max_matches_search_image_date_range_age_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_056.png")
            self.logger.info("test_VSJ_056 execution failed..")
            assert False

    def test_VSJ_057(self):
        self.logger.info("Visitor search jobs module = test_VSJ_057 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_age_gender_when_search_with_image_date_range_age_and_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_057.png")
            self.logger.info("test_VSJ_057 execution failed..")
            assert False

    def test_VSJ_058(self):
        self.logger.info("Visitor search jobs module = test_VSJ_058 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_age_gender_max_matches_search_with_image_date_range_age_gender_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_058.png")
            self.logger.info("test_VSJ_058 execution failed..")
            assert False

    def test_VSJ_059(self):
        self.logger.info("Visitor search jobs module = test_VSJ_059 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_age_gender_threshold_search_with_image_date_range_age_gender_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_059.png")
            self.logger.info("test_VSJ_059 execution failed..")
            assert False

    def test_VSJ_060(self):
        self.logger.info("Visitor search jobs module = test_VSJ_060 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_date_age_gender_threshold_matches_search_image_date_range_age_gender_threshold_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_060.png")
            self.logger.info("test_VSJ_060 execution failed..")
            assert False

    def test_VSJ_061(self):
        self.logger.info("Visitor search jobs module = test_VSJ_061 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_when_search_with_image_date_range_region():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_061.png")
            self.logger.info("test_VSJ_061 execution failed..")
            assert False

    def test_VSJ_062(self):
        self.logger.info("Visitor search jobs module = test_VSJ_062 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_max_matches_when_search_with_image_date_range_region_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_062.png")
            self.logger.info("test_VSJ_062 execution failed..")
            assert False

    def test_VSJ_063(self):
        self.logger.info("Visitor search jobs module = test_VSJ_063 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_age_gender_max_matches_search_image_date_region_age_gender_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_063.png")
            self.logger.info("test_VSJ_063 execution failed..")
            assert False

    def test_VSJ_064(self):
        self.logger.info("Visitor search jobs module = test_VSJ_064 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_threshold_max_matches_search_image_date_region_threshold_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_064.png")
            self.logger.info("test_VSJ_064 execution failed..")
            assert False

    def test_VSJ_065(self):
        self.logger.info("Visitor search jobs module = test_VSJ_065 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_gender_when_search_with_image_date_region_and_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_065.png")
            self.logger.info("test_VSJ_065 execution failed..")
            assert False

    def test_VSJ_066(self):
        self.logger.info("Visitor search jobs module = test_VSJ_066 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_gender_max_matches_search_with_image_date_region_gender_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_066.png")
            self.logger.info("test_VSJ_066 execution failed..")
            assert False

    def test_VSJ_067(self):
        self.logger.info("Visitor search jobs module = test_VSJ_067 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_gender_threshold_search_with_image_date_region_gender_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_067.png")
            self.logger.info("test_VSJ_067 execution failed..")
            assert False

    def test_VSJ_068(self):
        self.logger.info("Visitor search jobs module = test_VSJ_068 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_date_region_gender_threshold_matches_search_image_date_region_gender_threshold_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_068.png")
            self.logger.info("test_VSJ_068 execution failed..")
            assert False

    def test_VSJ_069(self):
        self.logger.info("Visitor search jobs module = test_VSJ_069 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_and_age_when_search_with_image_date_region_and_age():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_069.png")
            self.logger.info("test_VSJ_069 execution failed..")
            assert False

    def test_VSJ_070(self):
        self.logger.info("Visitor search jobs module = test_VSJ_070 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_age_max_matches_when_search_with_image_date_region_age_max_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_070.png")
            self.logger.info("test_VSJ_070 execution failed..")
            assert False

    def test_VSJ_071(self):
        self.logger.info("Visitor search jobs module = test_VSJ_071 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_age_threshold_when_search_with_image_date_region_age_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_071.png")
            self.logger.info("test_VSJ_071 execution failed..")
            assert False

    def test_VSJ_072(self):
        self.logger.info("Visitor search jobs module = test_VSJ_072 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_age_threshold_matches_search_image_date_region_age_threshold_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_072.png")
            self.logger.info("test_VSJ_072 execution failed..")
            assert False

    def test_VSJ_073(self):
        self.logger.info("Visitor search jobs module = test_VSJ_073 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_age_gender_when_search_with_image_date_region_age_and_gender():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_073.png")
            self.logger.info("test_VSJ_073 execution failed..")
            assert False

    def test_VSJ_074(self):
        self.logger.info("Visitor search jobs module = test_VSJ_074 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_age_gender_matches_search_image_date_region_age_gender_and_matches():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_074.png")
            self.logger.info("test_VSJ_074 execution failed..")
            assert False

    def test_VSJ_075(self):
        self.logger.info("Visitor search jobs module = test_VSJ_075 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_contains_date_region_age_gender_threshold_search_image_date_region_age_gender_threshold():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_075.png")
            self.logger.info("test_VSJ_075 execution failed..")
            assert False

    def test_VSJ_076(self):
        self.logger.info("Visitor search jobs module = test_VSJ_076 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_vsj_date_region_age_gender_threshold_max_search_image_date_region_age_gender_threshold_max():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_076.png")
            self.logger.info("test_VSJ_076 execution failed..")
            assert False

    def test_VSJ_077(self):
        self.logger.info("Visitor search jobs module = test_VSJ_077 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_for_visitor_search_with_meta_data_single_edge_or_store_selection():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_077.png")
            self.logger.info("test_VSJ_077 execution failed..")
            assert False

    def test_VSJ_078(self):
        self.logger.info("Visitor search jobs module = test_VSJ_078 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_visitor_search_with_an_image_the_default_match_count_should_be_50():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_078.png")
            self.logger.info("test_VSJ_078 execution failed..")
            assert False

    def test_VSJ_079(self):
        self.logger.info("Visitor search jobs module = test_VSJ_079 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                Verify_vs_with_image_the_visitor_search_result_should_be_listed_in_descending_order():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_079.png")
            self.logger.info("test_VSJ_079 execution failed..")
            assert False

    def test_VSJ_80(self):
        self.logger.info("Visitor search jobs module = test_VSJ_080 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_view_result_button_is_visible_and_clickable_in_the_visitor_search_jobs_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_080.png")
            self.logger.info("test_VSJ_080 execution failed..")
            assert False

    def test_VSJ_81(self):
        self.logger.info("Visitor search jobs module = test_VSJ_081 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitors_search_results_according_to_the_selected_max_match_count():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_081.png")
            self.logger.info("test_VSJ_081 execution failed..")
            assert False

    def test_VSJ_82(self):
        self.logger.info("Visitor search jobs module = test_VSJ_082 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_visitors_search_results_match_score_it_should_be_in_descending_order():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_082.png")
            self.logger.info("test_VSJ_082 execution failed..")
            assert False

    def test_VSJ_84(self):
        self.logger.info("Visitor search jobs module = test_VSJ_084 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_that_the_action_button_on_the_visitor_search_jobs_panel_is_visible_and_clickable():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_084.png")
            self.logger.info("test_VSJ_084 execution failed..")
            assert False

    def test_VSJ_85(self):
        self.logger.info("Visitor search jobs module = test_VSJ_085 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_the_action_dropdown_options_cancel_jobs_delete_jobs_refresh_change_refresh_visible_clickable():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_085.png")
            self.logger.info("test_VSJ_085 execution failed..")
            assert False

    def test_VSJ_86(self):
        self.logger.info("Visitor search jobs module = test_VSJ_086 execution started..")
        if Visitor_Search_jobs_Module_pom(self.logger). \
                verify_view_result_panel_Location_identify_enrollments_track_faces_identify_visitors_visible_clickble():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_086.png")
            self.logger.info("test_VSJ_086 execution failed..")
            assert False
