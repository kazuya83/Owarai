import abc
from Models.UserModel import UserModel

class ILoginUserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_group_user_info(self, user_unique_name:str, password:str):
        raise NotImplementedError()

    @abc.abstractmethod
    def validate_group_user(self, user_id:int, user_uqniue_name:str) -> bool:
        raise NotImplementedError()