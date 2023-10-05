import pytest

from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Identify_and_Enroll_Module_API.Identify_Enroll_Module_API import \
    Identify_Enroll_API_Methods


class Test_identify_enroll_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    @pytest.mark.p1
    def test_identify_enroll_Test_01(self):
        self.logger.info("test_identify_enroll_Test_01  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_create_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_identify_enroll_Test_02(self):
        self.logger.info("test_identify_enroll_Test_02  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_clear_enrollment_info():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_identify_enroll_Test_03(self):
        self.logger.info("test_identify_enroll_Test_03  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_query_Enrollment_FaceInfo():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_identify_enroll_Test_04(self):
        self.logger.info("test_identify_enroll_Test_04  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_enrollment_profiles():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_identify_enroll_Test_05(self):
        self.logger.info("test_identify_enroll_Test_05  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_identify_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_identify_enroll_Test_06(self):
        self.logger.info("test_identify_enroll_Test_06  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_search_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_identify_enroll_Test_07(self):
        self.logger.info("test_identify_enroll_Test_07  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_edit_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_identify_enroll_Test_08(self):
        self.logger.info("test_identify_enroll_Test_08  : Execution Started >>")
        if Identify_Enroll_API_Methods(self.logger).verify_delete_enrollments():
            assert True
        else:
            assert False