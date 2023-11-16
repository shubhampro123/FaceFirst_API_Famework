from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Enrollment_Data_Module_API.Enrollment_Data_API_Methods import Enrollment_Data_API_Methods


class Test_Enrollment_Data_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_Enrollment_Data_Test_01(self):
        self.logger.info("test_Enrollment_Data_Test_01  : Execution Started >>")
        if Enrollment_Data_API_Methods(self.logger).verify_get_enrollment_data_by_enrollment_id():
            assert True
        else:
            assert False

    def test_Enrollment_Data_Test_02(self):
        self.logger.info("test_Enrollment_Data_Test_02  : Execution Started >>")
        if Enrollment_Data_API_Methods(self.logger).verify_get_enrollment_data_by_page_number_and_batch_size():
            assert True
        else:
            assert False

    def test_Enrollment_Data_Test_03(self):
        self.logger.info("test_Enrollment_Data_Test_03  : Execution Started >>")
        if Enrollment_Data_API_Methods(self.logger).verify_get_enrollment_data_count():
            assert True
        else:
            assert False