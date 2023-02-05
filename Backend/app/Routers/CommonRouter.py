from Models.ResponseModel import ResponseModel, Status
from Models.RequestCommonModel import RequestCommonModel
from UseCases.Login.LoginUseCase import LoginUseCase
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class CommonRouter:
    def is_valid_user_info(request:RequestCommonModel):
        is_valid = LoginUseCase.is_valid_group_user_info(request)
        if not is_valid:
            return CommonRouter.bad_request_response()
        return None

    def bad_request_response():
        return CommonRouter.convert_response(ResponseModel(Status.BAD_REQUEST, 'リクエストに問題があります。'))

    def ok_request_response(message:str, return_value:object):
        return CommonRouter.convert_response(ResponseModel(Status.OK, message, return_value))

    def convert_response(response:ResponseModel):
        json_compatible_data = jsonable_encoder(response)
        return JSONResponse(content=json_compatible_data)