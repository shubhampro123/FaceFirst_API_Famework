from API_Utilities.Api_Base import API_Base_Utilities
from All_API_Methods_Package.Notes_Module_API.Notes_API_methods import Notes_API_Methods


class Test_notes_api(API_Base_Utilities):
    logger = API_Base_Utilities.get_logger()

    def test_notes_Test_01(self):
        self.logger.info("test_notes_Test_01  : Execution Started >>")
        if Notes_API_Methods(self.logger).verify_create_notes():
            assert True
        else:
            assert False

    def test_notes_Test_02(self):
        self.logger.info("test_notes_Test_02  : Execution Started >>")
        if Notes_API_Methods(self.logger).verify_get_notes_using_note_id():
            assert True
        else:
            assert False

    def test_notes_Test_03(self):
        self.logger.info("test_notes_Test_03  : Execution Started >>")
        if Notes_API_Methods(self.logger).verify_update_notes():
            assert True
        else:
            assert False

    def test_notes_Test_04(self):
        self.logger.info("test_notes_Test_04  : Execution Started >>")
        if Notes_API_Methods(self.logger).verify_delete_notes_using_note_id():
            assert True
        else:
            assert False

    def test_notes_Test_05(self):
        self.logger.info("test_notes_Test_05  : Execution Started >>")
        if Notes_API_Methods(self.logger).verify_clear_notes():
            assert True
        else:
            assert False

    def test_notes_Test_06(self):
        self.logger.info("test_notes_Test_06  : Execution Started >>")
        if Notes_API_Methods(self.logger).verify_add_image_to_note_using_note_id():
            assert True
        else:
            assert False

    def test_notes_Test_07(self):
        self.logger.info("test_notes_Test_07  : Execution Started >>")
        if Notes_API_Methods(self.logger).verify_get_image_using_note_id():
            assert True
        else:
            assert False
    #
    # def test_notes_Test_08(self):
    #     self.logger.info("test_notes_Test_08  : Execution Started >>")
    #     if Notes_API_Methods(self.logger).verify_delete_image_using_note_id():
    #         assert True
    #     else:
    #         assert False