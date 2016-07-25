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
			
		#cv_image=(255-cv_image)
		area_img=cv_image[300:450,50:450]
		g_img=cv2.cvtColor(area_img,cv2.COLOR_BGR2GRAY)
		g_img=cv2.GaussianBlur(g_img,(5,5),200)
		thresh=cv2.Canny(g_img,15,50,3)
		lines = cv2.HoughLinesP(thresh,2,np.pi/180,10,10,1)
		print lines.shape
		for i in range(0,lines.shape[0]):
			for x1,y1,x2,y2 in lines[i]:
				cv2.line(area_img,(x1,y1),(x2,y2),(0,255,0),2)
		cv2.imshow("real",cv_image)	
		cv2.imshow("image",area_img)
		cv2.imshow("other",thresh)
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
