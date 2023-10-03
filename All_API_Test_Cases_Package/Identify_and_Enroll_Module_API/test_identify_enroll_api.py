from All_API_Methods_Package.Identify_and_Enroll_Module_API.Identify_Enroll_Module_API import \
    Identify_Enroll_API_Methods
from All_API_Test_Cases_Package.conftest import API_Base_Utilities


class Test_identify_enroll_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_identify_enroll_Test_01(self):
        self.logger.info("test_identify_enroll_Test_01  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_create_enrollment():
            assert True
        else:
            assert False

    def test_identify_enroll_Test_02(self):
        self.logger.info("test_identify_enroll_Test_02  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_clear_enrollment_info():
            assert True
        else:
            assert False