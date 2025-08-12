
import serial
import time

SERIAL_PORT = "COM3"
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  
    print("Connected to Arduino on", SERIAL_PORT)

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print("Arduino says:", line)
        ser.write(b"Hello Arduino\n")
        time.sleep(1)

except serial.SerialException:
    print(f"Error: Could not open serial port {SERIAL_PORT}")
except KeyboardInterrupt:
    print("\nTest stopped by user.")
finally:
    try:
        ser.close()
    except:
        pass
