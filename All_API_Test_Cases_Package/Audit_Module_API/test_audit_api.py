from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Audit_Module_API.Audit_API_Methods import Audit_API_Methods


class Test_Account_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_Account_Test_01(self):
        self.logger.info("test_Account_Test_01  : Execution Started >>")
        if Audit_API_Methods(self.logger).verify_audit_approvers():
            assert True
        else:
            assert False

    def test_Account_Test_02(self):
        self.logger.info("test_Account_Test_02  : Execution Started >>")
        if Audit_API_Methods(self.logger).verify_audit_users():
            assert True
        else:
            assert False

    # def test_Account_Test_03(self):
    #     self.logger.info("test_Account_Test_03  : Execution Started >>")
    #     if Audit_API_Methods(self.logger).verify_audit_login():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_Account_Test_04(self):
    #     self.logger.info("test_Account_Test_04  : Execution Started >>")
    #     if Audit_API_Methods(self.logger).verify_get_audit_logins():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_Account_Test_05(self):
    #     self.logger.info("test_Account_Test_05  : Execution Started >>")
    #     if Audit_API_Methods(self.logger).verify_audit_threshold_changes():
    #         assert True
    #     else:
    #         assert False
