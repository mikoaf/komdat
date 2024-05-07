from typing import Tuple
from model.mqtt.response import Response, StatusResponse
from model.mqtt.mqtt import MqttSender
from mqtt.mqttbase import MqttSend
import paho.mqtt.client as mqtt

class mqtts(MqttSend):
    async def mqttMsg(self,msg:str)->Tuple[Response,MqttSender]:
        try:
            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            client.connect("mqtt.eclipseprojects.io", 1883, 60)
            message = msg
            topic = "komdat/dht"
            client.publish(topic, message)
            client.disconnect()
            return (Response(status=StatusResponse.success,message="success"), MqttSender(topic=topic,message=message))
        except Exception as e:
            return (Response(status=StatusResponse.failed,message=str(e)), MqttSender(topic="",message=""))