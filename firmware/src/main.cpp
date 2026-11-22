#include <Arduino.h>
#include <Wire.h>
#include "MAX30105.h"
#include <Adafruit_LIS3DH.h>
#include <Adafruit_Sensor.h>
#include "config.h"

MAX30105 pulseSensor;
Adafruit_LIS3DH accel;
bool pulseReady = false;
bool accelReady = false;
uint32_t lastReport = 0;

void setup() {
  Serial.begin(115200);
  delay(500);
  Wire.begin();

  Serial.println("{\"type\":\"status\",\"message\":\"boot\"}");

  pulseReady = pulseSensor.begin(Wire, I2C_SPEED_STANDARD);
  if (pulseReady) {
    // Conservative low-current configuration for bench testing.
    pulseSensor.setup(0x1F, 4, 2, 100, 411, 4096);
    pulseSensor.setPulseAmplitudeRed(0x1F);
    pulseSensor.setPulseAmplitudeIR(0x1F);
  }

  accelReady = accel.begin(LIS3DH_I2C_ADDRESS, &Wire);
  if (accelReady) {
    accel.setRange(LIS3DH_RANGE_2_G);
    accel.setDataRate(LIS3DH_DATARATE_50_HZ);
  }

  pinMode(PIN_BIO_ANALOG, INPUT);

  Serial.print("{\"type\":\"sensor_status\",\"max30102\":");
  Serial.print(pulseReady ? "true" : "false");
  Serial.print(",\"lis3dh\":");
  Serial.print(accelReady ? "true" : "false");
  Serial.println("}");
}

void loop() {
  const uint32_t now = millis();

  // Drain the optical sensor FIFO continuously to avoid stale samples.
  if (pulseReady) {
    pulseSensor.check();
  }

  if (now - lastReport >= REPORT_INTERVAL_MS) {
    lastReport = now;

    long red = -1;
    long ir = -1;
    if (pulseReady && pulseSensor.available()) {
      red = pulseSensor.getRed();
      ir = pulseSensor.getIR();
      pulseSensor.nextSample();
    }

    float ax = NAN, ay = NAN, az = NAN;
    if (accelReady) {
      sensors_event_t event;
      accel.getEvent(&event);
      // Adafruit Unified Sensor reports m/s^2. Convert to g.
      constexpr float MS2_PER_G = 9.80665f;
      ax = event.acceleration.x / MS2_PER_G;
      ay = event.acceleration.y / MS2_PER_G;
      az = event.acceleration.z / MS2_PER_G;
    }

    const int bioRaw = analogRead(PIN_BIO_ANALOG);
    // bio_raw is an uncalibrated analog channel, not an EEG measurement.
    Serial.print("{\"type\":\"sample\",\"timestamp_ms\":");
    Serial.print(now);
    Serial.print(",\"red\":"); Serial.print(red);
    Serial.print(",\"ir\":"); Serial.print(ir);
    Serial.print(",\"ax_g\":"); Serial.print(ax, 4);
    Serial.print(",\"ay_g\":"); Serial.print(ay, 4);
    Serial.print(",\"az_g\":"); Serial.print(az, 4);
    Serial.print(",\"bio_raw\":"); Serial.print(bioRaw);
    Serial.println("}");
  }

  // Intentionally no actuator commands. Haptics/audio are disabled by design.
}
