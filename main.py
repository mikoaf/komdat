from sensor.dht import Dht
import asyncio

Sen = Dht()

async def main():
    mqtt = "run"
    if mqtt == "run":
        p = await Sen.getData(mqtt)
        print(p)

asyncio.run(main())

