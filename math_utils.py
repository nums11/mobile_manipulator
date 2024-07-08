import math

def restrictVal(val, e):
    return math.copysign(min(math.fabs(val), e),val)

def limitPositionMovement(desiredMovement, epsilon):
    assert(epsilon > 0)
    desiredMovement[0] = restrictVal(desiredMovement[0], epsilon)
    desiredMovement[1] = restrictVal(desiredMovement[1], epsilon)
    desiredMovement[2] = restrictVal(desiredMovement[2], epsilon)

    return desiredMovement

def printArray(arr):
    out = "["
    for i in arr:
        out += "{:.2f},".format(i)
    out += "]"
    return out

array = [0.124124,120.123123, 123.052323]
a = printArray(array)
print(a)