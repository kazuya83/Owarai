from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Models.RequestCommonModel import RequestCommonModel
from Models.ResponseModel import ResponseModel, Status
from Routers.CommonRouter import CommonRouter

router = APIRouter()

@router.post('get_member_list')
def get_member_list(request:RequestCommonModel):
    is_valid = CommonRouter.is_valid_corporate_user_info(request)
    if not is_valid:
        return CommonRouter.convert_response(ResponseModel(Status.BAD_REQUEST, 'リクエストに問題があります。'))
