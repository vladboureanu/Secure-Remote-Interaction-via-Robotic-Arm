# reset_all.py
import glob, serial, time, sys

def find_port():
    for p in ("/dev/ttyUSB*", "/dev/ttyACM*"):
        ports = sorted(glob.glob(p))
        if ports:
            return ports[0]
    sys.exit("No serial ports found. Check USB-C and PSU are ON.")

PORT = find_port()
BAUD = 115200

# === Your adjusted neutral positions and move time ===
NEUTRAL_POS = {1:700, 2:500, 3:500, 4:500, 5:500, 6:480}
MOVE_TIME_MS = 900
# ======================================================

def send(ser, sid, pos, t=MOVE_TIME_MS, wait=0.65):
    cmd = f"servo {sid} {pos} {t}\r\n"
    print("->", cmd.strip())
    ser.write(cmd.encode())
    time.sleep(wait)

def main():
    print(f"[INFO] Using port {PORT}")
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(0.2)
    print("Sending neutral positions...")
    for sid, pos in NEUTRAL_POS.items():
        send(ser, sid, pos, MOVE_TIME_MS, wait=0.65)
    ser.close()
    print("Done. Arm is in neutral pose.")

if __name__ == "__main__":
    main()
