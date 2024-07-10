from modules.OculusWrapper import OculusWrapper
from modules.UR5Wrapper import UR5Wrapper
from time import sleep

right_robot_ip = "192.168.1.2"

timeout = 0.25

right_robot = UR5Wrapper(right_robot_ip)
controller = OculusWrapper()

right_robot.reset_to_init()

prev_held_trigger = False

while(True):
  right_trigger = controller.get_right_trigger()

  if(right_trigger):
    if(not prev_held_trigger):
      print("New trigger")
      controller.set_right_controller_home()
      right_robot.set_home_position()
    
    delta_movement = controller.get_right_controller_delta()
    delta_movement[2] *= -1
    delta_movement[1], delta_movement[2] = delta_movement[2], delta_movement[1] # y is z
    print("Delta is: " + str(delta_movement))

    right_robot.go_to_position(delta_movement, wait=False)
    sleep(timeout)
  else:
    right_robot.stop()
    
  prev_held_trigger = right_trigger

