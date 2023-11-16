import pytest

from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Integration_End_To_End.integration_Methods import Integration_API_Methods


class Test_integration_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_integration_Test_05(self):
        self.logger.info("test_integration_Test_04  : Execution Started >>")
        if Integration_API_Methods(self.logger).verify_approve_enrollment_end_to_end_integration_flow():
            assert True
        else:
            assert False

    def test_integration_Test_06(self):
        self.logger.info("test_integration_Test_06  : Execution Started >>")
        if Integration_API_Methods(self.logger).verify_disable_approve_enrollment_end_to_end_integration_flow():
            assert True
        else:
            assert False
