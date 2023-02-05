from Common.db_common import DBConnection
from Models.GroupModel import GroupModel
from Repositories.Login.ILoginGroupRepository import ILoginGroupRepository as repository

class LoginGroupRepository(repository):
    def get_group_info(self, group_unique_name: str) -> GroupModel:
        sql = f"""
        SELECT
          group_id,
          group_unique_name,
          group_name
        FROM
          T_Group
        WHERE
          group_unique_name = %(group_unique_name)s
        AND
          is_deleted = '0'
        """
        parameters = {"group_unique_name": group_unique_name}
        result = DBConnection('domain').execute_select_sql(sql, parameters)
        if len(result) != 1:
            return None
        return GroupModel(
            result[0]['group_id'],
            result[0]['group_unique_name'],
            result[0]['group_name'])

    def validate_group_info(self, group_id: int, group_unique_name: str) -> bool:
        sql = f"""
        SELECT
          'X'
        FROM
          T_Group
        WHERE
          is_deleted = '0'
        AND
          group_id = %(group_id)s
        AND
          group_unique_name = %(group_unique_name)s
        """
        parameters = {"group_id": group_id, "group_unique_name": group_unique_name}
        result = DBConnection('domain').execute_select_sql(sql, parameters)
        if len(result) != 1:
            return False
        return True