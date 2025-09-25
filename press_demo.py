# press_demo.py
import serial, time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
time.sleep(0.2)

# 1) Open clamp
ser.write(b"servo 1 180 400\r")  # open clamp
time.sleep(1)

# 2) Lower arm (servo 3 controls up/down in most setups — adjust if needed)
ser.write(b"servo 4 970 800\r")  # move down to press
time.sleep(1)

# 3) Raise arm back
ser.write(b"servo 4 700 800\r")  # return to neutral/up
time.sleep(1)

# 4) Close clamp
ser.write(b"servo 1 700 400\r")  # close clamp
time.sleep(0.5)

ser.close()
print("Demo cycle finished")
