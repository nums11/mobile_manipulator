import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class NeobotixBase(Node):
	def __init__(self):
		super().__init__('neo_base_controller')
		self.vel_pub = self.create_publisher(Twist,"/cmd_vel",10)

	def moveForward(self):
		if rclpy.ok():
			self.sendVelocity(0.1, 0.0, 0.0)

	def moveBackward(self):
		if rclpy.ok():
			self.sendVelocity(-0.1, 0.0, 0.0)

	def moveLeft(self):
		if rclpy.ok():
			self.sendVelocity(0.0, 0.1, 0.0)

	def moveRight(self):
		if rclpy.ok():
			self.sendVelocity(0.0, -0.1, 0.0)

	def sendVelocity(self, x, y, z):
		vel = Twist()
		vel.linear.x = x
		vel.linear.y = y
		vel.linear.z = z
		for i in range(75):
			self.vel_pub.publish(vel)
			time.sleep(0.005)
		self.stopRobot()

	def stopRobot(self):
		zero_vel = Twist()
		zero_vel.linear.x = 0.0
		zero_vel.linear.y = 0.0
		zero_vel.linear.z = 0.0
		self.vel_pub.publish(zero_vel)
