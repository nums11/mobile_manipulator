from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import printArray
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config
)
from pymodbus.framer import Framer
import socket


right_robot_ip = "192.168.1.2"
# right_robot = UR5Wrapper(right_robot_ip)
comms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
comms.connect((right_robot_ip, 30003))

# right_robot.reset_to_init()

client = ModbusClient.ModbusTcpClient(right_robot_ip,port=502,framer=Framer.SOCKET)
r = client.write_register(128, 0)

script_file = open("modbus.script",'rb')
script = script_file.read()
print(script)
comms.sendall(script)

# right_robot.sendProgram(script)

print("Modbus running")
sleep(3)


# pose = right_robot.get_pose()
# printArray(pose)
val = 6
print("New val:" + str(val))
r = client.write_register(128, int(val))


sleep(2)
# client.close()


# pose = right_robot.get_pose()
# printArray(pose)

