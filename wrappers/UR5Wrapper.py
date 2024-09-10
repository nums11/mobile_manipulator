import urx
from wrappers.math_utils import getMovement
from time import sleep
import pymodbus.client as ModbusClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.framer import Framer
import numpy as np

"""
Class that allows you to set a home position and then command new positions for it to go to.
"""

class UR5Wrapper:
    def __init__(self, robot_ip):
        self.robot = urx.Robot(robot_ip, use_rt=True)
        self.max_movement = 0.2
        self.move_time = 0.5
        self.init_pose = [1.57, -1.57, -2.66, -2.02, -1.57, 0.2]
        self.init_pose_modbus = [0.11,0.27,0.07,-0.21,-2.08,-2.15]
        self.home_position = self.robot.get_pose_array()
        self.robot.set_tcp((0, 0, 0, 0, 0, 0))
        self.robot.set_payload(2.3, (0, 0, 0.15))
        sleep(0.2)

        self.client = ModbusClient.ModbusTcpClient(
        robot_ip,
        port=502,
        framer=Framer.SOCKET
        )
        self.client.connect()
        self.updateModbusPosition(self.init_pose_modbus)

    def get_pose(self):
        return self.robot.get_pose_array(True)

    # Sets relative position
    def set_home_position(self):
        self.home_position = self.robot.get_pose_array()

    def makeRobotRelativePose(self, position):
        curr_pose = self.robot.get_pose_array()
        desired_pose = getMovement(curr_pose, self.home_position + position, self.max_movement)
        return desired_pose

    # Takes in delta position change from home position
    def go_to_position(self, position):
        curr_pose = self.robot.get_pose_array()
        print("Desired position arm space \t", self.home_position + position)
        desired_pose = getMovement(curr_pose, self.home_position + position, self.max_movement)
        self.updateModbusPosition(desired_pose)

    # Goes to predefined starting position
    def reset_to_init(self):
        self.robot.movej(self.init_pose, acc=1, vel=0.5)
        self.set_home_position()
        self.updateModbusPosition(self.init_pose_modbus)

    def stop(self):
        self.robot.stopj()

    # Give position as a list of 6 floats, this will multiply by 100 and then write it
    def updateModbusPosition(self, position):
        position = np.array(position) * 100
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)
        for i in range(6): # don't update the ypr for now
            builder.reset()
            builder.add_16bit_int(int(position[i]))
            payload = builder.to_registers()
            self.client.write_register(128 + i, payload[0])
        
    # Returns currently the end effector position    
    def getState(self):
        return np.array(self.get_pose())        
