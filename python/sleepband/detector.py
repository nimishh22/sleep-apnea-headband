"""Transparent candidate scoring baseline; not an apnea diagnostic model."""
import math

def score_candidate(features: dict) -> float:
    """Return a 0..1 exploratory score from available descriptive features.

    The weights are placeholders for pipeline testing, not clinically derived.
    Missing channels are ignored; no event label is asserted.
    """
    contributions = []
    spo2 = features.get("spo2_pct_mean")
    if spo2 is not None and math.isfinite(float(spo2)):
        # Lower peripheral SpO2 contributes to a higher candidate score.
        contributions.append(max(0.0, min(1.0, (96.0 - float(spo2)) / 8.0)) * 0.5)

    accel_std = features.get("accel_magnitude_std")
    if accel_std is not None and math.isfinite(float(accel_std)):
        contributions.append(max(0.0, min(1.0, float(accel_std) / 0.5)) * 0.2)

    hr_std = features.get("heart_rate_bpm_std")
    if hr_std is not None and math.isfinite(float(hr_std)):
        contributions.append(max(0.0, min(1.0, float(hr_std) / 10.0)) * 0.1)

    quality_values = [
        float(v) for k, v in features.items()
        if k.endswith("_valid_fraction") and v is not None and math.isfinite(float(v))
    ]
    quality = sum(quality_values) / len(quality_values) if quality_values else 0.0
    if not contributions or quality < 0.5:
        return 0.0
    raw = sum(contributions) / len(contributions)
    return round(max(0.0, min(1.0, raw * quality)), 4)
