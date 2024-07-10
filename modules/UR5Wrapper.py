import urx
from math_utils import getMovement

"""
Class that allows you to set a home position and then command new positions for it to go to.
"""

class UR5Wrapper:
    def __init__(self, robot_ip):
        self.robot = urx.Robot(robot_ip)
        self.max_movement = 0.3
        self.move_time = 0.4
        self.init_pose = [1.57, -1.57, -2.66, -0.6, -1.57, 0]
        self.home_position = self.robot.get_cur_pose_with_rot()

    # Sets relative position
    def set_home_position(self):
        self.home_position = self.robot.get_cur_pose_with_rot()

    # Takes in delta position change from home position
    def go_to_position(self, position, wait=False):
        curr_pose = self.robot.get_cur_pose_with_rot()
        desired_pose = getMovement(curr_pose, self.home_position + position, self.max_movement)
        self.robot.servojInvKin(desired_pose, wait=wait, t=self.move_time)

    # Goes to predefined starting position
    def reset_to_init(self):
        self.robot.movej(self.init_pose)

    def stop(self):
        self.robot.stopj()

