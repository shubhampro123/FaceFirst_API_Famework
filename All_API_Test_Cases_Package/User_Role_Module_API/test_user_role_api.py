from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.User_Role_Module_API.User_Role_API_Methods import User_Role_API_Methods


class Test_user_role_api(API_Base_Utilities):

    logger = API_Base_Utilities.logger_object()

    def test_user_role_Test_01(self):
        self.logger.info("test_Login_Test_01  : Execution Started >>")
        if User_Role_API_Methods(self.logger).post_user_role():
            assert True
        else:
            assert False

    def test_user_role_Test_02(self):
        self.logger.info("test_Login_Test_02  : Execution Started >>")
        if User_Role_API_Methods(self.logger).get_user_role():
            assert True
        else:
            assert False

    def test_user_role_Test_03(self):
        self.logger.info("test_Login_Test_03  : Execution Started >>")
        if User_Role_API_Methods(self.logger).verify_get_user_role_by_id():
            assert True
        else:
            assert False