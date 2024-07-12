from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import printArray

right_robot_ip = "192.168.1.2"
right_robot = UR5Wrapper(right_robot_ip)

# right_robot.reset_to_init()

# sleep(0.5)
# print("Resetted")
# printArray(right_robot.get_pose())

right_robot.modbusMode()

print("Moved")
printArray(right_robot.get_pose())

# right_robot.set_freedrive()
# while True:
#     printArray(right_robot.get_pose())
#     sleep(1)