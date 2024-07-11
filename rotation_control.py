from wrappers.OculusWrapper import OculusWrapper
from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import convertControllerAxesToUR5

import sys, os
sys.path.append('/home/weirdlab/mobile_manipulator/modules/math_utils.py')

right_robot_ip = "192.168.1.2"

timeout = 0.25

right_robot = UR5Wrapper(right_robot_ip)

right_robot.reset_to_init()
sleep(2)

right_robot.go_to_position([0,0,0,0,0,0.1])
sleep(5)
right_robot.go_to_position([0,0,0,0,0,0.3])
sleep(5)
right_robot.go_to_position([0,0,0,0,0,0.5])
sleep(5)

# right_robot.go_to_position([0.2,0.3,0.2,0,0,0])
# sleep(2)
# right_robot.go_to_position([-0.2,0.1,-0.2,0,0,0])
# sleep(2)
