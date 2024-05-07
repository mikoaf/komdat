from pydantic import BaseModel

class MqttSender(BaseModel):
    topic: str
    message: str