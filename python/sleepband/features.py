import numpy as np
import pandas as pd

def extract_window_features(window: pd.DataFrame) -> dict:
    """Extract transparent descriptive features from one time window."""
    result = {"sample_count": int(len(window))}
    for col in ("spo2_pct", "heart_rate_bpm", "ax_g", "ay_g", "az_g", "bio_raw"):
        if col in window:
            x = pd.to_numeric(window[col], errors="coerce").dropna().to_numpy(dtype=float)
            result[f"{col}_mean"] = float(np.mean(x)) if x.size else float("nan")
            result[f"{col}_std"] = float(np.std(x)) if x.size else float("nan")
            result[f"{col}_valid_fraction"] = float(x.size / max(1, len(window)))
    if all(c in window for c in ("ax_g", "ay_g", "az_g")):
        xyz = window[["ax_g", "ay_g", "az_g"]].apply(pd.to_numeric, errors="coerce")
        magnitude = np.sqrt((xyz ** 2).sum(axis=1)).dropna().to_numpy()
        result["accel_magnitude_std"] = float(np.std(magnitude)) if magnitude.size else float("nan")
    return result
