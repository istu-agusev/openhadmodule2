import time
import paho.mqtt.client as mqtt

received = []

def on_message(client, userdata, msg):
    received.append((msg.topic, msg.payload.decode()))

def test_mqtt_flow():
    client = mqtt.Client()
    client.on_message = on_message

    client.connect("mosquitto", 1883)
    client.subscribe("edge/#")

    client.loop_start()

    # емулюємо сенсор
    client.publish("greenhouse/air_temp", "25")
    client.publish("greenhouse/air_humidity", "60")

    time.sleep(3)

    client.loop_stop()

    topics = [t for t, _ in received]

    assert any("edge/growth_index" in t for t in topics)