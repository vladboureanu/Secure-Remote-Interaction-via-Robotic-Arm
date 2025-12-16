# type_demo.py
# Run: python3 type_demo.py
# It resets to neutral, types SEQUENCE, and exits. No prompts.

import serial, time

SERIAL_PORT = "/dev/ttyUSB0"
BAUD = 115200

# Your upright neutral posture
NEUTRAL = {1:680, 2:500, 3:400, 4:700, 5:500, 6:480}

# Global timings (ms)
MOVE_TIME  = 550
PRESS_TIME = 1050
PAUSE      = 0.25   # extra settle time after each move

# Change this to what you want to be typed (must be mapped below)
SEQUENCE = "boureanuvqbeavisctchaibeavis9p"    # e.g. "j8e", "je8", etc.

def send(ser, sid, pos, t):
    ser.write(f"servo {sid} {pos} {t}\r".encode())
    time.sleep(t/1000 + PAUSE)

def reset_to_neutral(ser):
    for sid, pos in NEUTRAL.items():
        send(ser, sid, pos, MOVE_TIME)

# KEYMAP: each step is (servo_id, position, time_ms)
# Pattern: position with 2/3/5/6 → press with 4 → lift 4 → (optionally) return 2/3/5/6
KEYMAP = {
    "j": [
        (6, 450, MOVE_TIME),
        (3, 350, MOVE_TIME),
        (4, 700, MOVE_TIME),   # hover height before press
        (4, 950, PRESS_TIME),  # press down
        (4, 700, MOVE_TIME),   # lift up
    ],

    "e": [
        (6, 540, MOVE_TIME),
        (5, 445, MOVE_TIME),
        (3, 360, MOVE_TIME),
        (4, 920, 950),         # press down
        (4, 700, MOVE_TIME),   # lift up
    ],

    "8": [
        (6, 450, MOVE_TIME),
        (5, 435, MOVE_TIME),
        (3, 450, MOVE_TIME),
        (4, 940, 900),         # press down
        (4, 700, MOVE_TIME),   # lift up
    ],

    "0": [
	(6, 415, MOVE_TIME),
	(5, 420, MOVE_TIME),
	(3, 460, MOVE_TIME),
	(4, 950, 1000),
	(4, 700, MOVE_TIME),
    ],

    "c": [
	(6, 600, MOVE_TIME),
	(5, 455, MOVE_TIME),
	(3, 410, MOVE_TIME),
	(4, 950, PRESS_TIME),
	(4, 700, MOVE_TIME),
    ],

    "u": [
	(6, 460, MOVE_TIME),
	(5, 470, MOVE_TIME),
	(3, 410, MOVE_TIME),
	(4, 960, 900),
	(4, 700, MOVE_TIME),
    ],

    "f": [
	(6, 520, MOVE_TIME),
	(5, 480, MOVE_TIME),
	(3, 330, MOVE_TIME),
	(4, 935, 930),
	(4, 700, MOVE_TIME),
    ],

    "v": [
	(6, 505, MOVE_TIME),
	(5, 500, MOVE_TIME),
	(3, 285, MOVE_TIME),
	(4, 935, 950),
	(4, 700, MOVE_TIME),
    ],

    "p": [
	(6, 350, MOVE_TIME),
	(5, 400, MOVE_TIME),
	(3, 380, MOVE_TIME),
	(4, 870, 950),
	(4, 700, MOVE_TIME),
    ],

    "b": [
	(6, 480, MOVE_TIME),
	(5, 500, MOVE_TIME),
	(3, 285, MOVE_TIME),
	(4, 935, 1000),
	(4, 700, MOVE_TIME),
    ],

    "o": [
	(6, 420, MOVE_TIME),
	(5, 460, MOVE_TIME),
	(3, 420, MOVE_TIME),
	(4, 960, 1000),
	(4, 700, MOVE_TIME),
    ],

    "r": [
        (6, 520, MOVE_TIME),
        (5, 445, MOVE_TIME),
        (3, 360, MOVE_TIME),
        (4, 920, 950),         # press down
        (4, 700, MOVE_TIME),
    ],

    "a": [
	(6, 580, MOVE_TIME),
 	(5, 450, MOVE_TIME),
 	(3, 330, MOVE_TIME),
 	(4, 900, PRESS_TIME),
 	(4, 700, MOVE_TIME),
    ],

    "n": [
        (6, 455, MOVE_TIME),
	(5, 520, MOVE_TIME),
        (3, 300, MOVE_TIME),
        (4, 700, MOVE_TIME),   # hover height before press
        (4, 950, PRESS_TIME),  # press down
        (4, 700, MOVE_TIME),   # lift up
    ],

    "q": [
	(6, 600, MOVE_TIME),
	(5, 420, MOVE_TIME),
	(3, 440, MOVE_TIME),
	(4, 945, 1000),
	(4, 700, MOVE_TIME),
    ],

    "i": [
	(6, 440, MOVE_TIME),
	(5, 460, MOVE_TIME),
	(3, 410, MOVE_TIME),
	(4, 970, 900),
	(4, 700, MOVE_TIME),
    ],

    "s": [
	(6, 560, MOVE_TIME),
	(5, 450, MOVE_TIME),
	(3, 300, MOVE_TIME),
	(4, 900, PRESS_TIME),
	(4, 700, MOVE_TIME),
    ],

    "t": [
	(6, 495, MOVE_TIME),
	(5, 455, MOVE_TIME),
	(3, 360, MOVE_TIME),
	(4, 935, PRESS_TIME),
	(4, 700, MOVE_TIME),
    ],

    "h": [
	(6, 473, MOVE_TIME),
	(5, 475, MOVE_TIME),
	(3, 300, MOVE_TIME),
	(4, 920, 950),
	(4, 700, MOVE_TIME),
     ],

    "9": [
	(6, 437, MOVE_TIME),
	(5, 430, MOVE_TIME),
	(3, 455, MOVE_TIME),
	(4, 945, 950),
	(4, 700, MOVE_TIME),
     ],
}

def main():
    ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
    time.sleep(0.2)

    reset_to_neutral(ser)

    for ch in SEQUENCE.lower():
        if ch in KEYMAP:
            for sid, pos, t in KEYMAP[ch]:
                send(ser, sid, pos, t)
        else:
            # unmapped char -> small pause (acts like a space)
            time.sleep(0.6)

    reset_to_neutral(ser)
    ser.close()

if __name__ == "__main__":
    main()

