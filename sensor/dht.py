from typing import Tuple
from model.dht.dht import DhtResult
from model.dht.response import Response, StatusResponse
from sensor.dhtbase import DhtBase
import asyncio
import adafruit_dht
import board

class Dht(DhtBase):
    def __init__(self) -> None:
        self.dht11_sensor = adafruit_dht.DHT11(board.D4)
    async def getData(self) -> Tuple[Response, DhtResult]:
        try:
            hum = self.dht11_sensor.humidity
            temp = self.dht11_sensor.temperature
            return (Response(status=StatusResponse.success,message="success"), DhtResult(humidity=hum, temp=temp))
        except RuntimeError as error:
            return (Response(status=StatusResponse.failed,message=str(error)), DhtResult(humidity=0, temp=0))
        except Exception as e:
            self.dht11_sensor.exit()
            raise e
