from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Account_Module_API.Account_API_Methods import Account_API_Methods
from All_API_Methods_Package.All_Module_Search_API.All_module_search_API_Methods import All_Module_Search_API_Methods


class Test_All_Module_Search_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_All_Module_Search_Test_01(self):
        self.logger.info("test_All_Module_Search_Test_01  : Execution Started >>")
        if All_Module_Search_API_Methods(self.logger).verify_events_search():
            assert True
        else:
            assert False

    def test_All_Module_Search_Test_02(self):
        self.logger.info("test_All_Module_Search_Test_02  : Execution Started >>")
        if All_Module_Search_API_Methods(self.logger).verify_users_search():
            assert True
        else:
            assert False

    def test_All_Module_Search_Test_03(self):
        self.logger.info("test_All_Module_Search_Test_03  : Execution Started >>")
        if All_Module_Search_API_Methods(self.logger).verify_notes_search():
            assert True
        else:
            assert False

    def test_All_Module_Search_Test_04(self):
        self.logger.info("test_All_Module_Search_Test_04  : Execution Started >>")
        if All_Module_Search_API_Methods(self.logger).verify_visitors_search():
            assert True
        else:
            assert False

    def test_All_Module_Search_Test_05(self):
        self.logger.info("test_All_Module_Search_Test_05  : Execution Started >>")
        if All_Module_Search_API_Methods(self.logger).verify_enrollments_search():
            assert True
        else:
            assert False

    def test_All_Module_Search_Test_06(self):
        self.logger.info("test_All_Module_Search_Test_06  : Execution Started >>")
        if All_Module_Search_API_Methods(self.logger).verify_visitor_search_jobs_search():
            assert True
        else:
            assert False

