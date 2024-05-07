from pydantic import BaseModel
from enum import Enum
from typing import Optional

class StatusResponse(Enum):
    success, failed, error = range(3)

class Response(BaseModel):
    status: StatusResponse
    message: Optional[str] = None
