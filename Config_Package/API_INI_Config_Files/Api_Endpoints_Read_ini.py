import configparser
from pathlib import Path


class Read_API_Endpoints:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\API_Test_Data\\Api_Endpoints' \
                                        f'\\Endpoints.ini'
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("Read_API_Endpoints config file got an exception", ex)

    def get_login_endpoint(self):
        try:
            ele = self.config.get('LOGIN', 'login_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def users_endpoint(self):
        try:
            ele = self.config.get('USERS', 'users_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def user_role_endpoint(self):
        try:
            ele = self.config.get('USER_ROLE', 'user_role_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_region_endpoint(self):
        try:
            ele = self.config.get('REGION', 'get_region_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def edit_user_endpoint(self):
        try:
            ele = self.config.get('USERS', 'edit_user_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_users_endpoint(self):
        try:
            ele = self.config.get('USERS', 'get_users_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_users_by_account_id_endpoint(self):
        try:
            ele = self.config.get('USERS', 'get_users_by_account_id_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def users_update_alert_schedule_endpoint(self):
        try:
            ele = self.config.get('USERS', 'users_update_alert_schedule_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def create_users_endpoint(self):
        try:
            ele = self.config.get('USERS', 'create_users_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_users_by_id_endpoint(self):
        try:
            ele = self.config.get('USERS', 'get_users_by_id_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_report_sheet_path(self):
        try:
            ele = self.config.get('EXCEL_PATH', 'report_excel_sheet_path')
            return ele
        except Exception as ex:
            print(ex)

    def get_test_data_sheet_path(self):
        try:
            ele = self.config.get('EXCEL_PATH', 'test_data_excel_sheet_path')
            return ele
        except Exception as ex:
            print(ex)

    def get_login_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'login_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def users_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'users_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def login_test_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'login_test_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def users_test_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'users_test_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_success_response_code(self):
        try:
            ele = self.config.get('RESPONSE_CODE', 'success_response_code')
            return ele
        except Exception as ex:
            print(ex)

    def internal_server_error(self):
        try:
            ele = self.config.get('RESPONSE_CODE', 'internal_server_error')
            return ele
        except Exception as ex:
            print(ex)

    def user_role_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'user_role_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def user_role_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'user_role_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_user_role_endpoint(self):
        try:
            ele = self.config.get('USER_ROLE', 'get_user_role_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_user_role_by_id_endpoint(self, value):
        try:
            ele = self.config.get('USER_ROLE', 'get_user_role_by_id_endpoint')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def get_all_user_role_endpoint(self):
        try:
            ele = self.config.get('USER_ROLE', 'get_all_user_role_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def del_user_role_by_id_endpoint(self, value):
        try:
            ele = self.config.get('USER_ROLE', 'del_user_role_by_id_endpoint')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def update_user_role_endpoint(self):
        try:
            ele = self.config.get('USER_ROLE', 'update_user_role_endpoint')
            return ele
        except Exception as ex:
            print(ex)


    def get_all_enrollment_group_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'get_all_enrollment_group_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_group_test_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'enrollment_group_test_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def create_enrollment_group_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'create_enrollment_group_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_group_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'enrollment_group_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def update_enrollment_group_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'update_enrollment_group_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def delete_enrollment_group_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'delete_enrollment_group_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_all_zones_endpoint(self):
        try:
            ele = self.config.get('ZONES', 'get_all_zones_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def create_enrollment_group_with_addCaseGroupZone_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'create_enrollment_group_with_addCaseGroupZone_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def removeCaseGroupZone_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'removeCaseGroupZone_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_user_info_endpoint(self):
        try:
            ele = self.config.get('USERS', 'get_user_info_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_service_user_true_endpoint(self):
        try:
            ele = self.config.get('USERS', 'get_service_user_true_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_service_user_false_endpoint(self):
        try:
            ele = self.config.get('USERS', 'get_service_user_false_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_alert_schedule_endpoint(self, user_id):
        try:
            ele = self.config.get('USERS', 'get_alert_schedule_endpoint')
            return ele.format(user_id)
        except Exception as ex:
            print(ex)

    def get_delete_user_from_system_endpoint(self, value):
        try:
            ele = self.config.get('USERS', 'get_delete_user_from_system_endpoint')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def get_delete_user_endpoint(self, value):
        try:
            ele = self.config.get('USERS', 'get_delete_user_endpoint')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def get_all_enrollment_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT', 'get_all_enrollment_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def addCaseGroupCase_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'addCaseGroupCase_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def removeCaseGroupCase_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'removeCaseGroupCase_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_all_alert_groups_endpoint(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUP', 'get_all_alert_groups_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def removeAlertGroupCase_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'removeAlertGroupCase_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def addAlertGroupCase_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP', 'addAlertGroupCase_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def put_user_password_endpoint(self):
        try:
            ele = self.config.get('USERS', 'put_user_password_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def post_alert_groups_endpoint(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'post_alert_groups_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'notification_groups_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'notification_groups_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_all_alert_groups_endpoint(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'get_all_alert_groups_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_alert_group_using_ID(self, a_group_id):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'get_alert_group_using_ID')
            return ele.format(a_group_id)
        except Exception as ex:
            print(ex)

    def put_alert_group_ID(self, a_group_id):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'put_alert_group_ID')
            return ele.format(a_group_id)
        except Exception as ex:
            print(ex)

    def put_user_to_alert_group(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'put_user_to_alert_group')
            return ele
        except Exception as ex:
            print(ex)

    def put_remove_user_from_alert_group(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'put_remove_user_from_alert_group')
            return ele
        except Exception as ex:
            print(ex)

    def get_main_user_info(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'get_main_user_info')
            return ele
        except Exception as ex:
            print(ex)

    def get_zone_id(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'get_zone_id')
            return ele
        except Exception as ex:
            print(ex)

    def post_case_group(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'post_case_group')
            return ele
        except Exception as ex:
            print(ex)

    def delete_alert_group(self, a_group_id):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'delete_alert_group')
            return ele.format(a_group_id)
        except Exception as ex:
            print(ex)

    def put_enrollment_group_to_alert_group(self):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'put_enrollment_group_to_alert_group')
            return ele
        except Exception as ex:
            print(ex)

    def get_zone_by_id_endpoint(self, zone_id):
        try:
            ele = self.config.get('ZONES', 'get_zone_by_id_endpoint')
            return ele.format(zone_id)
        except Exception as ex:
            print(ex)

    def zones_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'zones_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def zones_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'zones_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_all_account_endpoint(self):
        try:
            ele = self.config.get('ACCOUNT', 'get_all_account_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_account_by_account_id_endpoint(self, account_id):
        try:
            ele = self.config.get('ACCOUNT', 'get_account_by_account_id_endpoint')
            return ele.format(account_id)
        except Exception as ex:
            print(ex)

    def get_account_stations_by_account_id_endpoint(self, account_id):
        try:
            ele = self.config.get('ACCOUNT', 'get_account_stations_by_account_id_endpoint')
            return ele.format(account_id)
        except Exception as ex:
            print(ex)

    def account_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'account_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def account_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'account_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def identify_enroll_test_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'identify_enroll_test_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def create_enrollment_endpoint(self):
        try:
            ele = self.config.get('IDENTIFY_ENROLL', 'create_enrollment_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def identify_enroll_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'identify_enroll_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_profile_endpoint(self):
        try:
            ele = self.config.get('PROFILE', 'get_profile_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_enrollment_profiles_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT', 'get_enrollment_profiles_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def query_enrollment_info_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT', 'query_enrollment_info_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def clear_enrollment_info_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT', 'clear_enrollment_info_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def query_login_info_endpoint(self):
        try:
            ele = self.config.get('LOGIN', 'query_login_info_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def logout_endpoint(self):
        try:
            ele = self.config.get('LOGIN', 'logout_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def identify_enrollment_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT', 'identify_enrollment_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def create_notes_endpoint(self):
        try:
            ele = self.config.get('NOTES', 'create_notes_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def notes_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'notes_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def notes_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'notes_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def update_notes_endpoint(self):
        try:
            ele = self.config.get('NOTES', 'update_notes_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_notes_endpoint(self, note_id):
        try:
            ele = self.config.get('NOTES', 'get_notes_endpoint')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def delete_notes_endpoint(self, note_id):
        try:
            ele = self.config.get('NOTES', 'delete_notes_endpoint')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def clear_notes_endpoint(self):
        try:
            ele = self.config.get('NOTES', 'clear_notes_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def images_bulk_endpoint(self, note_id):
        try:
            ele = self.config.get('NOTES', 'images_bulk_endpoint')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def get_images_endpoint(self, note_id):
        try:
            ele = self.config.get('NOTES', 'get_images_endpoint')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def delete_images_endpoint(self, note_id):
        try:
            ele = self.config.get('NOTES', 'delete_images_endpoint')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def detect_face_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'detect_face_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def detect_face_endpoint(self):
        try:
            ele = self.config.get('DETECT_FACE', 'detect_face_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def detect_face_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'detect_face_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def tags_test_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'tags_test_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def tags_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'tags_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def tags_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'tags_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def tags_endpoint(self):
        try:
            ele = self.config.get('TAGS', 'tags_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def create_tags_endpoint(self, name, serious_event, types):
        try:
            ele = self.config.get('TAGS', 'create_tags_endpoint')
            return ele.format(name, serious_event, types)
        except Exception as ex:
            print(ex)

    def get_tags_endpoint(self):
        try:
            ele = self.config.get('TAGS', 'get_tags_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def del_tags_by_id_endpoint(self, value):
        try:
            ele = self.config.get('TAGS', 'del_tags_by_id_endpoint')
            return ele.format(value)
        except Exception as ex:
            print(ex)

    def update_tags_endpoint(self):
        try:
            ele = self.config.get('TAGS', 'update_tags_endpoint')
            return ele
        except Exception as ex:
            print(ex)
