# interactive_typing_helper.py
import glob, serial, time, sys
from pprint import pprint

def find_port():
    for p in ("/dev/ttyUSB*", "/dev/ttyACM*"):
        ports = sorted(glob.glob(p))
        if ports:
            return ports[0]
    sys.exit("No serial ports found. Check USB-C and PSU are ON.")

PORT = find_port()
BAUD = 115200
T_DEFAULT = 700

# Neutral defaults (keep in sync with reset_all.py)
NEUTRAL = {1:700, 2:500, 3:500, 4:500, 5:500, 6:480}

# Example mappings: label -> list of (servo_id, pos, time_ms, wait_after)
# Replace the numbers with your calibrated values.
MAPPINGS = {
    "demo_V": [
        (1, 700, 400, 0.8),   # close clamp
        (2, 600, 700, 0.6),   # position joint 2
        (3, 450, 700, 0.6),   # position joint 3
        (4, 840, 700, 1.0),   # press down
        (4, 700, 700, 0.8),   # lift up
        (2, 520, 700, 0.6),   # return joint 2
        (3, 520, 700, 0.6),   # return joint 3
    ],
    # Add more mappings for other keys as you calibrate
}

def send(ser, sid, pos, t=T_DEFAULT, wait=0.6):
    cmd = f"servo {sid} {pos} {t}\r\n"
    print(" ->", cmd.strip())
    ser.write(cmd.encode())
    time.sleep(wait)

def run_sequence(ser, seq):
    for sid, pos, t, wait in seq:
        send(ser, sid, pos, t, wait)

def reset_to_neutral(ser):
    print("[RESET] Sending neutral positions")
    for sid, pos in NEUTRAL.items():
        send(ser, sid, pos, T_DEFAULT, 0.6)
    time.sleep(0.8)

def main():
    print("[INFO] Auto-detected port:", PORT)
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(0.2)

    # 1) Reset first
    reset_to_neutral(ser)

    print("\nMappings available:")
    pprint(list(MAPPINGS.keys()))
    print("\nInstruction:")
    print(" - Type a mapping label (e.g. demo_V) and press Enter to run that key's sequence.")
    print(" - Type 'list' to show mappings, 'reset' to return to neutral, 'quit' to exit.")

    try:
        while True:
            cmd = input("\nEnter mapping to run > ").strip()
            if not cmd:
                continue
            if cmd == "quit":
                break
            if cmd == "list":
                pprint(list(MAPPINGS.keys()))
                continue
            if cmd == "reset":
                reset_to_neutral(ser)
                continue
            if cmd in MAPPINGS:
                print(f"[EXECUTE] Running mapping '{cmd}' - press Enter to confirm")
                _ = input("Press Enter to execute (or type 'cancel') > ").strip()
                if _ == "cancel":
                    print("Cancelled.")
                    continue
                run_sequence(ser, MAPPINGS[cmd])
                print("[DONE] Sequence complete. Arm returned to neutral.")
            else:
                print("Unknown mapping. Type 'list' to see available mappings.")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        ser.close()
        print("Closed serial. Exiting.")

if __name__ == "__main__":
    main()
