import json
from edge_ai.edge_runtime import publish, state, hist, dm, ai

def test_publish_runs_without_crash(monkeypatch):
    # мок MQTT publish
    class DummyClient:
        def publish(self, *args, **kwargs):
            return True

    import edge_ai.edge_runtime as runtime
    runtime.client = DummyClient()

    state.update({
        "t": 25,
        "h": 60,
        "s": 40,
        "l": 300,
        "co2": 600,
        "ph": 6.5
    })

    publish()


def test_alert_generation(monkeypatch):
    class DummyClient:
        def publish(self, *args, **kwargs):
            return True

    import edge_ai.edge_runtime as runtime
    runtime.client = DummyClient()

    state["t"] = 50  # аномально висока температура
    state["h"] = 10
    state["co2"] = 1500

    publish()