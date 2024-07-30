from wrappers.GripperWrapper import GripperWrapper
from wrappers.OculusWrapper import OculusWrapper
from time import sleep
from wrappers.UR5Wrapper import UR5Wrapper
from wrappers.math_utils import convertControllerAxesToUR5


right_robot_ip = "192.168.2.2"

gripper = GripperWrapper('/dev/ttyUSB0')
oc = OculusWrapper()

gripper.activate()

while True:
  gripper.update()
  if not gripper.isReady():
    continue
  held, val = oc.get_right_gripper()
  print(held, " ", val)
  # Get oculus trigger
  # Move hand that much * 255
  gripper.move(int(val * 255))
  
  sleep(0.01)
