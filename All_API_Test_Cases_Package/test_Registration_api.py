from self import self
from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Registration_API_Methods import Registration_API_Methods


class Test_Registration_api(API_Base_Utilities):

    logger = API_Base_Utilities.logger_object()

    def test_Registration_API_01(self):
        self.logger.info("test_Registration_API_01  : Execution Started >>")
        if Registration_API_Methods(self.logger).Crate_new_user_and_validate_response():
            assert True
        else:
            assert False

    def test_Registration_API_02(self):
        self.logger.info("test_Registration_API_02  : Execution Started >>")
        if Registration_API_Methods(self.logger).Crate_new_user_with_register_email_and_validate_response():
            assert True
        else:
            assert False

    def test_Registration_API_03(self):
        self.logger.info("test_Registration_API_03  : Execution Started >>")
        if Registration_API_Methods(self.logger).Crate_new_user_with_blank_email_and_validate_response():
            assert True
        else:
            assert False
