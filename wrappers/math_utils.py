import math

def restrictVal(val, e):
    return math.copysign(min(math.fabs(val), e),val)

# Takes in a delta movement, and restricts to given apsilon across all axes
def limitPositionMovement(desiredMovement, epsilon):
    assert(epsilon > 0)
    for i in range(3): # Only limit x,y,z
        desiredMovement[i] = restrictVal(desiredMovement[i], epsilon)
    return desiredMovement

# Takes in current and final position and returns the next position
def getMovement(currPos, goalPos, max_movement):
    delta = goalPos - currPos
    movement_limited = limitPositionMovement(delta, max_movement)
    return currPos + movement_limited

def convertControllerAxesToUR5(controllerDelta):
    controllerDelta[2] *= -1
    controllerDelta[1], controllerDelta[2] = controllerDelta[2], controllerDelta[1] # y is z
    controllerDelta[3] *= (math.pi / 2) # Goes from -1 to 1 to -1.57 to 1.57
    controllerDelta[5] *= -1 # Yaw is inverted
    return controllerDelta

def printArray(arr):
    out = "["
    for i in arr:
        out += "{:.2f},".format(i)
    out += "]"
    print(out)
