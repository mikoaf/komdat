from sensor.dht import Dht
import asyncio

Sen = Dht()

async def main():
    mqtt = "run"
    if mqtt == "run":
        while True:
            await asyncio.sleep(1)
            p = await Sen.getData(mqtt)
            print(p)

asyncio.run(main())