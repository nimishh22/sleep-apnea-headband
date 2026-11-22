from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"timestamp_s"}

def load_recording(path: str | Path) -> pd.DataFrame:
    """Load a CSV recording and validate its basic time axis."""
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    frame = frame.sort_values("timestamp_s").reset_index(drop=True)
    if frame["timestamp_s"].isna().any():
        raise ValueError("timestamp_s contains missing values")
    if len(frame) > 1 and (frame["timestamp_s"].diff().dropna() <= 0).any():
        raise ValueError("timestamp_s must be strictly increasing")
    return frame
