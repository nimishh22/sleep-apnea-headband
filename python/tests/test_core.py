import pandas as pd
import pytest
from sleepband.io import load_recording
from sleepband.detector import score_candidate
from sleepband.evaluation import evaluate_predictions

def test_load_recording_requires_timestamp(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("spo2_pct\n97\n")
    with pytest.raises(ValueError):
        load_recording(path)

def test_candidate_score_is_bounded_and_quality_gated():
    assert score_candidate({"spo2_pct_mean": 90, "spo2_pct_valid_fraction": 1.0}) >= 0
    assert score_candidate({"spo2_pct_mean": 90, "spo2_pct_valid_fraction": 0.2}) == 0

def test_evaluation_metrics():
    result = evaluate_predictions(pd.DataFrame({"y_true": [0, 0, 1, 1], "y_pred": [0, 1, 1, 1]}))
    assert result["tp"] == 2
    assert result["fp"] == 1
    assert result["sensitivity_recall"] == 1.0
    assert result["specificity"] == 0.5
