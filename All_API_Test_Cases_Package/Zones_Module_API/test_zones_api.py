
from All_API_Methods_Package.Zones_Module_API.Zones_API_Methods import Zones_API_Methods
from All_API_Test_Cases_Package.conftest import API_Base_Utilities


class Test_Zones_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_Zones_Test_01(self):
        self.logger.info("test_Zones_Test_01  : Execution Started >>")
        if Zones_API_Methods(self.logger).verify_get_all_zones():
            assert True
        else:
            assert False

    def test_Zones_Test_02(self):
        self.logger.info("test_Zones_Test_01  : Execution Started >>")
        if Zones_API_Methods(self.logger).verify_get_zone_by_id():
            assert True
        else:
            assert False