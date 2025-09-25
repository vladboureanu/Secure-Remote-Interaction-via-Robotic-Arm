Secure Remote Interaction via Robotic Arm

This project explores remote humna-computer interaction using a Hiwonder xArm robotic arm controlled via Raspberry Pi 4.
The objective is to demonstrate how physical keystrokes (e.g., typing, Ctrl+Alt+Del) can be pressedd securely from a remote system, without direct human presence.


1. Project Overview
- A Raspberry 4 model B communicates with the robotic arm’s ESP32 controller over USB.
- Python 3 scripts are used to send servo commands and automate keystrokes.
- Additional hardware such as an SG90 micro servo with PCA9685 PWM driver can extend functionality (e.g., dedicated stylus for pressing keys like `Delete`).
- Remote access is secured via SSH (secure shell) and command execution is executed using MQTT messaging


2. Hardware Used
- Raspberry Pi 4 Model B
- Hiwonder xArm (ESP32-based bus servo controller)
- External power supply for servos
- SG90 micro servo + PCA9685 module (for stylus actuator)
- USB-C / USB-A cables for connectivity


3. Software Environment
- Raspberry Pi OS as host OS
- Python 3 as primary development language
- Libraries:
  - `pyserial` → communication with ESP32 controller
  - `paho-mqtt` → remote command publishing/subscribing
  - `adafruit-pca9685` → optional control of SG90 servo
- Mosquitto MQTT Broker installed locally for message passing
- SH for remote system access

No unauthorised software was installed on the Council laptop — only the Raspberry Pi was configured for development and control.


4. Key Features
- Remote keystroke typing via robotic arm
- Secure reset functionality (`Ctrl+Alt+Del`)
- MQTT integration for flexible remote control
- Modular design: easy to extend with extra servos or attachments


5. Repository Structure
- `press_demo.py` → One full press cycle (open clamp, move down, press, release).
- `clamp_open.py` → Opens the clamp.
- `clamp_close.py` → Closes the clamp.
- `ctrl_alt_test.py` → Demonstrates repeated clamp motion (basis for typing Ctrl/Alt keys).

  
6. Future Work
- Calibration of all keys for full keyboard typing.
- Better stylus attachment for pressing diagonal keys.
- Integration with remote desktop workflows.
- Recording & replaying typed sequences.


7. Author
**Vlad Boureanu**
Final Year Project – Secure Remote Interaction via Robotic Arm
