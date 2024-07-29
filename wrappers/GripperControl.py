import numpy as np

class GraspMode:
  BASIC = 0
  PINCH = 2
  WIDE = 4
  SCISSOR = 6

class Finger:
    A = 0
    B = 1
    C = 2
    All = 3
    
class Position:
    OPENED = 0
    CLOSED = 255
