from wrappers.OculusWrapper import OculusWrapper
from wrappers.UR5Wrapper import UR5Wrapper
from wrappers.GripperWrapper import GripperWrapper
from time import sleep
from wrappers.math_utils import convertControllerAxesToUR5, printArray

# URX -------------------------

left_robot_ip = "192.168.2.2"


timeout = 0.01

arm = UR5Wrapper(left_robot_ip)
arm.reset_to_init()

gripper = GripperWrapper('/dev/ttyUSB0')

controller = OculusWrapper()

prev_held_trigger = False

# gripper.activate()

while True:
  gripper.update()
  if gripper.isReady():
    break

print("Ready")

while(True):
  reset_robots = controller.get_A()
  if(reset_robots):
    arm.reset_to_init()

  right_trigger = controller.get_right_trigger()

  if(right_trigger):
    if(not prev_held_trigger):
      print("New trigger")
      controller.set_right_controller_home()
      arm.set_home_position()
    
    delta_movement = controller.get_right_controller_delta()
    delta_movement = convertControllerAxesToUR5(delta_movement)

    arm.go_to_position(delta_movement)

  gripperHeld, gripperPos = controller.get_right_gripper()
  gripper.move(int(gripperPos * 255), 255, 255)
  
  if(gripperHeld or right_trigger):
    sleep(timeout)

  prev_held_trigger = right_trigger
