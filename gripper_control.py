import pymodbus.client as ModbusClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.framer import Framer
import numpy as np
import serial

# It shows up under COM8 port
client = ModbusClient.ModbusSerialClient(baudrate=115200, port='COM8')
print("Made client")
client.connect()
print("Connected")
request = 0b00000001
response = client.write_register(0, request)
print("Wrote request")
print(response)
