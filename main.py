from sensor.dht import Dht
from mqtt.mqtt import mqtts
from model.dht.response import StatusResponse
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

Sen = Dht()
Mqtt = mqtts()

async def mqttSend():
    while True:
        dhtRead = await Sen.getData()
        print(f"\n{dhtRead}\n")
        await asyncio.sleep(1)
        if dhtRead[0].status == StatusResponse.success:
            if bool(Mqtt.getMqttMsg()):
                pubMessage = await Mqtt.mqttMsg(f"temp: {dhtRead[1].temp} hum: {dhtRead[1].humidity}")
                print(f"\n{pubMessage}\n")
            else:
                print("Data not published to broker")
        elif dhtRead[0].status == StatusResponse.failed:
            print("Failed read dht11 data and not published to broker.")
        else:
            print("Errors read dht11 data undefined.")

async def main():
    await asyncio.gather(mqttSend(),Mqtt.mqttRead(str(os.getenv("SUBSCRIBE_TOPIC"))))

asyncio.run(main())
