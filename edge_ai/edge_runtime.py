import json
import paho.mqtt.client as mqtt
from collections import deque
from hybrid_ai import HybridAI
from disease_detection import DiseaseModel

ai = HybridAI()
dm = DiseaseModel()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("mosquitto", 1883)

state = {"t": 0, "h": 0, "s": 0, "l": 0, "co2": 0, "ph": 6.5}

hist = {
    "t": deque(maxlen=100),
    "h": deque(maxlen=100),
    "co2": deque(maxlen=100),
    "ph": deque(maxlen=100),
}

def publish():
    growth = ai.growth(state["t"], state["h"], state["s"], state["l"])
    risk = dm.predict(state["co2"], state["h"], state["t"], state["ph"])

    alerts = []
    if risk > 0.7:
        alerts.append("DISEASE_RISK")
    if ai.anomaly(state["t"], list(hist["t"])) > 3:
        alerts.append("TEMP_ANOMALY")

    action = "NORMAL"
    if growth < 0.3:
        action = "IRRIGATION_BOOST"

    client.publish("edge/growth_index", growth, retain=True)
    client.publish("edge/disease_risk", risk, retain=True)
    client.publish("edge/alerts", json.dumps(alerts), retain=True)
    client.publish("edge/action", action, retain=True)


def on_message(c, u, m):
    topic = m.topic
    payload = m.payload.decode().strip()

    if payload in ["ON", "OFF", "NORMAL", "IRRIGATION_BOOST"]:
        return

    try:
        v = float(payload)
    except ValueError:
        print(f"Invalid payload: {topic} -> {payload}")
        return

    if "temp" in topic:
        state["t"] = v
        hist["t"].append(v)

    elif "humidity" in topic:
        state["h"] = v
        hist["h"].append(v)

    elif "soil" in topic:
        state["s"] = v

    elif "light" in topic:
        state["l"] = v

    elif "co2" in topic:
        state["co2"] = v
        hist["co2"].append(v)

    elif "ph" in topic:
        state["ph"] = v
        hist["ph"].append(v)

    publish()


client.subscribe("greenhouse/#")
client.on_message = on_message
client.loop_forever()