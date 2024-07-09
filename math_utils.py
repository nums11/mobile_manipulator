import math

def restrictVal(val, e):
    return math.copysign(min(math.fabs(val), e),val)

def limitPositionMovement(desiredMovement, epsilon):
    assert(epsilon > 0)
    for i in range(len(desiredMovement)):
        desiredMovement[i] = restrictVal(desiredMovement[i], epsilon)
    return desiredMovement

def getMovement(currPos, goalPos, max_movement):
    delta = goalPos - currPos
    movement_limited = limitPositionMovement(delta, max_movement)
    return currPos + movement_limited

def printArray(arr):
    out = "["
    for i in arr:
        out += "{:.2f},".format(i)
    out += "]"
    print(out)