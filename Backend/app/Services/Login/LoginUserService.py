from Repositories.Login.ILoginUserRepository import ILoginUserRepository
from Models.UserModel import UserModel

class LoginUserService:
    def __init__(self, repository:ILoginUserRepository, group_id:int):
        self.repository = repository
        self.group_id = group_id

    def get_group_user_info(self, user_unique_name:str, password:str) -> UserModel:
        return self.repository.get_group_user_info(self.group_id, user_unique_name, password)

    def get_valid_user(self, user_id:int, user_unique_name:str) -> bool:
        return self.repository.validate_group_user(self.group_id, user_id, user_unique_name)