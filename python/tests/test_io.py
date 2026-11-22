import pytest
from sleepband.io import load_recording

def test_load_recording_rejects_duplicate_timestamps(tmp_path):
    path = tmp_path / "duplicate.csv"
    path.write_text("timestamp_s\n0\n1\n1\n")
    with pytest.raises(ValueError, match="strictly increasing"):
        load_recording(path)

def test_load_recording_sorts_rows(tmp_path):
    path = tmp_path / "unsorted.csv"
    path.write_text("timestamp_s,value\n2,20\n0,0\n1,10\n")
    frame = load_recording(path)
    assert frame["timestamp_s"].tolist() == [0, 1, 2]
