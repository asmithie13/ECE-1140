// Arduino IDE:
// File -> Examples -> 04.Communication -> PhysicalPixel

const int doorLeft = 10; // pin the LED is attached to
const int doorRight = 11;
const int headLights = 12;
const int cabinLights = 13;
int incomingByte;      // variable stores  serial data

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(doorLeft, OUTPUT);
  pinMode(doorRight, OUTPUT);
  pinMode(headLights, OUTPUT);
  pinMode(cabinLights, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();

    if (incomingByte == 'A') {
      digitalWrite(doorLeft, HIGH);
    }
    if (incomingByte == 'B') {
      digitalWrite(doorLeft, LOW);
    }

    if (incomingByte == 'C') {
      digitalWrite(doorRight, HIGH);
    }
    if (incomingByte == 'D') {
      digitalWrite(doorRight, LOW);
    }
    if (incomingByte == 'E') {
      digitalWrite(headLights, HIGH);
    }
    if (incomingByte == 'F') {
      digitalWrite(headLights, LOW);
    }
    if (incomingByte == 'G') {
      digitalWrite(cabinLights, HIGH);
    }
    if (incomingByte == 'H') {
      digitalWrite(cabinLights, LOW);
    }
  }
}