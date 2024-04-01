#include <Servo.h>

Servo servo;

const int trigPin = 13;
const int echoPin = 12;

const int servoPin = 11;

const int enAPin = 6;
const int in1Pin = 7;
const int in2Pin = 5;
const int in3Pin = 4;
const int in4Pin = 2;
const int enBPin = 3;

enum Motor { LEFT, RIGHT };

void go(enum Motor m, int speed) {
  if (m == LEFT) {
    digitalWrite(in1Pin, speed > 0 ? HIGH : LOW);
    digitalWrite(in2Pin, speed <= 0 ? HIGH : LOW);
    analogWrite(enAPin, speed < 0 ? -speed : speed);
  } else if (m == RIGHT) {
    digitalWrite(in3Pin, speed > 0 ? HIGH : LOW);
    digitalWrite(in4Pin, speed <= 0 ? HIGH : LOW);
    analogWrite(enBPin, speed < 0 ? -speed : speed);
  }
}


void testMotors() {
  static int speed[8] = {128, 255, 128, 0, -128, -255, -128, 0};
  go(RIGHT, 0);
  for (unsigned char i = 0; i < 8; i++)
    go(LEFT, speed[i]), delay(200);
  for (unsigned char i = 0; i < 8; i++)
    go(RIGHT, speed[i]), delay(200);
}

unsigned int readDistance() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  unsigned long period = pulseIn(echoPin, HIGH);
  return period * 343 / 2000;
}

#define NUM_ANGLES 7
unsigned char sensorAngle[NUM_ANGLES] = {60, 70, 80, 90, 100, 110, 120};
unsigned int distance[NUM_ANGLES];

void readNextDistance() {
  static unsigned char angleIndex = 0;
  static signed char step = 1;
  distance[angleIndex] = readDistance();
  angleIndex += step;
  if (angleIndex == NUM_ANGLES - 1)
    step = -1;
  else if (angleIndex == 0)
    step = 1;
  servo.write(sensorAngle[angleIndex]);
}

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  digitalWrite(trigPin, LOW);

  pinMode(enAPin, OUTPUT);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  pinMode(enBPin, OUTPUT);

  servo.attach(servoPin);
  servo.write(90);

  go(LEFT, 0);
  go(RIGHT, 0);
  testMotors();

  servo.write(sensorAngle[0]);
  delay(200);
  for (unsigned char i = 0; i < NUM_ANGLES; i++)
    readNextDistance(), delay(200);
}

void loop() {
  readNextDistance();
  bool tooClose = false;
  
  for (unsigned char i = 0; i < NUM_ANGLES; i++) {
    if (distance[i] < 300) {
      tooClose = true;
    }
    Serial.print("Distance ");
    Serial.print(i);
    Serial.print(": ");
    Serial.print(distance[i]);
    Serial.print("  ");
  }

  if (tooClose) {
    go(LEFT, 180);
    go(RIGHT,180);
  } else {
    go(LEFT, -180);
    go(RIGHT,-180);
  }
  delay(50);
  Serial.println(); // Print a newline after printing distance values
}
