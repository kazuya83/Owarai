from Models.GroupModel import GroupModel
from Models.UserModel import UserModel

class LoginModel:
    def __init__(self, group_info:GroupModel, user_info: UserModel):
        self.group_info = group_info
        self.user_info = user_info
