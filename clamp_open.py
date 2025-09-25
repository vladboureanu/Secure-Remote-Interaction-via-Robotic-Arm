# clamp_open.py
import serial, time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
time.sleep(0.2)

# Open clamp
ser.write(b"servo 1 200 400\r")
ser.close()

print("Clamp opened")
