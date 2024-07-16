from wrappers.OculusWrapper import OculusWrapper
from wrappers.UR5Wrapper import UR5Wrapper
from time import sleep
from wrappers.math_utils import convertControllerAxesToUR5
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import threading

# ROS ------------------------
rclpy.init()
node = Node("oculus_controller_node")
velocity_publisher = node.create_publisher(Twist, '/cmd_vel', 10)

# Converts right joystick values to velocities for the
# neobotix base
def convertRightJSValuesToBaseVelocities(rightjs_values):
    js_x, js_y = rightjs_values
    # Scale velocities by 0.2 to limit base speed
    js_x = js_x * 0.2
    js_y = js_y * 0.2
    # x and y axes between oculus controller and base are flipped
    # polarity is also flipped in the x direction
    base_vel_x = js_y
    base_vel_y = -1 * js_x
    return [base_vel_x, base_vel_y]

def sendRotationalBaseVelocities(js_values):
  js_x, js_y = js_values
  js_x = js_x * -0.2
  rotate_right = True if js_x > 0 else False
  vel = Twist()
  if rotate_right:
     vel.angular.z = js_x
  else:
     vel.angular.z = js_x
  velocity_publisher.publish(vel)

def sendBaseVelocities(rightjs_values):
    velocities = convertRightJSValuesToBaseVelocities(rightjs_values)
    vel = Twist()
    vel.linear.x = velocities[0]
    vel.linear.y = velocities[1]
    vel.linear.z = 0.0
    velocity_publisher.publish(vel)

def controlBase(oculus_controller):
    while(True):
        r_trigger = oculus_controller.get_right_trigger()
        if r_trigger:
            rightjs_values = oculus_controller.get_right_js()
            if not (rightjs_values == (0.0, 0.0)):
              print("rightjs_values: ", rightjs_values)
            #sendBaseVelocities(rightjs_values)
            sendRotationalBaseVelocities(rightjs_values)


# URX -------------------------

right_robot_ip = "192.168.1.2"
left_robot_ip = "192.168.2.2"


timeout = 0.25

right_robot = UR5Wrapper(right_robot_ip)
left_robot = UR5Wrapper(left_robot_ip)
controller = OculusWrapper()

right_robot.reset_to_init()
left_robot.reset_to_init()

prev_held_trigger = False

base_control_thread = threading.Thread(
    target=controlBase, args=(controller,))
base_control_thread.start()

while(True):
  reset_robots = controller.get_A()
  if(reset_robots):
    right_robot.reset_to_init()
    left_robot.reset_to_init()

  right_trigger = controller.get_right_trigger()

  if(right_trigger):
    if(not prev_held_trigger):
      print("New trigger")
      controller.set_right_controller_home()
      right_robot.set_home_position()
      left_robot.set_home_position()
    
    delta_movement = controller.get_right_controller_delta()
    delta_movement = convertControllerAxesToUR5(delta_movement)

    right_robot.go_to_position(delta_movement, wait=False)
    left_robot.go_to_position(delta_movement, wait=False)
    sleep(timeout)
  else:
    right_robot.stop()
    
  prev_held_trigger = right_trigger

