#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('pub_sub')

def callback(msg):
	pubsub=Int32()
	pubsub.data=msg.data*2
	pub.publish(pubsub)
sub=rospy.Subscriber('number',Int32,callback)
pub=rospy.Publisher('pub',Int32,queue_size=10)

rospy.spin()
