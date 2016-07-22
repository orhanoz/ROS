#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_map={ 'w':[0,1], 's':[0,-1],'a':[-1,0],'d':[1,0],' ':[0,0]}

g_last_twist=None

def key_callback(msg,twist_pub):
	global g_last_twist
	if len(msg.data)==0 or not key_map.has_key(msg.data[0]):
		return
	vels=key_map[msg.data[0]]
	g_last_twist.angular.z=vels[0]
	g_last_twist.linear.x=vels[1]
	twist_pub.publish(g_last_twist)
	
if __name__ =='__main__':
	rospy.init_node('keys_to_twist')
	twist_pub=rospy.Publisher('cmd_vel_mux/input/teleop',Twist,queue_size=1)
	rospy.Subscriber('keys',String,key_callback,twist_pub)
	rate=rospy.Rate(10)
	g_last_twist=Twist()
	while not rospy.is_shutdown():
		twist_pub.publish(g_last_twist)
		rate.sleep()
