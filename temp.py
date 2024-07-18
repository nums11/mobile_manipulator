from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import printArray,convertControllerAxesToUR5
from wrappers.ModbusWrapper import ModbusWrapper
from wrappers.OculusWrapper import OculusWrapper



right_robot_ip = "192.168.2.2"
right_robot = UR5Wrapper(right_robot_ip)

right_robot.reset_to_init()
robot_pose = right_robot.get_pose()
printArray(robot_pose)

modbus = ModbusWrapper(right_robot_ip)
modbus.updateModbusPosition(robot_pose)


controller = OculusWrapper()

init_pose = [0.11,0.29,0.24,0.00,0.18,3.14,]

print("Ready")

prev_held_trigger = False
while(True):
  reset_robots = controller.get_A()
  if(reset_robots):
    modbus.updateModbusPosition(init_pose)

  right_trigger = controller.get_right_trigger()

  if(right_trigger):
    if(not prev_held_trigger):
      print("New trigger")
      controller.set_right_controller_home()
      right_robot.set_home_position()
    
    delta_movement = controller.get_right_controller_delta()
    delta_movement = convertControllerAxesToUR5(delta_movement)

    movement = right_robot.makeRobotRelativePose(delta_movement)
    printArray(movement)

    # print("New movement")
    right_robot.updateModbusPosition(movement)

    # modbus.updateModbusPosition(movement)
    sleep(0.01)

  prev_held_trigger = right_trigger

  