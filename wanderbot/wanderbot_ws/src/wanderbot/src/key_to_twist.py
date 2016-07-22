#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_map={ 'w':[0,1], 's':[0,-1],'a':[-1,0],'d':[1,0],' ':[0,0]}

def key_callback(msg,twist_pub):
	if len(msg.data)==0 or not key_map.has_key(msg.data[0]):
		return 
	vels=key_map[msg.data[0]]
	t=Twist()
	t.angular.z=vels[0]
	t.linear.x=vels[1]
	twist_pub.publish(t)
	
if __name__=='__main__':
	rospy.init_node('key_to_twist')
	twist_pub=rospy.Publisher('cmd_vel_mux/input/teleop',Twist,queue_size=1)
	rospy.Subscriber('keys',String,key_callback,twist_pub)
	rospy.spin()
