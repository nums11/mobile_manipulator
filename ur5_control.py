import urx
from time import sleep

a = 0.1
v = 0.1

rob = urx.Robot("192.168.1.2")
rob.set_tcp((0, 0, 0, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
sleep(0.2)  #leave some time to robot to process the setup commands

pos = rob.getj()
print(pos)
rob.movej((pos[0], pos[1], pos[2], pos[3], pos[4], pos[5]+0.3), a, v)


"""
rob.movel((x, y, z, rx, ry, rz), a, v)
print("Current tool pose is: ",  rob.getl())
rob.movel((0.1, 0, 0, 0, 0, 0), a, v, relative=true)  # move relative to current pose
rob.translate((0.1, 0, 0), a, v)  #move tool and keep orientation
rob.stopj(a)

rob.movel((x, y, z, rx, ry, rz), wait=False)
while True :
    sleep(0.1)  #sleep first since the robot may not have processed the command yet
    if rob.is_program_running():
        break

rob.movel((x, y, z, rx, ry, rz), wait=False)
while rob.getForce() < 50:
    sleep(0.01)
    if not rob.is_program_running():
        break
rob.stopl()

try:
    rob.movel((0,0,0.1,0,0,0), relative=True)
except(RobotError, ex):
    print("Robot could not execute move (emergency stop for example), do something", ex)
"""
