NEPHELE 3.0

This repository contains the code and modules for Nephele 3.0, a student-built humanoid robot of 4-wheel drive with omnidirectional movement, articulated arms, and a control system.

Current included module:
- `Mecanum.py`: Controls the mecanum wheel movement.

Future modules:
- Head control
- Arm control
- Complete robot control system

Components:
1. Four NEMA 23 Motors       
2. Four 4" Mecanum Wheels with shaft coupler
3. Four TB6600 Motor Drivers
4. 25.2v 15ah Li-ion Battery Pack with in-built BMS connected using XT60 Connector
5. Raspberry pi 4 with 5V power source using battery or power bank
6. HDMI Display or Remote Connection to Windows Device using ssh or RealVNC
7. Switch and Wires

Steps:
1. Identify the pair coils of the motors and connect them to A+, A-, B+, B- of the motor driver.
2. Connect the VCC and GND of all the motor drivers to the battery connector in parallel. Use thick wires to connect the pins to the battery connector.
3. Using Jumper Wires, connect the pins PUL+, and DIR+ of each motor to the appropriate GPIO pins of the pi for the pulse and direction, according to their position in the base.
4. The following are the positions of the wheels:
   1. FL - Front Left
   2. FR - Front Right
   3. BL - Back Left
   5. BR - Back Right
5. Connect the PUL- and DIR- pins in series and take one connection from either pin and connect to a GND pin in the pi. Repeat this for each motor driver.
6. Fit the mecanum wheels to the motors such that the rollers of the diagonally placed wheels are aligned to each other.
7. Execute the given Mecanum.py codefile using terminal using "python3 Mecanum.py" or execute it directly in the editor.
8. Enter the desired speed. Start off slow to know how it works.
9. Use the controls given to move the robot in the desired direction.
