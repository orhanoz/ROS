#!/usr/bin/env python

'''
information will be published on cmd_vel_mux/input/navi as a twist message
you can change gogo.linear or .angular values to different movement types
rate is 10hz queue size is 10
'''

import rospy
from geometry_msgs.msg import Twist

class gogogo():
	def __init__(self):
		rospy.init_node('mypub',anonymous=False)
		rospy.on_shutdown(self.shutdown)
		self.cmd_vel=rospy.Publisher('/cmd_vel_mux/input/navi',Twist,queue_size=10)
		rate=rospy.Rate(10)
		gogo=Twist()
		gogo.linear.x=0.2
	
		while not rospy.is_shutdown():
			self.cmd_vel.publish(gogo)
			rospy.loginfo('published')
			rate.sleep()
	def shutdown(self):
		self.cmd_vel.publish(Twist())
		rospy.sleep(1)

if __name__ == '__main__':
	try:
		gogogo()
	except:
		rospy.loginfo('oops')
