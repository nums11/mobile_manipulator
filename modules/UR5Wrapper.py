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
        self.home_pose = self.robot.get_cur_pose_with_rot()


    def set_home_position(self):
        self.home_position = self.robot.get_cur_pose_with_rot()

    # this will be in delta relative to home position
    def go_to_position(self, position, wait=False):
        curr_pose = self.robot.get_cur_pose_with_rot()
        desried_pose = getMovement(curr_pose, position, self.max_movement)
        self.robot.servojInvKin(desried_pose, wait=wait, t=self.move_time)

    def reset_to_init(self):
        self.robot.movej(self.home_position)

    def stop(self):
        self.robot.stopj()

