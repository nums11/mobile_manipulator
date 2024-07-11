import urx
from wrappers.math_utils import getMovement
from time import sleep

"""
Class that allows you to set a home position and then command new positions for it to go to.
"""

class UR5Wrapper:
    def __init__(self, robot_ip):
        self.robot = urx.Robot(robot_ip)
        self.max_movement = 0.3
        self.move_time = 0.5
        self.init_pose = [1.57, -1.57, -2.66, -0.6, -1.57, 0]
        self.home_position = self.robot.get_pose_array()
        self.robot.set_tcp((0, 0, 0, 0, 0, 0))
        self.robot.set_payload(2, (0, 0, 0.1))
        sleep(0.2)

    def get_pose(self):
        return self.robot.get_pose_array()

    # Sets relative position
    def set_home_position(self):
        self.home_position = self.robot.get_pose_array()

    # Takes in delta position change from home position
    def go_to_position(self, position, wait=False):
        curr_pose = self.robot.get_pose_array()
        desired_pose = getMovement(curr_pose, self.home_position + position, self.max_movement)
        self.robot.servojInvKin(desired_pose, wait=wait, t=self.move_time)

    # Goes to predefined starting position
    def reset_to_init(self):
        self.robot.movej(self.init_pose, acc=1, vel=0.5)
        self.set_home_position()

    def stop(self):
        self.robot.stopj()
