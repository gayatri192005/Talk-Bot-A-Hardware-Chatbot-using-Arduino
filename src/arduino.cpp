#include <Servo.h>

// Components
Servo servoMotor;
int ledPin = 3;
int buzzerPin = 4;

// Variables
String command = "";

void setup() {
  Serial.begin(9600); // Baud rate must match Python code
  servoMotor.attach(9);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  Serial.println("Arduino Chatbot Ready");
}

void loop() {
  // Check if Python sent a command
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "LED_ON") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned ON");
    }
    else if (command == "LED_OFF") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned OFF");
    }
    else if (command == "BUZZER_ON") {
      digitalWrite(buzzerPin, HIGH);
      delay(200);
      digitalWrite(buzzerPin, LOW);
      Serial.println("Buzzer Beep");
    }
    else if (command.startsWith("SERVO_")) {
      int angle = command.substring(6).toInt();
      servoMotor.write(angle);
      Serial.println("Servo moved to " + String(angle) + " degrees");
    }
    else {
      Serial.println("Unknown command: " + command);
    }
  }
}
