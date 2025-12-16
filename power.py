import serial, time

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
time.sleep(0.2)

ser.write(b"servo 6 370 700\r")
time.sleep(1)
ser.write(b"servo 5 330 700\r")
time.sleep(1)
ser.write(b"servo 3 400 700\r")
time.sleep(1)
ser.write(b"servo 4 815 950\r")   # press
time.sleep(1)
ser.write(b"servo 4 700 700\r")   # release
time.sleep(1)

ser.close()
print("Power pressed")
