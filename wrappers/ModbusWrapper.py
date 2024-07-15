import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config
)
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
    for i in range(6):
      self.client.write_register(128 + i, int(position[i]))
  
  def close(self):
    self.client.close()
