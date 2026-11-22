import pandas as pd
from sleepband.features import extract_window_features

def test_extract_features_from_accelerometer():
    frame = pd.DataFrame({
        "ax_g": [0.0, 0.1], "ay_g": [0.0, 0.0], "az_g": [1.0, 1.0],
        "spo2_pct": [97.0, 96.0]
    })
    result = extract_window_features(frame)
    assert result["sample_count"] == 2
    assert "accel_magnitude_std" in result
    assert result["spo2_pct_mean"] == 96.5
