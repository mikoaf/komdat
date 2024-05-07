from abc import ABC,abstractmethod
from model.dht.dht import DhtResult
from model.dht.response import Response
from typing import Tuple
import asyncio

class DhtBase(ABC):
    @abstractmethod
    async def getData(self,msg:str)->Tuple[Response,DhtResult]:
        pass