from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Detect_Face_Module_API.Detect_Faces_API_Methods import Detect_Face_API_Methods


class Test_detect_face_api(API_Base_Utilities):
    logger = API_Base_Utilities().get_logger()

    def test_tags_Test_01(self):
        self.logger.info("test_detect_face_Test_01  : Execution Started >>")
        if Detect_Face_API_Methods(self.logger).verify_post_detect_face_with_valid_data():
            assert True
        else:
            assert False
