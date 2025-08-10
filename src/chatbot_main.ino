// File: chatbot_main.ino
// Project: Arduino Hardware Chatbot
// Author: Luv Agarwal
// Description: Arduino listens to commands from Python chatbot and controls hardware accordingly.

#include <Servo.h>

// Pin Definitions
Servo servoMotor;
const int ledPin = 3;
const int buzzerPin = 4;

// Variable to store incoming command
String command = "";

void setup() {
  Serial.begin(9600); // Baud rate must match Python side
  servoMotor.attach(9); // Servo on pin 9
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  Serial.println("Arduino Chatbot Ready");
}

void loop() {
  // Check if there is data from Python
  if (Serial.available()) {
    command = Serial.readStringUntil('\n'); // Read until newline
    command.trim(); // Remove extra spaces

    // LED Control
    if (command == "LED_ON") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned ON");
    }
    else if (command == "LED_OFF") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned OFF");
    }
    // Buzzer Control
    else if (command == "BUZZER_ON") {
      digitalWrite(buzzerPin, HIGH);
      delay(200);
      digitalWrite(buzzerPin, LOW);
      Serial.println("Buzzer beeped");
    }
    // Servo Control
    else if (command.startsWith("SERVO_")) {
      int angle = command.substring(6).toInt();
      if (angle >= 0 && angle <= 180) {
        servoMotor.write(angle);
        Serial.println("Servo moved to " + String(angle) + " degrees");
      } else {
        Serial.println("Invalid servo angle");
      }
    }
    // Unknown Command
    else {
      Serial.println("Unknown command: " + command);
    }
  }
}
