import numpy as np

class DiseaseModel:
    def predict(self, co2, hum, temp, ph):
        risk = (
            0.3*(co2/1200) +
            0.3*(hum/100) +
            0.2*(temp/40) +
            0.2*(abs(ph-6.5)/2.5)
        )
        return 1/(1+np.exp(-10*(risk-0.5)))