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

    def get_audit_approvers_endpoint(self):
        try:
            ele = self.config.get('Audit', 'get_audit_approves')
            return ele
        except Exception as ex:
            print(ex)

    def get_audit_users_endpoint(self):
        try:
            ele = self.config.get('Audit', 'get_audit_users_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_audit_login_endpoint(self):
        try:
            ele = self.config.get('Audit', 'get_audit_login_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_request_audit_logins(self):
        try:
            ele = self.config.get('Audit', 'get_request_audit_logins')
            return ele
        except Exception as ex:
            print(ex)

    def get_request_audit_threshold_changes(self):
        try:
            ele = self.config.get('Audit', 'get_request_audit_threshold_changes')
            return ele
        except Exception as ex:
            print(ex)

    def users_endpoint(self):
        try:
            ele = self.config.get('USERS', 'users_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def alr_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'alr_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def user_role_endpoint(self):
        try:
            ele = self.config.get('USER_ROLE', 'user_role_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def alr_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'alr_result_sheet_name')
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

    def all_module_search_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'all_module_search_test_data_sheet_name')
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

    def events_search_endpoint(self):
        try:
            ele = self.config.get('All_Module_Search_API', 'events_search_endpoint')
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

    def get_visitor_search_jobs_search_endpoint(self):
        try:
            ele = self.config.get('VISITORS_SEARCH_JOBS', 'get_visitor_search_jobs_search_endpoint')
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

    def get_alert_group_using_ID(self,a_group_id):
        try:
            ele = self.config.get('NOTIFICATION_GROUPS', 'get_alert_group_using_ID')
            return ele.format(a_group_id)
        except Exception as ex:
            print(ex)

    def put_alert_group_ID(self,a_group_id):
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

    def get_zone_by_id_endpoint(self,zone_id):
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

    def get_account_by_account_id_endpoint(self,account_id):
        try:
            ele = self.config.get('ACCOUNT', 'get_account_by_account_id_endpoint')
            return ele.format(account_id)
        except Exception as ex:
            print(ex)

    def get_account_stations_by_account_id_endpoint(self,account_id):
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

    def all_module_search_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'all_module_search_result_sheet_name')
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

    def add_enrollment_with_image_end_point(self):
        try:
            ele = self.config.get('ENROLLMENT', 'add_enrollment_with_image_end_point')
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

    def get_enrollment_end_point(self, case_id):
        try:
            ele = self.config.get('ENROLLMENT', 'get_enrollment_end_point')
            return ele.format(case_id)
        except Exception as ex:
            print(ex)

    def get_enrollment_data_by_id(self, case_id):
        try:
            ele = self.config.get('ENROLLMENT', 'get_enrollment_data_by_id')
            return ele.format(case_id)
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

    def remove_enrollment_by_id(self):
        try:
            ele = self.config.get('ENROLLMENT', 'remove_enrollment_by_id')
            return ele
        except Exception as ex:
            print(ex)

    def images_bulk_endpoint(self, note_id):
        try:
            ele = self.config.get('NOTES', 'images_bulk_endpoint')
            return ele.format(note_id)
        except Exception as ex:
            print(ex)

    def create_enroll_with_id_ng(self, case_id):
        try:
            ele = self.config.get('ENROLLMENT', 'create_enroll_with_id_ng')
            return ele.format(case_id)
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

    def get_region_by_id_endpoint(self, id_value):
        try:
            ele = self.config.get('REGION', 'get_region_by_id_endpoint')
            return ele.format(id_value)
        except Exception as ex:
            print(ex)

    def get_region_import_file(self):
        try:
            ele = self.config.get('REGION', 'get_region_import_file')
            return ele
        except Exception as ex:
            print(ex)

    def get_region_by_region_path(self, id_value):
        try:
            ele = self.config.get('REGION', 'get_region_by_region_path')
            return ele.format(id_value)
        except Exception as ex:
            print(ex)

    def get_region_by_descendants(self, id_value):
        try:
            ele = self.config.get('REGION', 'get_region_by_descendants')
            return ele.format(id_value)
        except Exception as ex:
            print(ex)

    def create_by_migrate_events(self, zone_id):
        try:
            ele = self.config.get('REGION', 'create_by_migrate_events')
            return ele.format(zone_id)
        except Exception as ex:
            print(ex)

    def get_region_id_by_cameras(self, region_id):
        try:
            ele = self.config.get('REGION', 'get_region_id_by_cameras')
            return ele.format(region_id)
        except Exception as ex:
            print(ex)

    def create_region_by_descendants(self, region_id):
        try:
            ele = self.config.get('REGION', 'create_region_by_descendants')
            return ele.format(region_id)
        except Exception as ex:
            print(ex)

    def delete_region_endpoint(self, region_id):
        try:
            ele = self.config.get('REGION', 'delete_region_endpoint')
            return ele.format(region_id)
        except Exception as ex:
            print(ex)

    def create_move_regions(self):
        try:
            ele = self.config.get('REGION', 'create_move_regions')
            return ele
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

    def region_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'region_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def integration_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'integration_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def region_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'region_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_region_id_endpoint(self):
        try:
            ele = self.config.get('REGION', 'get_region_id_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def start_search_endpoint(self):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'start_search_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def visitors_search_end_point(self):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'visitors_search_end_point')
            return ele
        except Exception as ex:
            print(ex)

    def fed_search_status_endpoint(self, job_id):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'fed_search_status_endpoint')
            return ele.format(job_id)
        except Exception as ex:
            print(ex)

    def visitor_search_test_result_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'visitor_search_test_result_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def visitor_search_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'visitor_search_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def region_module_test_module(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'region_module_test_module')
            return ele
        except Exception as ex:
            print(ex)

    def note_search_endpoint(self):
        try:
            ele = self.config.get('NOTES', 'note_search_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def query_enrollment_info_by_id(self):
        try:
            ele = self.config.get('ENROLLMENT', 'query_enrollment_info_by_id')
            return ele
        except Exception as ex:
            print(ex)

    def aggregates_by_geospatial_endpoint(self):
        try:
            ele = self.config.get('NOTES', 'aggregates_by_geospatial_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_by_enrollment_endpoint(self):
        try:
            ele = self.config.get('NOTES', 'get_by_enrollment_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_visitors_image_by_image_id_endpoint(self, image_id):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'get_visitors_image_by_image_id_endpoint')
            return ele.format(image_id)
        except Exception as ex:
            print(ex)

    def post_identify_alien_federated(self):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'post_identify_alien_federated')
            return ele
        except Exception as ex:
            print(ex)

    def delete_alien_federated_endpoint(self, job_id):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'delete_alien_federated_endpoint')
            return ele.format(job_id)
        except Exception as ex:
            print(ex)

    def delete_alien_faces_endpoint(self):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'delete_alien_faces_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_alien_image_endpoint(self, image_id):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'get_alien_image_endpoint')
            return ele.format(image_id)
        except Exception as ex:
            print(ex)

    def get_identify_alien_federated_status_endpoint(self, job_id):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'get_identify_alien_federated_status_endpoint')
            return ele.format(job_id)
        except Exception as ex:
            print(ex)

    def get_query_alien_face_info_endpoint(self, image_id):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'get_query_alien_face_info_endpoint')
            return ele.format(image_id)
        except Exception as ex:
            print(ex)

    def put_identify_cancel_federated_endpoint(self, job_id):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'put_identify_cancel_federated_endpoint')
            return ele.format(job_id)
        except Exception as ex:
            print(ex)

    def get_query_alien_federated_identification_log_endpoint(self, result_deleted, count):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'get_query_alien_federated_identification_log_endpoint')
            return ele.format(result_deleted, count)
        except Exception as ex:
            print(ex)

    def post_visitor_search_endpoint(self, start, limit, sort_direction):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'post_visitor_search_endpoint')
            return ele.format(start, limit, sort_direction)
        except Exception as ex:
            print(ex)

    def get_visitor_count_by_zone_endpoint(self):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'get_visitor_count_by_zone_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_visitor_count_by_time_endpoint(self):
        try:
            ele = self.config.get('VISITOR_SEARCH', 'get_visitor_count_by_time_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_enrollment_data_by_id_endpoint(self, case_id):
        try:
            ele = self.config.get('ENROLLMENT_DATA', 'get_enrollment_data_by_id_endpoint')
            return ele.format(case_id)
        except Exception as ex:
            print(ex)

    def enrollment_data_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'enrollment_data_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_data_test_results_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'enrollment_data_test_results_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_enrollment_data_by_page_number_and_batch_size_request_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_DATA', 'get_enrollment_data_by_page_number_and_batch_size_request_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_enrollment_data_count_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_DATA', 'get_enrollment_data_count_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_group_data_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'enrollment_group_data_test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_group_data_test_results_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'enrollment_group_data_test_results_sheet_name')
            return ele
        except Exception as ex:
            print(ex)

    def get_enrollment_group_data_by_id_endpoint(self, c_group_id):
        try:
            ele = self.config.get('ENROLLMENT_GROUP_DATA', 'get_enrollment_group_data_by_id_endpoint')
            return ele.format(c_group_id)
        except Exception as ex:
            print(ex)

    def get_enrollment_group_data_by_page_number_and_batch_size_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP_DATA', 'get_enrollment_group_data_by_page_number_and_batch_size_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_enrollment_group_data_count_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_GROUP_DATA', 'get_enrollment_group_data_count_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_all_enrollment_template_data_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_TEMPLATE_DATA', 'get_all_enrollment_template_data_endpoint')
            return ele.format()
        except Exception as ex:
            print(ex)

    def enrollment_template_data_test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'enrollment_template_data_test_data_sheet_name')
            return ele.format()
        except Exception as ex:
            print(ex)

    def enrollment_template_data_test_results_sheet_name(self):
        try:
            ele = self.config.get('TEST_RESULT_SHEET_NAME', 'enrollment_template_data_test_results_sheet_name')
            return ele.format()
        except Exception as ex:
            print(ex)

    def post_enrollment_template_data_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_TEMPLATE_DATA', 'post_enrollment_template_data_endpoint')
            return ele.format()
        except Exception as ex:
            print(ex)

    def delete_enrollment_template_data_endpoint(self, case_id):
        try:
            ele = self.config.get('ENROLLMENT_TEMPLATE_DATA', 'delete_enrollment_template_data_endpoint')
            return ele.format(case_id)
        except Exception as ex:
            print(ex)

    def get_enrollment_template_data_count_endpoint(self):
        try:
            ele = self.config.get('ENROLLMENT_TEMPLATE_DATA', 'get_enrollment_template_data_count_endpoint')
            return ele
        except Exception as ex:
            print(ex)

    def get_enrollment_template_data_by_id_endpoint(self, enrollment_id):
        try:
            ele = self.config.get('ENROLLMENT_TEMPLATE_DATA', 'get_enrollment_template_data_by_id_endpoint')
            return ele.format(enrollment_id)
        except Exception as ex:
            print(ex)

    def put_enrollment_template_data_endpoint(self, enrollment_id):
        try:
            ele = self.config.get('ENROLLMENT_TEMPLATE_DATA', 'put_enrollment_template_data_endpoint')
            return ele.format(enrollment_id)
        except Exception as ex:
            print(ex)

    def integration_Test_data_sheet_name(self):
        try:
            ele = self.config.get('TEST_DATA_SHEET_NAME', 'integration_Test_data_sheet_name')
            return ele
        except Exception as ex:
            print(ex)