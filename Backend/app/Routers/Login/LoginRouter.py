from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Models.RequestCommonModel import RequestCommonModel
from Models.ResponseModel import ResponseModel, Status
from UseCases.Login.LoginUseCase import LoginUseCase

router = APIRouter()

class LoginForm(BaseModel):
    group_unique_name:str
    user_unique_name:str
    password:str

@router.post('/Login')
def Login(request:LoginForm):
    response = ResponseModel(Status.OK, 'ログイン成功')
    try:
        group_unique_name = request.group_unique_name
        user_unique_name = request.user_unique_name
        password = request.password
    except Exception as e:
        response.status_code = Status.BAD_REQUEST
        response.message = '入力内容に不足があります。'
        return response

    login_info = LoginUseCase.login(group_unique_name, user_unique_name, password)
    if login_info is None:
        response.status_code = Status.OK
        response.message = 'ログイン情報に誤りがあります。'
        return response
    response.data = login_info
    json_compatible_data = jsonable_encoder(response)
    return JSONResponse(content=json_compatible_data)