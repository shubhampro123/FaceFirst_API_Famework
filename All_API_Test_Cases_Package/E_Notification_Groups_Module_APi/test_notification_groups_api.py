from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Notification_groups_Module_API.Notification_Groups_Methods import \
    Notification_Groups_API_Methods


class Test_Notification_groups_api(API_Base_Utilities):

    logger = API_Base_Utilities.get_logger()

    def test_Notification_Groups_Test_01(self):
        self.logger.info("test_Notification_Groups_Test_01  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_create_notification_group_with_users_enrollment_group_zones():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_02(self):
        self.logger.info("test_Notification_Groups_Test_02  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_create_notification_group_without_users_enrollment_group_and_zones():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_03(self):
        self.logger.info("test_Notification_Groups_Test_03  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_get_all_alert_groups():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_04(self):
        self.logger.info("test_Notification_Groups_Test_04  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_get_single_alert_group_using_id():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_05(self):
        self.logger.info("test_Notification_Groups_Test_05  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .modify_alert_group():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_06(self):
        self.logger.info("test_Notification_Groups_Test_06  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_add_user_to_alert_group():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_07(self):
        self.logger.info("test_Notification_Groups_Test_07  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_remove_user_from_alert_group():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_08(self):
        self.logger.info("test_Notification_Groups_Test_08  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_delete_alert_group():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_09(self):
        self.logger.info("test_Notification_Groups_Test_09  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_notification_group_should_not_be_duplicate():
            assert True
        else:
            assert False

    def test_Notification_Groups_Test_10(self):
        self.logger.info("test_Notification_Groups_Test_10  : Execution Started >>")
        if Notification_Groups_API_Methods(self.logger)\
                .verify_add_enrollment_group_to_notification_group():
            assert True
        else:
            assert False

