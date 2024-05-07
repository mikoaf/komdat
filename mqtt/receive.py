import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    if msg == "run":
        print("ok")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqttc.on_message = on_message

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)

mqttc.subscribe("komdat/dht")

mqttc.loop_forever()