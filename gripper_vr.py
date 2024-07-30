from wrappers.GripperWrapper import GripperWrapper
from wrappers.OculusWrapper import OculusWrapper
from time import sleep

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
