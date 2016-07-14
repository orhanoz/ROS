#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

key_map={ 'w':[0,1], 's':[0,-1],'a':[-1,0],'d':[1,0],' ':[0,0]}

g_last_twist=None
g_vel_scales=[0.1,0.1]

def key_callback(msg,twist_pub):
	global g_last_twist,g_vel_scales
	if len(msg.data)==0 or not key_map.has_key(msg.data[0]):
		return
	vels=key_map[msg.data[0]]
	g_last_twist.angular.z=vels[0]*g_vel_scales[0]
	g_last_twist.linear.x=vels[1]*g_vel_scales[1]
	twist_pub.publish(g_last_twist)
	
if __name__=='__main__':
	rospy.init_node('keys_to_twist')
	twist_pub=rospy.Publisher('cmd_vel_mux/input/teleop',Twist,queue_size=1)
	rospy.Subscriber('keys',String,key_callback,twist_pub)
	g_last_twist=Twist()
	if rospy.has_param('~linear_scale'):
		g_vel_scales[1]=rospy.get_param('~linear_scale')
	else:
		rospy.logwarn("linear scale not given using %.1f"%g_vel_scales[1])
	if rospy.has_param('~angular_scale'):
		g_vel_scales[0]=rospy.get_param('~angular_scale')
	else:
		rospy.logwarn("angular scale not given using %.1f"%g_vel_scales[0])
		
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		twist_pub.publish(g_last_twist)
		rate.sleep()
