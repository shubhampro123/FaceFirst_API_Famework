from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Visitors_Search_Module_API.Visitors_Search_Methods import Visitors_Search_API_Methods


class Test_visitors_search_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_Visitors_Test_01(self):
        self.logger.info("test_visitor_search_Test_01  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_post_start_search():
            assert True
        else:
            assert False

    def test_tags_Test_02(self):
        self.logger.info("test_visitor_search_Test_02  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_get_fed_search_status():
            assert True
        else:
            assert False

    def test_tags_Test_03(self):
        self.logger.info("test_visitor_search_Test_03  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_get_visitor_image_by_image_id():
            assert True
        else:
            assert False

    def test_tags_Test_04(self):
        self.logger.info("test_visitor_search_Test_04  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_identify_alien_federated():
            assert True
        else:
            assert False

    def test_tags_Test_05(self):
        self.logger.info("test_visitor_search_Test_05  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_identify_delete_federated():
            assert True
        else:
            assert False

    def test_tags_Test_06(self):
        self.logger.info("test_visitor_search_Test_06  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_get_alien_image():
            assert True
        else:
            assert False

    def test_tags_Test_07(self):
        self.logger.info("test_visitor_search_Test_07  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_identify_alien_federated_status():
            assert True
        else:
            assert False

    def test_tags_Test_08(self):
        self.logger.info("test_visitor_search_Test_08  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_query_alien_face_info():
            assert True
        else:
            assert False

    def test_tags_Test_09(self):
        self.logger.info("test_visitor_search_Test_09  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_identify_cancel_federated():
            assert True
        else:
            assert False

    def test_tags_Test_10(self):
        self.logger.info("test_visitor_search_Test_10  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_query_alien_federated_identification_log():
            assert True
        else:
            assert False

    def test_tags_Test_11(self):
        self.logger.info("test_visitor_search_Test_11  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_visitor_search():
            assert True
        else:
            assert False

    def test_tags_Test_12(self):
        self.logger.info("test_visitor_search_Test_12  : Execution Started >>")
        if Visitors_Search_API_Methods(self.logger).verify_visitor_count_by_zone():
            assert True
        else:
            assert False

