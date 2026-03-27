import random
import time
import paho.mqtt.client as mqtt

c = mqtt.Client()
c.connect("mosquitto", 1883)

while True:
    data = {
        "air_temp": random.uniform(16,32),
        "air_humidity": random.uniform(40,90),
        "soil_humidity": random.uniform(25,80),
        "soil_temp": random.uniform(10,30),
        "light": random.uniform(50,900),
        "co2": random.uniform(300,1200),
        "ph": random.uniform(5.5,7.5)
    }

    for k,v in data.items():
        c.publish(f"greenhouse/{k}", v)

    time.sleep(5)