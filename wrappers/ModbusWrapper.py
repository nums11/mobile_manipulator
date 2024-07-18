import pymodbus.client as ModbusClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.framer import Framer
import numpy as np

class ModbusWrapper:
  def __init__(self, robot_ip):
    self.client = ModbusClient.ModbusTcpClient(
      robot_ip,
      port=502,
      framer=Framer.SOCKET
    )
    self.client.connect()
  
  # Give position as a list of 6 floats, this will multiply by 100 and then write it
  def updateModbusPosition(self, position):
    position = np.array(position) * 100
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)

    for i in range(6): # don't update the ypr for now
      builder.reset()
      builder.add_16bit_int(int(position[i]))
      payload = builder.to_registers()
      print(payload)
      self.client.write_register(128 + i, payload[0])
  
  def close(self):
    self.client.close()
