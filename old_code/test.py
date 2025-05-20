import event, time, cyberpi, mbot2, mbuild, random

# initialize variables
base_power = 35
current_speed = base_power 
kp = 0.3
left_power = 0
right_power = 0
red_count = 0

@event.start
def on_start():
    global current_speed, base_power, kp, left_power, right_power, red_count
    cyberpi.console.set_font(12)
    cyberpi.console.println("A：Stop Navigating")
    cyberpi.console.println("B：Start Navigating")
    cyberpi.console.println("Press joystick：")
    cyberpi.console.println("Check the color recognition results")

# @event.is_press('a')
# def is_a_press():
#     global base_power, kp, left_power, right_power
#     cyberpi.stop_other()
#     mbot2.drive_power(0, 0)

@event.is_press('b')
def is_b_press():
    global current_speed, base_power, kp, left_power, right_power, red_count
    cyberpi.stop_other()
    base_power = 35
    kp = 0.3

    while not cyberpi.controller.is_press('a'):
        # Obstacle detection
        if mbuild.ultrasonic2.get(1) < 10:
            mbot2.EM_stop("all") 
            cyberpi.console.println("Obstacle detected!")
            continue

        # Color detection - RED
        if mbuild.quad_rgb_sensor.is_color("red", "L1") or mbuild.quad_rgb_sensor.is_color("red", "R1"):
            mbot2.EM_stop("all")
            mbot2.backward(50, 0.5)
            cyberpi.led.show("red red red red red")
            cyberpi.console.println("Red detected - stopping")
            cyberpi.console.println("Waiting for green...")
            
            while True:
                if mbuild.quad_rgb_sensor.is_color("green", "L1") or mbuild.quad_rgb_sensor.is_color("green", "R1"):
                    cyberpi.console.println("Green detected - moving forward")
                    cyberpi.led.show("green green green green green")
                    mbot2.forward(50, 1.0)
                    break  # Exit loop and resume navigation
                time.sleep(0.1)  # Slight delay to prevent CPU overload

        # Color detection - YELLOW
        if mbuild.quad_rgb_sensor.is_color("yellow", "L1") or mbuild.quad_rgb_sensor.is_color("yellow", "R1"):
            mbot2.forward(30, 1.0)
            cyberpi.led.show("yellow yellow yellow yellow yellow")
            cyberpi.console.println("Yellow detected - slowing down")

            start_time = time.time()  # Record the current time
            base_power = 25

            # Line tracking logic with decrease speed
            while time.time() - start_time < 5:  # Run for 5 seconds
                    offset = mbuild.quad_rgb_sensor.get_offset_track(1)
                    left_power = (base_power - kp * offset)
                    right_power = -1 * (base_power + kp * offset)
                    mbot2.drive_power(left_power, right_power)
                    time.sleep(0.05)  # Small delay to avoid overloading the CPU

            base_power = 35  # Return to normal speed

        # Color detection - WHITE
        if mbuild.quad_rgb_sensor.is_color("white", "L1") or mbuild.quad_rgb_sensor.is_color("white", "R1"):
            cyberpi.led.show("white white white white white")
            # Line tracking logic with normal speed
            base_power = 35
            offset = mbuild.quad_rgb_sensor.get_offset_track(1)
            left_power = (base_power - kp * offset)
            right_power = -1 * (base_power + kp * offset)
            mbot2.drive_power(left_power, right_power)

        time.sleep(0.05)

    mbot2.EM_stop("all") 
    cyberpi.console.println("Navigation stopped")

@event.is_press('middle')
def is_joy_press():
    cyberpi.stop_other()
    mbot2.drive_power(0, 0)

    while not cyberpi.controller.is_press('a'):
        # Show colors from sensors for debugging
        colors = [
            "L1: " + str(mbuild.quad_rgb_sensor.get_color_sta("L1", 1)), 
            "R1: " + str(mbuild.quad_rgb_sensor.get_color_sta("R1", 1))
        ]

        cyberpi.console.clear()
        for color in colors:
            cyberpi.console.println(color)

