from robotiq_modbus_controller.driver import RobotiqModbusRtuDriver
import numpy as np

"""
Class meant to interface with the Robotiq 3F gripper via USB.
Currently only supports the RTU driver and works on overall hand control, not per finger
"""
class GripperWrapper:
  def __init__(self, port: str):
    self.gripper = RobotiqModbusRtuDriver(port)
    self.status = self.gripper.status()
    if(not self.isActivated()):
      self.activate()
  
  """
  Needs to be called preiodically, upper limit is 100hz
  """
  def update(self):
    self.status = self.gripper.status()
    
  def activate(self):
    self.gripper.reset()
    self.gripper.activate()
  
  def isActivated(self):
    return self.status.gripper_status.act

  def isReady(self):
    return self.status.gripper_status.sta == 3
  
  def move(self, pos: int, speed: int = 255, force: int = 0):
    self.gripper.move(pos=pos, speed=speed, force=force)
    
  # Currently only returns the position of the whole gripper
  def getState(self):
    return np.array(self.status.position)
    
if __name__ == "__main__":
  gripper = GripperWrapper('COM6')
  
  gripper.update()
  while not gripper.isReady():
    pass
  
  print("Gripper is ready")
  gripper.move(0)
  from time import sleep
  sleep(2)
  gripper.move(255)
