import abc
from Models.GroupModel import GroupModel

class ILoginGroupRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_group_info(self, group_unique_name:str) -> GroupModel:
        raise NotImplementedError()

    @abc.abstractmethod
    def validate_group_info(self, group_id:int, group_unique_name:str) -> bool:
        raise NotImplementedError()
