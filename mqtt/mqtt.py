from typing import Tuple
from model.mqtt.response import Response, StatusResponse
from model.mqtt.mqtt import MqttSender
from mqtt.mqttbase import MqttSend
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

class mqtts(MqttSend):
    async def mqttMsg(self,msg:str)->Tuple[Response,MqttSender]:
        try:
            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            client.connect(str(os.getenv("MQTT_BROKER")), int(os.getenv("MQTT_PORT")), 60)
            message = msg
            topic = str(os.getenv("PUBLISH_TOPIC"))
            client.publish(topic, message)
            client.disconnect()
            return (Response(status=StatusResponse.success,message="success"), MqttSender(topic=topic,message=message))
        except Exception as e:
            return (Response(status=StatusResponse.failed,message=str(e)), MqttSender(topic="",message=""))