#!/usr/bin/env python

import rospy

from kobuki_msgs.msg import DockInfraRed
from kobuki_msgs.msg import SensorState

class deneme():
	def __init__(self):
		rospy.init_node("mydock_ir", anonymous=True)
		self.sub_dock_ir = rospy.Subscriber("/mobile_base/sensors/dock_ir", DockInfraRed, self.DockIRCallback)
		self.sub_core    = rospy.Subscriber("/mobile_base/sensors/core" , SensorState, self.SensorStateCallback)
		self.bumper = 0
		self.charger = 0
		self.stack = []
    
	def SensorStateCallback(self,data):
		self.bumper = data.bumper
		self.charger = data.charger
    
	def DockIRCallback(self,data):
		#rospy.loginfo("ir data NEAR[LEFT,CENTER,RIGHT]:[%d%d%d]"%(data.NEAR_LEFT,data.NEAR_CENTER,data.NEAR_RIGHT))
		array = [ ord(x) for x in data.data]
		self.stack.append(array)
		array=[0,0,0]
		for i in range(len(self.stack)):
			for j in range(3):
				array[j] |= self.stack[i][j]
		print array
		for ir in array:
			print("{0:#08b}".format(ir)[2:] + " ")
		
		
if __name__ == '__main__':
	try:
		deneme()
		rospy.spin()
	except:
		pass
