from abc import ABC,abstractmethod
from model.dht import DhtResult
from model.response import Response
from typing import Tuple
import asyncio

class DhtBase(ABC):
    @abstractmethod
    async def getData(self,msg:str)->Tuple[Response,DhtResult]:
        pass