import pytest

from All_API_Methods_Package.Login_Module_API.Login_API_Methods import Login_API_Methods
from All_API_Test_Cases_Package.conftest import API_Base_Utilities


class Test_login_api(API_Base_Utilities):
    logger = API_Base_Utilities().get_logger()

    @pytest.mark.p1
    def test_Login_Test_01(self):
        self.logger.info("test_Login_Test_01  : Execution Started >>")
        if Login_API_Methods(self.logger).login_with_valid_username_and_password():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Login_Test_02(self):
        self.logger.info("test_Login_Test_02  : Execution Started >>")
        if Login_API_Methods(self.logger).verify_get_login():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Login_Test_03(self):
        self.logger.info("test_Login_Test_03  : Execution Started >>")
        if Login_API_Methods(self.logger).verify_query_login_info():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Login_Test_04(self):
        self.logger.info("test_Login_Test_04  : Execution Started >>")
        if Login_API_Methods(self.logger).verify_logout_request():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Login_Test_05(self):
        self.logger.info("test_Login_Test_05  : Execution Started >>")
        if Login_API_Methods(self.logger).login_with_blank_username_and_blank_password():
            assert True
        else:
            assert False
