# press_demo.py
import serial, time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
time.sleep(0.2)

# 1) Open clamp
ser.write(b"servo 1 180 400\r")
time.sleep(1)

# 2) Lower arm (servo controls up/down in most setups — adjust if needed)
ser.write(b"servo 4 970 800\r")
time.sleep(1)

# 3) Raise arm back
ser.write(b"servo 4 700 800\r")
time.sleep(1)

# 4) Close clamp
ser.write(b"servo 1 700 400\r")
time.sleep(0.5)

ser.close()
print("Demo cycle finished")
