# Hardware notes

This document records integration assumptions and known limitations for the proposed bill of materials.

| Part | Intended interface | Important limitation |
|---|---|---|
| Seeed XIAO ESP32C3 | I2C, ADC, serial | Confirm board pin mapping and ADC characteristics for the exact revision. |
| MAX30102 module | I2C | Peripheral PPG/SpO2 estimates; sensor placement and motion artefacts matter. |
| LIS3DH breakout | I2C | Accelerometer readings require calibration and orientation interpretation. |
| AD8232 module | Analog output | Typically ECG/biopotential front-end, not a dedicated EEG AFE. Do not label its output EEG. |
| Conductive pads | Analog electrode interface | Electrode material does not establish EEG-grade performance or safety. |
| DRV2605L + actuator | I2C / actuator | Not enabled in the firmware; requires independent electrical and mechanical validation. |
| MAX98357A + transducer | I2S | Not enabled in the firmware; ensure audio level and hardware design are reviewed. |
| LiPo cell | Power | Requires a suitable protected charging/power-management design. Never connect a bare cell without appropriate protection. |
| fNIRS components | Additional optical channels | Not included. Requires NIR emitters, photodetectors, optical geometry, ambient-light rejection and validation. |

## Suggested integration sequence

1. Verify power rails and I2C wiring with actuators physically disconnected.
2. Bring up one sensor at a time and confirm its identity register.
3. Record timestamped raw data and assess signal quality.
4. Validate the data pipeline using synthetic and public research data.
5. Treat every new hardware channel as untrusted until independently characterized.

The firmware currently supports basic MAX30102 and LIS3DH reads plus an optional raw analog channel. It does not implement calibrated EEG or fNIRS.
