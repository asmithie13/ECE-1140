// Arduino IDE: 
// File -> Examples -> 04.Communication -> PhysicalPixel

const int ledCross = 11; // pin the LED is attached to
const int ledSwitch = 12;
const int ledLight = 13;
int incomingByte;      // variable stores  serial data

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledCross, OUTPUT);
  pinMode(ledSwitch, OUTPUT);
  pinMode(ledLight, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
  
    if (incomingByte == 'A') {
      digitalWrite(ledCross, HIGH);
    }
    if (incomingByte == 'B') {
      digitalWrite(ledCross, LOW);
    }

    if (incomingByte == 'C') {
      digitalWrite(ledSwitch, HIGH);
      digitalWrite(ledLight, HIGH);
    }
    if (incomingByte == 'D') {
      digitalWrite(ledSwitch, LOW);
      digitalWrite(ledLight, LOW);
    }

  }
}