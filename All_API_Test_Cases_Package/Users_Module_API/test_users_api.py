from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Users_Module_API.Users_API_Methods import Users_API_Methods


class Test_Users_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_Users_Test_01(self):
        self.logger.info("test_Users_Test_01  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_create_user_with_valid_information_in_enabled_mode():
            assert True
        else:
            assert False

    def test_Users_Test_02(self):
        self.logger.info("test_Users_Test_02  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_create_user_with_mandatory_information_in_enabled_mode():
            assert True
        else:
            assert False

    def test_Users_Test_03(self):
        self.logger.info("test_Users_Test_03  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_create_user_with_valid_information_in_disabled_mode():
            assert True
        else:
            assert False

    def test_Users_Test_04(self):
        self.logger.info("test_Users_Test_04  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_create_user_with_mandatory_fields_in_disable_mode():
            assert True
        else:
            assert False

    def test_Users_Test_06(self):
        self.logger.info("test_Users_Test_06  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_users_update_alert_schedule():
            assert True
        else:
            assert False

    def test_Users_Test_07(self):
        self.logger.info("test_Users_Test_07  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_create_users_using_json():
            assert True
        else:
            assert False

    def test_Users_Test_08(self):
        self.logger.info("test_Users_Test_08  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_edit_user_with_mandatory_information():
            assert True
        else:
            assert False

    def test_Users_Test_09(self):
        self.logger.info("test_Users_Test_09  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_edit_user_password():
            assert True
        else:
            assert False

    def test_Users_Test_10(self):
        self.logger.info("test_Users_Test_10  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_edite_user_with_json_data():
            assert True
        else:
            assert False

    def test_Users_Test_11(self):
        self.logger.info("test_Users_Test_11  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_get_users_api():
            assert True
        else:
            assert False

    def test_Users_Test_12(self):
        self.logger.info("test_Users_Test_12  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_get_user_by_account_id():
            assert True
        else:
            assert False

    def test_Users_Test_13(self):
        self.logger.info("test_Users_Test_13  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_get_user_by_id():
            assert True
        else:
            assert False

    def test_Users_Test_14(self):
        self.logger.info("test_Users_Test_14  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_get_user_info():
            assert True
        else:
            assert False

    def test_Users_Test_15(self):
        self.logger.info("test_Users_Test_15  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_get_service_user_true():
            assert True
        else:
            assert False

    def test_Users_Test_16(self):
        self.logger.info("test_Users_Test_16  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_get_service_user_false():
            assert True
        else:
            assert False

    def test_Users_Test_17(self):
        self.logger.info("test_Users_Test_17  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_get_users_alert_schedule():
            assert True
        else:
            assert False

    def test_Users_Test_18(self):
        self.logger.info("test_Users_Test_18  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_delete_user_from_system():
            assert True
        else:
            assert False

    def test_Users_Test_19(self):
        self.logger.info("test_Users_Test_19  : Execution Started >>")
        if Users_API_Methods(self.logger).verify_delete_user():
            assert True
        else:
            assert False
