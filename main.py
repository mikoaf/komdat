from sensor.dht import Dht
from mqtt.mqtt import mqtts
import asyncio

Sen = Dht()
Mqtt = mqtts()


async def main():
    while True:
        await asyncio.sleep(1)
        p = await Sen.getData()
        print(p)
        if p[0].message == "success":
            res = await Mqtt.mqttMsg(f"temp: {p[1].temp} hum: {p[1].humidity}")
            print(res)
        elif p[0].message == "failed":
            print("failed")
        else:
            print("errors undefined")

asyncio.run(main())