from wrappers import Gripper, OculusWrapper
from time import sleep

gripper = Gripper('COM6')
oculus = OculusWrapper()

while True:
  # Get oculus trigger
  # Move hand that much * 255
  gripper.move(int(oculus.get_trigger() * 255))
  
  sleep(0.01)
