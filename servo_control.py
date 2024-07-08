import urx
from time import sleep, time
from math_utils import limitPositionMovement, printArray
import copy

a = 1
v = 0.2

init_pose = [1.57, -1.57, -2.66, -0.6, -1.57, 0]
# init_pose = [3.14, 0, 0, 0, 0, 0]


rob = urx.Robot("192.168.1.2")
rob.set_tcp((0, 0, 0, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
sleep(0.2)  #leave some time to robot to process the setup commands


max_movement = 0.1
timeout = 0.25
move_time = 0.4

rob.movej(init_pose, a, v)

pos = rob.get_pose(True)

orig_pos = pos.pos.array_ref

print(pos)

setpoint = copy.deepcopy(orig_pos)

setpoint[0] -= 0.5
setpoint[1] += 0.25
setpoint[2] += 0.25


for i in range(50):
    curr_pose = rob.get_pose().pos.array_ref
    delta = setpoint - curr_pose
    print("Delta: " + printArray(delta))
    delta = limitPositionMovement(delta, max_movement)
    print("New Delta: " + printArray(delta))

    orient = rob.get_pose().orient.log.array_ref

    finalSetpoint = [0,0,0,0,0,0]
    for i in range(6):
        if(i < 3):
            finalSetpoint[i] = curr_pose[i] + delta[i]
        else:
            finalSetpoint[i] = orient[i - 3]
    print("final setpoint: " + printArray(finalSetpoint))

    rob.servojInvKin(finalSetpoint, wait=False, t=move_time)
    sleep(timeout)






# print(pos.pos)
# print(pos.orient)
# print(pos.orient.log)
# orient = pos.orient.log.array_ref


# changed_pose = [0,0,0,0,0,0]
# changed_pose[0] = pos.pos.x
# changed_pose[1] = pos.pos.y
# changed_pose[2] = pos.pos.z + delta
# changed_pose[3] = orient[0]
# changed_pose[4] = orient[1]
# changed_pose[5] = orient[2]


# print(changed_pose)

# rob.servojInvKin(changed_pose, wait=False, t=move_time)

# sleep(timeout)

# print(rob.get_pose(True))

# for i in range(5):
#     changed_pose[2] += delta # go up
#     rob.servojInvKin(changed_pose, wait=False, t=move_time)
#     sleep(timeout)


# for i in range(5):
#     changed_pose[1] += delta # go forward
#     rob.servojInvKin(changed_pose, wait=False, t=move_time)
#     sleep(timeout)

# for i in range(5):
#     changed_pose[1] += delta # go forward
#     changed_pose[2] -= delta # go down
#     rob.servojInvKin(changed_pose, wait=False, t=move_time)
#     sleep(timeout)

# for i in range(5):
#     changed_pose[0] += delta
#     changed_pose[1] -= delta
#     changed_pose[2] += delta
#     rob.servojInvKin(changed_pose, wait=False, t=move_time)
#     sleep(timeout)

# sleep(1)
# rob.movej(init_pose, a, v)