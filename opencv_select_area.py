#!/usr/bin/env python

import roslib
roslib.load_manifest('beginner_tutorials')
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class test_vision_node:
	def __init__(self):
		rospy.init_node('test_node')
		self.bridge=CvBridge()
		
		self.image_sub = rospy.Subscriber("/camera/rgb/image_color", Image, self.callback,queue_size=1)
		
	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)
			
		area=cv_image[300:450,50:450]
			
		cv2.imshow("image",cv_image)
		cv2.imshow("other",area)
		cv2.waitKey(3)
		
def main():
	vn=test_vision_node()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "quitting"
	cv2.DestroyAllWindows()

if __name__=='__main__':
	main()
