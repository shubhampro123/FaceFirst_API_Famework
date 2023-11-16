from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Region_Module_API.Region_methods import Region_API_Methods


class Test_region_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_tags_Test_01(self):
        self.logger.info("test_region_Test_01  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_get_region_by_account_id():
            assert True
        else:
            assert False

    def test_tags_Test_02(self):
        self.logger.info("test_region_Test_02  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_get_region_by_id():
            assert True
        else:
            assert False

    def test_tags_Test_03(self):
        self.logger.info("test_region_Test_03  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_get_region_by_region_path():
            assert True
        else:
            assert False

    def test_tags_Test_04(self):
        self.logger.info("test_region_Test_04  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_get_region_by_descendants():
            assert True
        else:
            assert False

    def test_tags_Test_05(self):
        self.logger.info("test_region_Test_05  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_create_regions_migrate_events():
            assert True
        else:
            assert False

    def test_tags_Test_06(self):
        self.logger.info("test_region_Test_06  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_get_regions_by_cameras():
            assert True
        else:
            assert False

    def test_tags_Test_07(self):
        self.logger.info("test_region_Test_07  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_update_region_by_id():
            assert True
        else:
            assert False

    def test_tags_Test_08(self):
        self.logger.info("test_region_Test_08  : Execution Started >>")
        if Region_API_Methods(self.logger).verify_regions_import():
            assert True
        else:
            assert False

    def test_tags_Test_09(self):
        self.logger.info("test_region_Test_09  : Execution Started >>")
        if Region_API_Methods(self.logger).varify_create_regions_by_id():
            assert True
        else:
            assert False

    def test_tags_Test_10(self):
        self.logger.info("test_region_Test_10  : Execution Started >>")
        if Region_API_Methods(self.logger).varify_create_regions_by_id_descendants():
            assert True
        else:
            assert False

    def test_tags_Test_11(self):
        self.logger.info("test_region_Test_11  : Execution Started >>")
        if Region_API_Methods(self.logger).varify_create_regions_by_move():
            assert True
        else:
            assert False

    def test_tags_Test_12(self):
        self.logger.info("test_region_Test_12  : Execution Started >>")
        if Region_API_Methods(self.logger).varify_delete_regions():
            assert True
        else:
            assert False
