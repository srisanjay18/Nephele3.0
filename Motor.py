from gpiozero import DigitalOutputDevice
from time import sleep
import threading

# Motor pin mapping
# Assign GPIOs for direction + pulse (example pins, update to match wiring)
FL_dir = DigitalOutputDevice(5)   # Front Left direction
FL_pul = DigitalOutputDevice(6)   # Front Left pulse
FR_dir = DigitalOutputDevice(13)  # Front Right direction
FR_pul = DigitalOutputDevice(19)  # Front Right pulse
BL_dir = DigitalOutputDevice(20)  # Back Left direction
BL_pul = DigitalOutputDevice(21)  # Back Left pulse
BR_dir = DigitalOutputDevice(26)  # Back Right direction
BR_pul = DigitalOutputDevice(16)  # Back Right pulse

# Global variables
motor_command = 'w'   # default forward
keep_moving = True

# Orientation adjustment:
# Left side = normal, Right side = inverted
def set_motor(dir_pin, motor_side, command):
    if motor_side == "Left":  # normal
        dir_pin.value = 1 if command == "F" else 0
    elif motor_side == "Right":  # inverted
        dir_pin.value = 0 if command == "F" else 1
    elif command == "Stop":
        pass  # no movement

# Assign direction for all wheels
def set_directions(cmd):
    if cmd == "forward":
        set_motor(FL_dir, "Left", "F")
        set_motor(FR_dir, "Right", "F")
        set_motor(BL_dir, "Left", "F")
        set_motor(BR_dir, "Right", "F")
    elif cmd == "backward":
        set_motor(FL_dir, "Left", "B")
        set_motor(FR_dir, "Right", "B")
        set_motor(BL_dir, "Left", "B")
        set_motor(BR_dir, "Right", "B")
    elif cmd == "strafe_left":
        set_motor(FL_dir, "Left", "F")
        set_motor(FR_dir, "Right", "B")
        set_motor(BL_dir, "Left", "B")
        set_motor(BR_dir, "Right", "F")
    elif cmd == "strafe_right":
        set_motor(FL_dir, "Left", "B")
        set_motor(FR_dir, "Right", "F")
        set_motor(BL_dir, "Left", "F")
        set_motor(BR_dir, "Right", "B")
    elif cmd == "rotate_left":
        set_motor(FL_dir, "Left", "B")
        set_motor(FR_dir, "Right", "F")
        set_motor(BL_dir, "Left", "B")
        set_motor(BR_dir, "Right", "F")
    elif cmd == "rotate_right":
        set_motor(FL_dir, "Left", "F")
        set_motor(FR_dir, "Right", "B")
        set_motor(BL_dir, "Left", "F")
        set_motor(BR_dir, "Right", "B")
    elif cmd == "diag_fl":
        set_motor(FL_dir, "Left", "F")
        set_motor(FR_dir, "Right", "Stop")
        set_motor(BL_dir, "Left", "Stop")
        set_motor(BR_dir, "Right", "F")
    elif cmd == "diag_fr":
        set_motor(FL_dir, "Left", "Stop")
        set_motor(FR_dir, "Right", "F")
        set_motor(BL_dir, "Left", "F")
        set_motor(BR_dir, "Right", "Stop")
    elif cmd == "diag_bl":
        set_motor(FL_dir, "Left", "Stop")
        set_motor(FR_dir, "Right", "B")
        set_motor(BL_dir, "Left", "B")
        set_motor(BR_dir, "Right", "Stop")
    elif cmd == "diag_br":
        set_motor(FL_dir, "Left", "B")
        set_motor(FR_dir, "Right", "Stop")
        set_motor(BL_dir, "Left", "Stop")
        set_motor(BR_dir, "Right", "B")

def set_motor_speed(speed_percentage):
    max_delay = 0.0005
    delay = max_delay * (1 - (speed_percentage / 100))
    return delay

def move_motors(speed_percentage):
    global motor_command, keep_moving

    while keep_moving:
        # Map command keys to motions
        if motor_command == 'w':
            set_directions("forward")
        elif motor_command == 's':
            set_directions("backward")
        elif motor_command == 'a':
            set_directions("strafe_left")
        elif motor_command == 'd':
            set_directions("strafe_right")
        elif motor_command == 'q':
            set_directions("rotate_left")
        elif motor_command == 'e':
            set_directions("rotate_right")
        elif motor_command == 'z':
            set_directions("diag_fl")
        elif motor_command == 'x':
            set_directions("diag_fr")
        elif motor_command == 'c':
            set_directions("diag_bl")
        elif motor_command == 'v':
            set_directions("diag_br")

        # Step pulses
        delay = set_motor_speed(speed_percentage)
        for pul in [FL_pul, FR_pul, BL_pul, BR_pul]:
            pul.on()
        sleep(delay)
        for pul in [FL_pul, FR_pul, BL_pul, BR_pul]:
            pul.off()

def control_motors(speed_percentage):
    global motor_command, keep_moving

    motor_thread = threading.Thread(target=move_motors, args=(speed_percentage,))
    motor_thread.start()

    while True:
        command = input("Enter command (w=F, s=B, a=StrafeL, d=StrafeR, q=RotL, e=RotR, z/x/c/v=Diagonals, x=quit): ")
        if command in ['w','s','a','d','q','e','z','x','c','v']:
            motor_command = command
        elif command == 'p':  # quit
            keep_moving = False
            motor_thread.join()
            break
        else:
            print("Invalid command")

def main():
    speed = float(input("Enter speed (0-100): "))
    control_motors(speed)

if name == 'main':
    main()
