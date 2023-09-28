

from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Login_Module_API.Login_API_Methods import Login_API_Methods


class Test_login_api(API_Base_Utilities):

    logger = API_Base_Utilities.logger_object()

    def test_Login_Test_01(self):
        self.logger.info("test_Login_Test_01  : Execution Started >>")
        if Login_API_Methods(self.logger).login_with_valid_username_and_password():
            assert True
        else:
            assert False

    def test_Login_Test_02(self):
        self.logger.info("test_Login_Test_02  : Execution Started >>")
        if Login_API_Methods(self.logger).login_with_invalid_username_and_valid_password():
            assert True
        else:
            assert False

    def test_Login_Test_03(self):
        self.logger.info("test_Login_Test_03  : Execution Started >>")
        if Login_API_Methods(self.logger).login_with_valid_username_and_invalid_password():
            assert True
        else:
            assert False

    def test_Login_Test_04(self):
        self.logger.info("test_Login_Test_04  : Execution Started >>")
        if Login_API_Methods(self.logger).login_with_invalid_username_and_invalid_password():
            assert True
        else:
            assert False

    def test_Login_Test_05(self):
        self.logger.info("test_Login_Test_05  : Execution Started >>")
        if Login_API_Methods(self.logger).login_with_blank_username_and_blank_password():
            assert True
        else:
            assert False
