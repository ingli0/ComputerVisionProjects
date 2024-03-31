import serial
import time


def blink_led(pin):
    try:
        # Open serial connection with Arduino
        arduino = serial.Serial('COM3', 9600, timeout=1)  # Change 'COM3' to your port
        time.sleep(2)  # Allow some time for Arduino to initialize

        while True:
            # Send command to Arduino to blink LED on the specified pin
            arduino.write(str(pin).encode())
            print(f"Blinking LED on pin {pin} for 2 seconds...")

            # Wait for 2 seconds
            time.sleep(2)

            # Send command to turn off LED
            arduino.write(b'0')
            print("LED turned off.")



            # Prompt user to enter LED pin number again
            pin = int(input("Enter the LED pin number (e.g., 7): "))

        # Close serial connection (unreachable in this example)
        arduino.close()

    except serial.SerialException:
        print("Error: Could not open serial port. Make sure the port is correct and the Arduino is connected.")


if __name__ == "__main__":
    pin = int(input("Enter the LED pin number (e.g., 7): "))
    blink_led(pin)
