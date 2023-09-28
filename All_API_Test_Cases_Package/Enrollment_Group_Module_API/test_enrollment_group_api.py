from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Enrollment_Group_Module_API.Enrollment_Group_API_Methods import \
    Enrollment_Group_API_Methods


class Test_enrollment_group_api(API_Base_Utilities):

    logger = API_Base_Utilities.logger_object()

    def test_enrollment_group_Test_01(self):
        self.logger.info("test_enrollment_group_Test_01  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_the_get_all_enrollment_group():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_02(self):
        self.logger.info("test_enrollment_group_Test_02  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_the_enrollment_groups_is_created_with_valid_data():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_03(self):
        self.logger.info("test_enrollment_group_Test_03  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_the_get_single_enrollment_group():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_04(self):
        self.logger.info("test_enrollment_group_Test_04  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_the_update_enrollment_group():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_05(self):
        self.logger.info("test_enrollment_group_Test_05  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_remove_a_single_Enrollment_Group_from_collection():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_06(self):
        self.logger.info("test_enrollment_group_Test_06  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_create_enrollment_group_with_addCaseGroupZone():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_07(self):
        self.logger.info("test_enrollment_group_Test_07  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_removeCaseGroupZone():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_08(self):
        self.logger.info("test_enrollment_group_Test_08  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_addCaseGroupCase():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_09(self):
        self.logger.info("test_enrollment_group_Test_09  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_removeCaseGroupCase():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_10(self):
        self.logger.info("test_enrollment_group_Test_10  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_addAlertGroupCase():
            assert True
        else:
            assert False

    def test_enrollment_group_Test_11(self):
        self.logger.info("test_enrollment_group_Test_11  : Execution Started >>")
        if Enrollment_Group_API_Methods(self.logger).verify_removeAlertGroupCase():
            assert True
        else:
            assert False

