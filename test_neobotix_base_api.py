from NeobotixBase import NeobotixBase
from pynput.keyboard import Key, Listener
import rclpy

rclpy.init()
base = NeobotixBase()

def on_press(key):
  print("Pressed key")
  if key.char == 'w':
    base.moveForward()
  elif key.char == 'a':
    base.moveLeft()
  elif key.char == 'd':
    base.moveRight()
  elif key.char == 's':
    base.moveBackward()
  elif key.char == 'q':
    return False

print("Enter key for movement: 'w', 'a', 's', 'd'")
with Listener(
        on_press=on_press) as listener:
    listener.join()

zzzzZZZzzzthe_usual