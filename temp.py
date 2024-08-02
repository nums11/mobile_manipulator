from wrappers.OculusWrapper import OculusWrapper
from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import convertControllerAxesToUR5, printArray

# URX -------------------------

left_robot_ip = "192.168.1.2"


timeout = 0.01

left_robot = UR5Wrapper(left_robot_ip)
left_robot.reset_to_init()

controller = OculusWrapper()

prev_held_trigger = False

print("Ready")

while(True):
  reset_robots = controller.get_A()
  if(reset_robots):
    left_robot.reset_to_init()

  right_trigger = controller.get_right_trigger()

  if(right_trigger):
    if(not prev_held_trigger):
      print("New trigger")
      controller.set_right_controller_home()
      left_robot.set_home_position()
    
    delta_movement = controller.get_right_controller_delta()
    delta_movement = convertControllerAxesToUR5(delta_movement)

    left_robot.go_to_position(delta_movement, wait=False)
    sleep(timeout)

  prev_held_trigger = right_trigger
