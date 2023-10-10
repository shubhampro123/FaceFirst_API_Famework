from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Tags_Module_API.Tags_API_Methods import Tags_API_Methods


class Test_tags_api(API_Base_Utilities):
    logger = API_Base_Utilities.logger_object()

    def test_tags_Test_01(self):
        self.logger.info("test_tags_Test_01  : Execution Started >>")
        if Tags_API_Methods(self.logger).verify_create_tags_with_valid_data():
            assert True
        else:
            assert False

    def test_tags_Test_02(self):
        self.logger.info("test_tags_Test_02  : Execution Started >>")
        if Tags_API_Methods(self.logger).verify_all_get_tag_data():
            assert True
        else:
            assert False

    def test_tags_Test_03(self):
        self.logger.info("test_tags_Test_03  : Execution Started >>")
        if Tags_API_Methods(self.logger).verify_update_tag_with_valid_data():
            assert True
        else:
            assert False

    def test_tags_Test_04(self):
        self.logger.info("test_tags_Test_04  : Execution Started >>")
        if Tags_API_Methods(self.logger).verify_delete_tags_with_valid_tag_id():
            assert True
        else:
            assert False

    def test_tags_Test_05(self):
        self.logger.info("test_tags_Test_04  : Execution Started >>")
        if Tags_API_Methods(self.logger).verify_create_tag_with_tag_alert():
            assert True
        else:
            assert False
