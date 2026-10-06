#include <Arduino_OV767X.h>

const int W = 176, H = 144;      // QCIF resolution
uint8_t frame[W * H];            // 8-bit grayscale

void setup() {
  Serial.begin(1000000);
  while (!Serial);
  if (!Camera.begin(QCIF, GRAYSCALE, 5)) {
    while (1);                   // camera not detected
  }
}

void loop() {
  Camera.readFrame(frame);
  Serial.write("FRAM", 4);       // marker so the PC can stay in sync
  Serial.write(frame, sizeof(frame));
}