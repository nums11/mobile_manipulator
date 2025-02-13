
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

    def reset(self):
        """
        Call this method to reset the start position for the deltas call.
        """
        self.cur_pos = self.get_cur_pos()

    def get_cur_pos(self):
        """
        Internal method, this returns the positon of the right controller
        """
        # print(self.oculus.get_transformations_and_buttons()[0])
        transform = self.oculus.get_transformations_and_buttons()[0]['r']

        return transform[:, 3]
    
    def get_ypr(self):
        transform = self.oculus.get_transformations_and_buttons()[0]['r']
        yaw = transform[0][0]
        roll = transform[1][0]
        pitch = transform[1][1]
        return yaw, pitch, roll

    def get_cur_pose_with_rot(self):
        pose = self.get_cur_pos()[:3]
        y,p,r = self.get_ypr()
        output = [0,0,0,0,0,0]
        output[:3] = pose
        output[3] = y
        output[4] = p
        output[5] = r
        return output

    def getEverything(self):
        return self.oculus.get_transformations_and_buttons()


    def get_buttons(self):
        """
        Returns the buttons.
        The ones on the right are "A, B, RTr"
        """
        return self.oculus.get_transformations_and_buttons()[1]

    def get_deltas(self):
        """
        This method returns the deltas of the vr controller since the last time this or 
        reset method has been called. It returns them of the form x, y, z in centimeters
        where positive x is closer to the headset, positive y is left of the headset, 
        and positive z is upwards
        """
        new_pose = self.get_cur_pos()
        deltas = new_pose - self.cur_pos
        self.cur_pos = new_pose

        final_deltas = [0,0,0]
        final_deltas[2] = deltas[1]
        final_deltas[1] = deltas[0] 
        final_deltas[0] = deltas[2] 
        final_deltas = np.array(final_deltas) * 100
        for i , delta in enumerate(final_deltas):
            final_deltas[i] = delta if delta > .5 or delta < -.5 else 0
        return final_deltas

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