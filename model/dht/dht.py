from pydantic import BaseModel

class DhtResult(BaseModel):
    humidity:float
    temp:float