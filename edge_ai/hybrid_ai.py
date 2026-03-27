import numpy as np

class HybridAI:
    def growth(self, t, h, s, l):
        score = 0.3*t/40 + 0.3*h/100 + 0.3*s/100 + 0.1*l/1000
        return 1/(1+np.exp(-10*(score-0.5)))

    def anomaly(self, x, hist):
        if len(hist) < 10:
            return 0
        arr = np.array(hist)
        return abs((x - arr.mean()) / (arr.std()+1e-6))