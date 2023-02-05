from Repositories.Login.ILoginGroupRepository import ILoginGroupRepository
from Models.GroupModel import GroupModel

class LoginGroupService:
    def __init__(self, repository:ILoginGroupRepository):
        self.repository = repository

    def get_group_info(self, group_unique_name:str) -> GroupModel:
        return self.repository.get_group_info(group_unique_name)

    def get_valid_group(self, group_id:int, group_unique_name:str) -> bool:
        return self.repository.validate_group_info(group_id, group_unique_name)