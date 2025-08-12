
void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; 
  }
  Serial.println("Arduino Serial Test - Ready!");
}

void loop() {
  Serial.println("Hello from Arduino!");
  delay(1000); 
}
