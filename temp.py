from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import printArray
from wrappers.ModbusWrapper import ModbusWrapper


right_robot_ip = "192.168.1.2"
right_robot = UR5Wrapper(right_robot_ip)

right_robot.reset_to_init()
robot_pose = right_robot.get_pose()
printArray(robot_pose)

modbus = ModbusWrapper(right_robot_ip)
modbus.updateModbusPosition(robot_pose)

