# press_demo.py
import serial, time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
time.sleep(0.2)

# 1) Open clamp
ser.write(b"servo 1 540 400\r")
time.sleep(1)

ser.write(b"servo 2 480 400\r")
time.sleep(1)

ser.write(b"servo 3 270 400\r")
time.sleep(1)

ser.write(b"servo 6 390 800\r")
time.sleep(1)

ser.write(b"servo 4 950 1000\r")
time.sleep(1)

ser.write(b"servo 4 700 800\r")
time.sleep(1)

# 4) Close clamp
ser.write(b"servo 1 680 400\r")
time.sleep(0.5)

ser.close()
print("Demo cycle finished")
