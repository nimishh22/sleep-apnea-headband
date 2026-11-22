import numpy as np
from scipy.signal import butter, sosfiltfilt

def bandpass(values, sample_rate_hz: float, low_hz: float, high_hz: float, order: int = 3):
    """Zero-phase Butterworth bandpass for offline analysis only."""
    x = np.asarray(values, dtype=float)
    if sample_rate_hz <= 0 or not 0 < low_hz < high_hz < sample_rate_hz / 2:
        raise ValueError("Require 0 < low < high < Nyquist and positive sample rate")
    if x.size < max(16, 3 * (2 * order + 1)):
        raise ValueError("Not enough samples for stable offline filtering")
    if not np.isfinite(x).all():
        raise ValueError("Input contains non-finite values")
    sos = butter(order, [low_hz, high_hz], btype="bandpass", fs=sample_rate_hz, output="sos")
    return sosfiltfilt(sos, x)

def signal_quality(values) -> dict:
    """Return simple finite-data diagnostics, not a clinical quality score."""
    x = np.asarray(values, dtype=float)
    finite = np.isfinite(x)
    valid_fraction = float(finite.mean()) if x.size else 0.0
    valid = x[finite]
    return {
        "sample_count": int(x.size),
        "valid_fraction": valid_fraction,
        "usable": bool(valid.size >= 2 and valid_fraction >= 0.9 and np.std(valid) > 0),
    }
