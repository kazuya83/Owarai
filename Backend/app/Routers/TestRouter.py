from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Models.RequestCommonModel import RequestCommonModel
from Models.ResponseModel import ResponseModel, Status

router = APIRouter()

@router.post('/get_test')
def get_test(request:RequestCommonModel):
    return convert_response(ResponseModel(Status.BAD_REQUEST, 'リクエストに問題があります。'))

def convert_response(response:ResponseModel):
    json_compatible_data = jsonable_encoder(response)
    return JSONResponse(content=json_compatible_data)