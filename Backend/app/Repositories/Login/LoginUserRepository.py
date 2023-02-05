from Common.db_common import DBConnection
from Models.UserModel import UserModel
from Repositories.Login.ILoginUserRepository import ILoginUserRepository

class LoginUserRepository(ILoginUserRepository):
    def get_group_user_info(self, gropu_id:int, user_unique_name: str, password: str):
        sql = f"""
        SELECT
          group_user_seq,
          group_user_unique_name,
          group_user_name
        FROM
          T_Group_User
        WHERE
          group_id = %(group_id)s
        AND
          group_user_unique_name = %(group_user_unique_name)s
        """
        parameters = { "group_id":gropu_id, "group_user_unique_name":user_unique_name }
        result = DBConnection('domain').execute_select_sql(sql, parameters)
        if len(result) != 1:
            return None
        return UserModel(
            result[0]['group_user_seq'],
            result[0]['group_user_unique_name'],
            result[0]['group_user_name']
        )
        
    def validate_group_user(self, group_id, user_id: int, user_uqniue_name: str) -> bool:
        sql = f"""
        SELECT
          'X'
        FROM
          T_Group_User
        WHERE
          is_deleted = '0'
        AND
          group_id = %(group_id)s
        AND
          group_user_seq = %(group_user_seq)s
        AND
          group_user_unique_name = %(group_user_unique_name)s
        """
        parameters = {"group_id": group_id, "group_user_seq": user_id, "group_user_unique_name": user_uqniue_name}
        result = DBConnection('domain').execute_select_sql(sql, parameters)
        if len(result) != 1:
            return False
        return True