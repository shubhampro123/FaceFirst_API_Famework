from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Visitors_Search_Module_API.Visitors_Search_Methods import Visitors_Search_API_Methods


class Test_visitors_search_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_tags_Test_01(self):
        self.logger.info("test_visitor_search_Test_01  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_post_start_search_with_valid_data():
            assert True
        else:
            assert False

    def test_tags_Test_02(self):
        self.logger.info("test_visitor_search_Test_02  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_get_fed_search_status_with_valid_data():
            assert True
        else:
            assert False

