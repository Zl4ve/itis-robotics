#include <Servo.h>

const int SERVO_PIN_1 = 4;
const int SERVO_PIN_2 = 2;
Servo servo;
Servo servo1;

void setup() {
  servo.attach(SERVO_PIN_1);
  servo1.attach(SERVO_PIN_2);
}

void loop() {
  servo.write(45);
  servo1.write(120); 
}
