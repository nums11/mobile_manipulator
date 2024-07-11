from wrappers.OculusWrapper import OculusWrapper
from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import convertControllerAxesToUR5

right_robot_ip = "192.168.1.2"
left_robot_ip = "192.168.2.2"


timeout = 0.25

right_robot = UR5Wrapper(right_robot_ip)
left_robot = UR5Wrapper(left_robot_ip)
controller = OculusWrapper()

right_robot.reset_to_init()
left_robot.reset_to_init()

prev_held_trigger = False

while(True):
  right_trigger = controller.get_right_trigger()

  print(controller.getEverything())

  if(right_trigger):
    if(not prev_held_trigger):
      print("New trigger")
      controller.set_right_controller_home()
      right_robot.set_home_position()
      left_robot.set_home_position()
    
    delta_movement = controller.get_right_controller_delta()
    delta_movement = convertControllerAxesToUR5(delta_movement)

    right_robot.go_to_position(delta_movement, wait=False)
    left_robot.go_to_position(delta_movement, wait=False)
    sleep(timeout)
  else:
    right_robot.stop()
    
  prev_held_trigger = right_trigger

