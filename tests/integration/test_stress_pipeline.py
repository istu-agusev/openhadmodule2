import time
import paho.mqtt.client as mqtt
import random

MQTT_HOST = "mosquitto"

def test_mqtt_stress():
    client = mqtt.Client()
    client.connect(MQTT_HOST, 1883)

    start = time.time()

    for _ in range(200):
        client.publish("greenhouse/air_temp", str(random.uniform(10, 40)))
        client.publish("greenhouse/air_humidity", str(random.uniform(30, 90)))
        client.publish("greenhouse/co2", str(random.uniform(300, 1500)))

    elapsed = time.time() - start

    assert elapsed < 10