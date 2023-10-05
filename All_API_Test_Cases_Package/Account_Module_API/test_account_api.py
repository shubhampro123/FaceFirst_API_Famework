from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Account_Module_API.Account_API_Methods import Account_API_Methods


class Test_Account_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_Account_Test_01(self):
        self.logger.info("test_Account_Test_01  : Execution Started >>")
        if Account_API_Methods(self.logger).verify_get_all_account():
            assert True
        else:
            assert False

    def test_Account_Test_02(self):
        self.logger.info("test_Account_Test_02  : Execution Started >>")
        if Account_API_Methods(self.logger).verify_get_account_by_account_id():
            assert True
        else:
            assert False

    def test_Account_Test_03(self):
        self.logger.info("test_Account_Test_03  : Execution Started >>")
        if Account_API_Methods(self.logger).verify_account_stations_by_account_id():
            assert True
        else:
            assert False