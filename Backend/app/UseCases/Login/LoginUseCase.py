from Models.LoginModel import LoginModel
from Services.Login.LoginGroupService import LoginGroupService
from Services.Login.LoginUserService import LoginUserService
from Repositories.Login.LoginGroupRepository import LoginGroupRepository
from Repositories.Login.LoginUserRepository import LoginUserRepository
from Models.RequestCommonModel import RequestCommonModel

class LoginUseCase:
    def login(group_unique_name:str, user_unique_name:str, password:str) -> LoginModel:
        loginGroupService = LoginGroupService(LoginGroupRepository())
        group = loginGroupService.get_group_info(group_unique_name)
        if group is None:
            return None

        loginUserService = LoginUserService(LoginUserRepository(), group.group_id)
        user = loginUserService.get_group_user_info(user_unique_name, password)
        if user is None:
            return None
        
        return LoginModel(group, user)

    def is_valid_group_user_info(request:RequestCommonModel):
        loginGroupService = LoginGroupService(LoginGroupRepository())
        if not loginGroupService.get_valid_group(request.group_id, request.group_unique_name):
            return False

        loginUserService = LoginUserService(LoginUserRepository(), request.group_id)
        return loginUserService.get_valid_user(request.user_id, request.user_unique_name)