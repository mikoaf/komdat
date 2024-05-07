from typing import Tuple
from model.dht import DhtResult
from model.response import Response, StatusResponse
from sensor.dhtbase import DhtBase
import asyncio
import adafruit_dht
import board

class Dht(DhtBase):
    def __init__(self) -> None:
        self.dht11_sensor = adafruit_dht.DHT11(board.D26)
    async def getData(self, msg: str) -> Tuple[Response, DhtResult]:
        try:
            hum = self.dht11_sensor.humidity
            temp = self.dht11_sensor.temperature
            return (Response(status=StatusResponse.success,message="success"), DhtResult(humidity=hum, temp=temp))
        except RuntimeError as e:
            return (Response(status=StatusResponse.failed,message=str(e)), DhtResult(humidity=0, temp=0))
        except Exception as e:
            self.dht11_sensor.exit()
            raise e
