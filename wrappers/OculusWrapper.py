
OCCULUS = '/home/weirdlab/Documents/oculus_reader'
import sys
import time

import numpy as np
sys.path.append(OCCULUS)
from oculus_reader.reader import OculusReader
from scipy.spatial.transform._rotation import Rotation 


class OculusWrapper():
    def __init__(self):
        self.oculus = OculusReader()
        time.sleep(1)
        self.right_controller_home = self.get_right_controller_pose_with_rot()
        # self.left_controller_home = self.get_left_controller_pose_with_rot()

    # Returns global position
    def get_controller_position(self, controller):
        transform = self.oculus.get_transformations_and_buttons()[0][controller]
        return transform[:, 3]

    def get_right_controller_position(self):
        return self.get_controller_position('r')
    
    def get_left_controller_position(self):
        return self.get_controller_position('l')
    
    # returns global yaw, pitch, roll
    def get_controller_ypr(self, controller):
        transform = self.oculus.get_transformations_and_buttons()[0][controller]
        rot_matrix = transform[:3,:3] # 3x3 rotation matrix
        rot_matrix_vals = Rotation.from_matrix(rot_matrix)
        pry = rot_matrix_vals.as_euler('XYZ')
        pitch = pry[0]
        roll = pry[1]
        yaw = pry[2]
        return yaw, pitch, roll
    
    def get_right_controller_ypr(self):
        return self.get_controller_ypr('r')

    def get_left_controller_ypr(self):
        return self.get_controller_ypr('l')
    
    # Returns global position and yaw, pitch, roll
    def get_controller_pose_with_rot(self, controller):
        pose = self.get_controller_position(controller)[:3]
        y,p,r = self.get_controller_ypr(controller)
        output = [0,0,0,0,0,0]
        output[:3] = pose
        output[3] = r
        output[4] = p
        output[5] = y
        output = np.array(output)
        return output
    
    def get_right_controller_pose_with_rot(self):
        return self.get_controller_pose_with_rot('r')
    
    def get_left_controller_pose_with_rot(self):
        return self.get_controller_pose_with_rot('l')

    # Returns delta position relative to home
    def get_right_controller_delta(self):
        return self.get_right_controller_pose_with_rot() - self.right_controller_home
    
    def get_left_controller_delta(self):
        return self.get_left_controller_pose_with_rot() - self.left_controller_home

    def get_right_trigger(self):
        return self.oculus.get_transformations_and_buttons()[1]['RTr']
    
    def get_left_trigger(self):
        return self.oculus.get_transformations_and_buttons()[1]['LTr']
    
    def get_right_gripper(self):
        return self.oculus.get_transformations_and_buttons()[1]['RG'], self.oculus.get_transformations_and_buttons()[1]['rightGrip'][0]
    
    def get_left_gripper(self):
        return self.oculus.get_transformations_and_buttons()[1]['LG']
    
    def get_A(self):
        return self.oculus.get_transformations_and_buttons()[1]['A']
    
    def get_X(self):
        return self.oculus.get_transformations_and_buttons()[1]['X']

    def get_right_js(self):
        return self.oculus.get_transformations_and_buttons()[1]['rightJS']

    def set_right_controller_home(self):
        self.right_controller_home = self.get_right_controller_pose_with_rot()

    def set_left_controller_home(self):
        self.left_controller_home = self.get_left_controller_pose_with_rot()

    def getEverything(self):
        return self.oculus.get_transformations_and_buttons()
    
    # Returns the delta movements, and the button states
    def getState(self):
        return np.array(self.get_right_controller_delta(), self.get_left_controller_delta(), self.getEverything()[1])

def main():
    reader = OculusWrapper()
    print(reader.getEverything())
    while True:
        print()
        poses, buttons = reader.getEverything()
        # print(poses)
        yaw, pitch, roll = reader.get_right_controller_ypr()
        print(f'Yaw = {yaw}, Pitch = {pitch}, Roll = {roll}')
        time.sleep(0.1)

if __name__ == '__main__':
     main()
