#!/usr/bin/env python

'''
this shows how you can take imu data from /mobile_base/sensors/imu_data
the data is logged as quaternion , linear accel , angular velocity
'''

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion , Vector3

def callback(data):
	rospy.loginfo('HeaderID: %s'%data.header.frame_id)
	rospy.loginfo('Timestamp: %s'%data.header.stamp)
	rospy.loginfo('Quaternion data:[%f ,%f ,%f ,%f]'%(data.orientation.x,data.orientation.y,data.orientation.z,data.orientation.w))
	rospy.loginfo('Linear acceleration:[%f ,%f ,%f]'%(data.linear_acceleration.x,data.linear_acceleration.y,data.linear_acceleration.z))
	rospy.loginfo('Angular velocity:[%f ,%f ,%f]'%(data.angular_velocity.x,data.angular_velocity.y,data.angular_velocity.z))
	
	
def listener():
	rospy.init_node('myimu_listener')
	rospy.Subscriber('/mobile_base/sensors/imu_data',Imu,callback)
	rospy.spin()
	
if __name__ == '__main__':
	listener()
