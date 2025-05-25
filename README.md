# COSC3070 – Programming Autonomous Robots  
### Final Project – Autonomous Path Following and Obstacle Avoidance with mBot2 Neo

## Overview
This repository contains the Python source code for the COSC3070 final project titled **"Autonomous Path Following and Obstacle Avoidance with mBot2 Neo"**. The robot is programmed to follow a colored path (yellow or white), recognize traffic light-style color signs, and avoid obstacles using onboard sensors.

## Project Features
- **Line Following** using proportional control based on RGB sensor offset.
- **Color Sign Detection** for stop (red), go (green), slow (yellow), and track (white).
- **Obstacle Avoidance** using ultrasonic sensing and reactive decision logic.
- **Interactive Modes** controlled via onboard buttons:
  - **Triangle**: Stop Mode
  - **Square**: Run Mode
  - **Joystick**: Color Detection Debug Mode
- LED feedback and 🎵 sound tones for enhanced user interaction.

## Files
- `main.py` – The full code that is copied into the **mBlock** CyberPi editor and uploaded directly to the robot.

## Upload Instructions
1. Open the **mBlock 5** application.
2. Switch to **Python Mode**.
3. Select your device: **CyberPi + mBot2**.
4. Connect the robot via **USB cable** or **Bluetooth dongle**.
5. Open `main.py`, paste it into the editor.
6. Click **Upload** to flash the program to the mBot2.

> You must be in **Upload Mode**, not Live Mode, for autonomous behavior to function.

## Dependencies
No external Python libraries are required. The code relies on built-in **CyberPi** and **mBuild** modules available inside mBlock’s Python environment.

```python
import cyberpi
import mbot2
import mbuild
import event
import time
import random
