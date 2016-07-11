#!/usr/bin/env python

'''
this is the lighter version of mymove.py
gogo will publish a twist message on cmd_vel_mux/input/navi 
rate is 10hz you can change go_cmd.linear or angular values to differ the output
'''


import rospy
from geometry_msgs.msg import Twist

def gogo():
	pub=rospy.Publisher('/cmd_vel_mux/input/navi',Twist,queue_size=10)
	rospy.init_node('mypub_easy',anonymous=True)
	rate=rospy.Rate(10)
	go_cmd=Twist()
	go_cmd.linear.x=0.2
	
	while not rospy.is_shutdown():
		pub.publish(go_cmd)
		rate.sleep()
		rospy.loginfo('published.')
		
if __name__=='__main__':
	try:
		gogo()
	except rospy.ROSInterruptException:
		rospy.loginfo('exited.')
		pass
