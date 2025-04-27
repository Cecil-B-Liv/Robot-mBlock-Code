import event, time, cyberpi, mbot2, mbuild
import time
# initialize variables
base_power = 0
kp = 0
left_power = 0
right_power = 0

@event.is_press('a')
def is_btn_press():
    global base_power, kp, left_power, right_power
    cyberpi.stop_other()
    mbot2.drive_power(0, 0)

@event.is_press('b')
def is_btn_press1():
    global base_power, kp, left_power, right_power
    cyberpi.stop_other()
    base_power = 35
    kp = 0.8
    while True:
      left_power = (base_power - kp * mbuild.quad_rgb_sensor.get_offset_track(1))
      # As a "deviation quantity", line offset position can be used for deviation correction of automatic line-following tasks. It is the "P" in what we call PID control.
      #
      # I and D involve integral and differential knowledge, and have high requirements for mathematics, programming and hardware efficiency, which will not be expanded here.
      right_power = -1 * ((base_power + kp * mbuild.quad_rgb_sensor.get_offset_track(1)))
      mbot2.drive_power(left_power, right_power)

@event.is_press('middle')
def is_joy_press():
    global base_power, kp, left_power, right_power
    cyberpi.stop_other()
    while True:
      cyberpi.console.println(mbuild.quad_rgb_sensor.get_color_sta("R2",1))
      time.sleep(0.1)

