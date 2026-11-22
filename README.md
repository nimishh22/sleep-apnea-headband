# Sleep Apnea Headband Research Prototype

A research-oriented software scaffold for exploring multimodal sleep signals from a wearable headband. The project separates sensor acquisition, signal-quality checks, exploratory event scoring, feedback hardware interfaces, and offline evaluation.

> **Research prototype only.** This software is not a medical device and must not be used to diagnose, treat, monitor, or make care decisions about sleep apnea. It has not been clinically validated. Haptic/audio outputs are disabled by default. Do not use the prototype on a sleeping person.

## Start here (non-technical guide)

If you are not a programmer, think of the project as a set of small jobs:

1. **Collect information:** the headband's electronics read measurements from sensors.
2. **Clean the information:** software checks whether readings are usable and reduces ordinary measurement noise.
3. **Look for patterns:** an experimental algorithm calculates indicators that researchers can inspect. It does not decide whether someone has sleep apnea.
4. **Record results:** the evaluation tools compare algorithm output with labelled research data so the team can measure errors.
5. **Optional feedback hardware:** a separate module contains a controlled interface for vibration/audio experiments. It is disabled unless deliberately configured.

### What each important file does

| File | In plain language |
|---|---|
| `firmware/platformio.ini` | Tells PlatformIO which microcontroller board and software libraries to use. |
| `firmware/include/config.h` | Central place for pin assignments, sensor addresses and safe default settings. |
| `firmware/src/main.cpp` | Runs on the ESP32-C3. Starts the sensors, reads measurements, timestamps them and prints structured data over USB serial. |
| `firmware/README.md` | Explains how the electronics firmware is built and what hardware assumptions it makes. |
| `python/sleepband/io.py` | Reads recorded sensor samples from CSV files. |
| `python/sleepband/signal.py` | Performs basic filtering and checks whether a signal has enough usable data. |
| `python/sleepband/features.py` | Turns raw measurements into simple numerical summaries for research. |
| `python/sleepband/detector.py` | Produces experimental event-candidate scores. These scores are not diagnoses. |
| `python/sleepband/evaluation.py` | Compares predictions with researcher-provided labels and calculates performance statistics. |
| `python/sleepband/cli.py` | Provides simple terminal commands to inspect a recording and evaluate predictions. |
| `python/tests/` | Small automated checks that help catch software mistakes. |
| `docs/HARDWARE_NOTES.md` | Explains important limitations of the proposed sensor parts. |
| `docs/SAFETY.md` | Describes what the prototype must not be used for and its safety boundaries. |
| `docs/DATA_FORMAT.md` | Explains the CSV columns expected by the analysis tools. |

## Hardware notes you should know

- **MAX30102:** peripheral optical pulse/SpO2 sensor. It does not measure oxygen directly inside the brain.
- **LIS3DH:** three-axis accelerometer; useful for movement/orientation research.
- **AD8232:** commonly used as a single-channel ECG/biopotential front-end. It is not a dedicated EEG amplifier and this repository does not claim EEG measurement from it.
- **Dry electrodes:** electrode material alone does not make the front-end suitable for EEG.
- **fNIRS:** would require additional near-infrared light sources, photodetectors, optical design and validation. It is not implemented here.
- **Haptic/audio hardware:** firmware outputs are disabled by default and are not an apnea treatment.

## Quick start: analysis software

Requires Python 3.10 or newer.

```bash
cd python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

Inspect a CSV recording:

```bash
sleepband inspect ../data/example_recording.csv
```

Evaluate a CSV containing reference labels and model predictions:

```bash
sleepband evaluate ../data/evaluation_example.csv
```

The example files contain synthetic demonstration data, not patient recordings.

## Firmware

Open `firmware/` with PlatformIO. Review `firmware/include/config.h` and the wiring guide before connecting anything. The default firmware reports sensor data only. It does not activate vibration or audio.

## Current status

This is an initial research scaffold. It does not include a trained model, validated apnea detector, clinical-grade EEG acquisition, fNIRS acquisition, or a validated closed-loop intervention. Performance targets must be treated as hypotheses until tested on an appropriately governed, independent dataset.

See [Competition guide](docs/COMPETITION_GUIDE.md), [Project status](docs/PROJECT_STATUS.md), [Validation protocol](docs/VALIDATION_PROTOCOL.md), [Safety](docs/SAFETY.md), [Hardware notes](docs/HARDWARE_NOTES.md), and [Data format](docs/DATA_FORMAT.md).
