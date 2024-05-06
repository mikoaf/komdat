from typing import Tuple
from model.dht import DhtResult
from model.response import Response, StatusResponse
from sensor.dhtbase import DhtBase
import asyncio

class Dht(DhtBase):
    async def getData(self, msg: str) -> Tuple[Response, DhtResult]:
        lah = 8.9
        leh = 32
        return (Response(status=StatusResponse.success,message="success"), DhtResult(humidity=lah, temp=leh))
