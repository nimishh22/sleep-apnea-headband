#pragma once

#include <Arduino.h>

// Verify every pin against the exact XIAO ESP32C3 board revision and wiring.
// These are configurable placeholders, not a wiring certification.
static constexpr uint8_t PIN_BIO_ANALOG = A0;

// I2C addresses are the common defaults for these devices.
static constexpr uint8_t MAX30102_I2C_ADDRESS = 0x57;
static constexpr uint8_t LIS3DH_I2C_ADDRESS = 0x18;

// Outputs remain disabled in the research scaffold.
static constexpr bool ENABLE_HAPTIC_OUTPUT = false;
static constexpr bool ENABLE_AUDIO_OUTPUT = false;

// Serial reporting interval.
static constexpr uint32_t REPORT_INTERVAL_MS = 100;
