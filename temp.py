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
comms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
comms.connect((right_robot_ip, 30003))

client = ModbusClient.ModbusTcpClient(right_robot_ip,port=502,framer=Framer.SOCKET)
r = client.write_register(128, 0)

script_file = open("modbus.script",'rb')
script = script_file.read()
print(script)
comms.sendall(script)

print("Modbus running")
sleep(3)

val = 6
print("New val:" + str(val))
r = client.write_register(128, int(val))

