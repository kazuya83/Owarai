from pydantic import BaseModel

class RequestCommonModel(BaseModel):
    group_id:int
    group_unique_name:str
    user_id:int
    user_unique_name:str