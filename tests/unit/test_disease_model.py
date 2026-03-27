import numpy as np
from edge_ai.disease_detection import DiseaseModel

def test_disease_model_output_range():
    model = DiseaseModel()

    risk = model.predict(co2=600, hum=50, temp=22, ph=6.5)

    assert 0.0 <= risk <= 1.0


def test_disease_model_high_risk():
    model = DiseaseModel()

    risk = model.predict(co2=1200, hum=100, temp=40, ph=4.0)

    assert risk > 0.5