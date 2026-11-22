# Firmware

ESP32-C3 firmware for bench-level sensor acquisition.

## What it currently does

- Starts the MAX30102 over I2C and reports raw red/IR FIFO samples.
- Starts the LIS3DH over I2C and reports acceleration in g.
- Samples one configurable analog input and labels it `bio_raw`.
- Emits newline-delimited JSON records over USB serial.

## What it does not do

- It does not calculate SpO2 or heart rate from raw optical values.
- It does not measure EEG. The AD8232 channel is only an uncalibrated analog/biopotential input.
- It does not implement fNIRS.
- It does not classify sleep apnea.
- It does not activate vibration or audio outputs.

## Build

Install PlatformIO, open this folder as a PlatformIO project, then build for `xiao_esp32c3`. Confirm the board package and pin names against your installed PlatformIO version.

Before connecting sensors, verify voltage compatibility, I2C pull-ups, common ground, pin mapping and power budget. Keep actuator modules disconnected during initial testing. Never power a LiPo cell without a suitable protected power/charging circuit.

The MAX3010x SparkFun library supports the MAX30102 through the MAX30105 class name.
