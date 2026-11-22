# Safety and intended use

This repository is an engineering and data-analysis research scaffold. It is not a medical device, diagnostic system, treatment, or substitute for professional medical assessment.

## Hard boundaries

- Do not use this prototype to diagnose, rule out, monitor, or treat sleep apnea.
- Do not run human sleep experiments with this unvalidated hardware/software.
- Do not activate haptic or audio outputs on a person. They are disabled in the firmware by default.
- Do not use algorithm scores to make health decisions.
- Do not infer clinical sensitivity, specificity, or treatment benefit from synthetic data.
- Follow institutional ethics review, informed-consent requirements, privacy rules, and qualified supervision before any human-subject research.
- Use properly de-identified, appropriately licensed research datasets and respect their terms.

## Signal limitations

The MAX30102 provides peripheral optical measurements and estimates; it is not a direct brain oxygen sensor. The AD8232 is not a dedicated EEG acquisition front-end. Movement, sensor contact, ambient light, perfusion, electrical interference, and timing errors can make signals unreliable.

The current event scorer is intentionally transparent and experimental. It generates candidate scores from supplied features and must not be described as an apnea diagnosis.

## Feedback outputs

Firmware defaults keep haptics and audio disabled. The current code does not implement a clinical closed-loop intervention, phase-locked stimulation, or a guaranteed response time. Any future actuator study requires a separate safety review and hardware validation.
