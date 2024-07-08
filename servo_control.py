import urx
from time import sleep, time
import math

a = 1
v = 0.2

init_pose = [1.57, -1.57, -2.66, -0.6, -1.57, 0]
# init_pose = [3.14, 0, 0, 0, 0, 0]


rob = urx.Robot("192.168.1.2")
rob.set_tcp((0, 0, 0, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
sleep(0.2)  #leave some time to robot to process the setup commands


rob.movej(init_pose, a, v)

pos = rob.get_pose(True)

orig_pos = pos.pos.array_ref


print(pos.pos)
print(pos.orient)
print(pos.orient.log)
orient = pos.orient.log.array_ref

delta = 0.04
timeout = 0.25

changed_pose = [0,0,0,0,0,0]
changed_pose[0] = pos.pos.x
changed_pose[1] = pos.pos.y
changed_pose[2] = pos.pos.z + delta
changed_pose[3] = orient[0]
changed_pose[4] = orient[1]
changed_pose[5] = orient[2]


print(changed_pose)


move_time = 0.4

rob.servojInvKin(changed_pose, wait=False, t=move_time)

sleep(timeout)

print(rob.get_pose(True))

for i in range(5):
    changed_pose[2] += delta # go up
    rob.servojInvKin(changed_pose, wait=False, t=move_time)
    sleep(timeout)


for i in range(5):
    changed_pose[1] += delta # go forward
    rob.servojInvKin(changed_pose, wait=False, t=move_time)
    sleep(timeout)

for i in range(5):
    changed_pose[1] += delta # go forward
    changed_pose[2] -= delta # go down
    rob.servojInvKin(changed_pose, wait=False, t=move_time)
    sleep(timeout)

for i in range(5):
    changed_pose[0] += delta
    changed_pose[1] -= delta
    changed_pose[2] += delta
    rob.servojInvKin(changed_pose, wait=False, t=move_time)
    sleep(timeout)

sleep(1)
rob.movej(init_pose, a, v)

# speeds = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
# print("Entering speedl")
# rob.speedl(speeds, 0.2, min_time=1)


# for i in range(5):
#     print("\nSending new movement")

#     init_pose[0] -= math.radians(10)
#     init_pose[1] -= math.radians(10)

#     print("new pose: " + str(init_pose))
    
#     prevTime = time()
#     rob.servoj(init_pose,acc=5,vel=5, t=0.5, wait=True)
#     print("time taken is: " + str(time() - prevTime))
    
#     data = rob.get_all_rt_data(wait=False)
#     print(data)

#     # sleep(timeout)
#     pos = rob.getj()
#     print("Robot pos: " + str(pos))