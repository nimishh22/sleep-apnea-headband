import numpy as np
import pytest
from sleepband.signal import bandpass, signal_quality

def test_signal_quality_flags_empty_and_valid():
    assert signal_quality([])["usable"] is False
    result = signal_quality([1.0, 2.0, 3.0, 4.0])
    assert result["valid_fraction"] == 1.0
    assert result["usable"] is True

def test_bandpass_rejects_invalid_nyquist():
    with pytest.raises(ValueError):
        bandpass(np.ones(100), sample_rate_hz=10, low_hz=1, high_hz=6)

def test_bandpass_returns_finite_signal():
    t = np.arange(500) / 50
    x = np.sin(2 * np.pi * 2 * t) + 0.2 * np.sin(2 * np.pi * 15 * t)
    filtered = bandpass(x, sample_rate_hz=50, low_hz=1, high_hz=4)
    assert filtered.shape == x.shape
    assert np.isfinite(filtered).all()
