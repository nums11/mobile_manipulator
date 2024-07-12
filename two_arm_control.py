from wrappers.OculusWrapper import OculusWrapper
from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import convertControllerAxesToUR5

# URX -------------------------

right_robot_ip = "192.168.2.2"
left_robot_ip = "192.168.1.2"


timeout = 0.25

right_robot = UR5Wrapper(right_robot_ip)
left_robot = UR5Wrapper(left_robot_ip)
controller = OculusWrapper()

right_robot.reset_to_init()
left_robot.reset_to_init()

prev_held_right_trigger = False
prev_held_left_trigger = False

while(True):
    all = controller.getEverything()
    reset_robots = controller.get_X() or controller.get_A()
    if(reset_robots):
        right_robot.reset_to_init()
        left_robot.reset_to_init()
    
    right_trigger = controller.get_right_trigger()
    if(right_trigger):
        if(not prev_held_right_trigger):
            print("New right trigger")
            controller.set_right_controller_home()
            right_robot.set_home_position()

        delta_movement = controller.get_right_controller_delta()
        delta_movement = convertControllerAxesToUR5(delta_movement)

        right_robot.go_to_position(delta_movement, wait=False)
    else:
        right_robot.stop()
    prev_held_right_trigger = right_trigger

    left_trigger = controller.get_left_trigger()
    if(left_trigger):
        if(not prev_held_left_trigger):
            print("New left trigger")
            controller.set_left_controller_home()
            left_robot.set_home_position()

        delta_movement = controller.get_left_controller_delta()
        delta_movement = convertControllerAxesToUR5(delta_movement)

        left_robot.go_to_position(delta_movement, wait=False)
    else:
        left_robot.stop()
    prev_held_left_trigger = left_trigger

    if(left_trigger or right_trigger):
        sleep(timeout)