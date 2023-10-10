from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.User_Roles_Module_API.User_Role_Methods import User_Role_API_Methods


class Test_user_role_api(API_Base_Utilities):

    logger = API_Base_Utilities.logger_object()

    def test_user_role_Test_01(self):
        self.logger.info("test_user_role_Test_01  : Execution Started >>")
        if User_Role_API_Methods(self.logger).verify_create_user_role_with_valid_data_in_enable_mode():
            assert True
        else:
            assert False

    def test_user_role_Test_02(self):
        self.logger.info("test_user_role_Test_02  : Execution Started >>")
        if User_Role_API_Methods(self.logger).verify_get_single_user_role_by_id():
            assert True
        else:
            assert False

    def test_user_role_Test_03(self):
        self.logger.info("test_user_role_Test_03  : Execution Started >>")
        if User_Role_API_Methods(self.logger).verify_update_user_role_with_valid_data():
            assert True
        else:
            assert False

    def test_user_role_Test_04(self):
        self.logger.info("test_user_role_Test_04  : Execution Started >>")
        if User_Role_API_Methods(self.logger).verify_delete_user_role_with_valid_user_role_id():
            assert True
        else:
            assert False

    def test_user_role_Test_05(self):
        self.logger.info("test_user_role_Test_05  : Execution Started >>")
        if User_Role_API_Methods(self.logger).verify_all_get_user_roles():
            assert True
        else:
            assert False

    def test_user_role_Test_06(self):
        self.logger.info("test_user_role_Test_06  : Execution Started >>")
        if User_Role_API_Methods(self.logger).verify_the_user_role_is_created_with_valid_data_in_disable_mode():
            assert True
        else:
            assert False


