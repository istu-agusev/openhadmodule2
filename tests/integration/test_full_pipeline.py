import time
import paho.mqtt.client as mqtt

MQTT_HOST = "mosquitto"

results = {
    "growth": None,
    "risk": None,
    "alerts": None,
    "action": None
}

def on_message(client, userdata, msg):
    payload = msg.payload.decode()

    if msg.topic == "edge/growth_index":
        results["growth"] = float(payload)

    elif msg.topic == "edge/disease_risk":
        results["risk"] = float(payload)

    elif msg.topic == "edge/alerts":
        results["alerts"] = payload

    elif msg.topic == "edge/action":
        results["action"] = payload


def test_full_pipeline_flow():
    client = mqtt.Client()
    client.on_message = on_message

    client.connect(MQTT_HOST, 1883)
    client.subscribe("edge/#")

    client.loop_start()

    time.sleep(15)

    client.loop_stop()

    assert results["growth"] is not None
    assert results["risk"] is not None
    assert isinstance(results["alerts"], str)
    assert results["action"] in ["NORMAL", "IRRIGATION_BOOST"]