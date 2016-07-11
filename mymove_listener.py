#!/usr/bin/env python

'''
this code will subscribe /cmd_vel_mux/input/navi
takes the data and logs the info
you can use the same method on other nodes to get their data logged...
'''

import rospy
from geometry_msgs.msg import Twist

def callback(data):
	rospy.loginfo('Linear  xyz:[%f, %f, %f]'%(data.linear.x,data.linear.y,data.linear.z))
	rospy.loginfo('Angular xyz:[%f, %f, %f]'%(data.angular.x,data.angular.y,data.angular.z))
	
	
def listener():
	rospy.init_node('mymove_listener')
	rospy.Subscriber('/cmd_vel_mux/input/navi',Twist,callback)
	rospy.spin()
	
if __name__=='__main__':
	listener()	
