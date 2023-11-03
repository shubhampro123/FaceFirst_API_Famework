from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Enrollment_Template_Data_Module_API.Enrollment_Template_Data_API_Methods import \
    Enrollment_Template_Data_API_Methods


class Test_Enrollment_Template_Data_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    # def test_Enrollment_Template_Data_Test_01(self):
    #     self.logger.info("test_Enrollment_Template_Data_Test_01  : Execution Started >>")
    #     if Enrollment_Template_Data_API_Methods(self.logger).verify_get_all_enrollment_template_data():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_Enrollment_Template_Data_Test_02(self):
    #     self.logger.info("test_Enrollment_Template_Data_Test_02  : Execution Started >>")
    #     if Enrollment_Template_Data_API_Methods(self.logger).verify_create_enrollment_template_data():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_Enrollment_Template_Data_Test_03(self):
    #     self.logger.info("test_Enrollment_Template_Data_Test_03  : Execution Started >>")
    #     if Enrollment_Template_Data_API_Methods(self.logger).verify_delete_enrollment_template_data():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_Enrollment_Template_Data_Test_04(self):
    #     self.logger.info("test_Enrollment_Template_Data_Test_04  : Execution Started >>")
    #     if Enrollment_Template_Data_API_Methods(self.logger).verify_get_enrollment_template_data_count():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_Enrollment_Template_Data_Test_05(self):
    #     self.logger.info("test_Enrollment_Template_Data_Test_05  : Execution Started >>")
    #     if Enrollment_Template_Data_API_Methods(self.logger).verify_get_enrollment_template_data_by_enrollment_id():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_Enrollment_Template_Data_Test_06(self):
    #     self.logger.info("test_Enrollment_Template_Data_Test_06  : Execution Started >>")
    #     if Enrollment_Template_Data_API_Methods(self.logger).verify_edit_enrollment_template_data():
    #         assert True
    #     else:
    #         assert False