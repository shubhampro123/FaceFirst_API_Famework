import pytest

from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Integration_End_To_End.integration_Methods import Integration_API_Methods


class Test_integration_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    @pytest.mark.p1
    def test_integration_Test_01(self):
        self.logger.info("test_integration_Test_01  : Execution Started >>")
        if Integration_API_Methods(self.logger).integration_end_to_end():
            assert True
        else:
            assert False

    def test_integration_Test_02(self):
        self.logger.info("test_integration_Test_02  : Execution Started >>")
        if Integration_API_Methods(self.logger).second_integration_end_to_end_VS_with_pic():
            assert True
        else:
            assert False

    def test_integration_Test_03(self):
        self.logger.info("test_integration_Test_03  : Execution Started >>")
        if Integration_API_Methods(self.logger).third_integration_end_to_end_VS_with_pic_metadata():
            assert True
        else:
            assert False

    def test_integration_Test_04(self):
        self.logger.info("test_integration_Test_04  : Execution Started >>")
        if Integration_API_Methods(self.logger).fourth_integration_end_to_end_VS_with_only_metadata():
            assert True
        else:
            assert False







