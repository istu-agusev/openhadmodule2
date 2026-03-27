from edge_ai.hybrid_ai import HybridAI

def test_growth_output_range():
    ai = HybridAI()

    score = ai.growth(t=25, h=60, s=50, l=300)

    assert 0.0 <= score <= 1.0


def test_anomaly_insufficient_history():
    ai = HybridAI()

    result = ai.anomaly(10, [1, 2, 3])

    assert result == 0