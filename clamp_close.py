# clamp_close.py
import serial, time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
time.sleep(0.2)

# Close clamp (servo 1 → position 700)
ser.write(b"servo 1 700 400\r")
ser.close()

print("Clamp closed")
