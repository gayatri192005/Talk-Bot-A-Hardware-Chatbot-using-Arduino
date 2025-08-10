# File: serial_comm.py
# Purpose: Send commands to Arduino via Serial Port.

import serial
import time

class ArduinoComm:
    def __init__(self, port="COM3", baud=9600):
        self.port = port
        self.baud = baud
        try:
            self.arduino = serial.Serial(port, baud, timeout=1)
            time.sleep(2)  # Wait for connection
            print(f"✅ Connected to Arduino on {port}")
        except serial.SerialException:
            print(f"❌ Could not connect to Arduino on {port}")
            self.arduino = None

    def send_command(self, cmd):
        if self.arduino:
            self.arduino.write((cmd + "\n").encode())
            print(f"📤 Sent: {cmd}")
            time.sleep(0.1)
        else:
            print("⚠️ No Arduino connection.")

    def close(self):
        if self.arduino:
            self.arduino.close()
            print("🔌 Arduino connection closed.")

if __name__ == "__main__":
    arduino = ArduinoComm("COM3", 9600)
    arduino.send_command("LED_ON")
    time.sleep(1)
    arduino.send_command("LED_OFF")
    arduino.close()
