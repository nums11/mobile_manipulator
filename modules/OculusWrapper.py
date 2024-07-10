
OCCULUS = '/home/weirdlab/Documents/oculus_reader'
import sys
import time

import numpy as np
sys.path.append(OCCULUS)
from oculus_reader.reader import OculusReader


class OculusController():
    def __init__(self):
        self.oculus = OculusReader()
        time.sleep(1)
        self.cur_pos = self.get_cur_pos()

    def get_controller_position(self, controller):
        transform = self.oculus.get_transformations_and_buttons()[0][controller]
        return transform[:, 3]

    def get_right_controller_position(self):
        return self.get_controller_position('r')
    
    def get_left_controller_position(self):
        return self.get_controller_position('l')
    
    def get_controller_ypr(self, controller):
        transform = self.oculus.get_transformations_and_buttons()[0][controller]
        yaw = transform[0][0]
        roll = transform[1][0]
        pitch = transform[1][1]
        return yaw, pitch, roll
    
    def get_right_controller_ypr(self):
        return self.get_controller_ypr('r')

    def get_left_controller_ypr(self):
        return self.get_controller_ypr('l')
    
    def get_controller_pose_with_rot(self, controller):
        pose = self.get_controller_position(controller)[:3]
        y,p,r = self.get_controller_ypr(controller)
        output = [0,0,0,0,0,0]
        output[:3] = pose
        output[3] = y
        output[4] = p
        output[5] = r
        return output
    
    def get_right_controller_pose_with_rot(self):
        return self.get_controller_pose_with_rot('r')
    
    def get_left_controller_pose_with_rot(self):
        return self.get_controller_pose_with_rot('l')

    def getEverything(self):
        return self.oculus.get_transformations_and_buttons()
    
    def get_right_trigger(self):
        return self.oculus.get_transformations_and_buttons()[1]['RTr']
    
    def get_left_trigger(self):
        return self.oculus.get_transformations_and_buttons()[1]['LTr']


    def get_buttons(self):
        """
        Returns the buttons.
        The ones on the right are "A, B, RTr"
        """
        return self.oculus.get_transformations_and_buttons()[1]

def main():
    reader = OculusController()
    print(reader.get_buttons())
    while True:
        print()
        poses, buttons = reader.getEverything()
        print(poses)
        yaw, pitch, roll = reader.get_ypr()
        print(f'Yaw = {yaw}, Pitch = {pitch}, Roll = {roll}')
        print(reader.get_cur_pose_with_rot())
        time.sleep(1)

if __name__ == '__main__':
     main()
