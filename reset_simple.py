# reset_simple.py
import serial, time

# Edit these if your arm uses a different port or you want different neutral positions
SERIAL_PORT = "/dev/ttyUSB0"
BAUD = 115200

# Neutral positions, adjust numbers slightly if a servo needs micro-correction
NEUTRAL = {
    1: 700,
    2: 500,
    3: 500,
    4: 500,
    5: 500,
    6: 480,
}

ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
time.sleep(0.2)

# Each command format: servo <id> <position> <time_ms>
for sid, pos in NEUTRAL.items():
    cmd = f"servo {sid} {pos} 900\r"
    ser.write(cmd.encode())
    time.sleep(0.8)   # allow movement to complete (match time_ms loosely)

ser.close()
print("Reset to neutral positions complete")
