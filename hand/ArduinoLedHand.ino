int ledPins[] = {7, 6, 5, 4, 3};

void setup() {
  // Set the LED pins as outputs
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  
  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Blink the specified LEDs based on the input command
    if (command >= '1' && command <= '5') {
      int startLED = 3; // Default starting LED
      
      // Determine the starting LED based on the input command
      switch(command) {
        case '1':
          startLED = 3;
          break;
        case '2':
          startLED = 3;
          break;
        case '3':
          startLED = 3;
          break;
        case '4':
          startLED = 2; // Adjusted for LED indexing
          break;
        case '5':
          startLED = 1; // Adjusted for LED indexing
          break;
      }
      
      int endLED = command - '0' + 2; // Convert char to int and adjust for end LED
      
      // Turn on specified LEDs
      for (int i = startLED; i <= endLED; i++) {
        digitalWrite(ledPins[i - 1], HIGH); // Adjusted for LED indexing
      }
      
      delay(50); // Wait for 50 milliseconds
      
      // Turn off specified LEDs
      for (int i = startLED; i <= endLED; i++) {
        digitalWrite(ledPins[i - 1], LOW); // Adjusted for LED indexing
      }
    }
  }
}
