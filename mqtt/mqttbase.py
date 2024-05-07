from abc import ABC, abstractmethod
from model.mqtt.response import Response
from model.mqtt.mqtt import MqttSender
from typing import Tuple

class MqttSend(ABC):
    @abstractmethod
    async def mqttMsg(self,msg:str)->Tuple[Response,MqttSender]:
        pass