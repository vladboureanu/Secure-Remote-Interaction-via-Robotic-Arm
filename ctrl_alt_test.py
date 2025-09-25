# ctrl_alt_test.py
import serial, time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
time.sleep(0.2)

OPEN = 200   # clamp open
CLOSE = 700  # clamp closed
DELAY = 1.0  # seconds between moves

print("Pressing sequence started (Ctrl/Alt). Ctrl+C to stop.")

while True:
    ser.write(b"servo 1 %d 400\r" % OPEN)
    time.sleep(DELAY)
    ser.write(b"servo 1 %d 400\r" % CLOSE)
    time.sleep(DELAY)
