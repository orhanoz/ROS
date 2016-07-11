#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import radians

class Movee():
	def __init__(self):
		rospy.init_node('moveshape', anonymous=False)
		#node adi moveshape ve tekil
		rospy.loginfo("crtl+c to stop")
		#log info
		rospy.on_shutdown(self.shutdown)
		#kendilerini kapatsinlar
		
		self.cmd_vel=rospy.Publisher('cmd_vel_mux/input/navi',Twist,queue_size=10)
		#cmd_vel o noda twist mesaji yolliyacak..
		r=rospy.Rate(5);
		#saniyede 5 mesaj degistirip denenebilir
		
		#---------ileri go--------
		
		ileri_cmd=Twist()
		ileri_cmd.linear.x=0.2
		ileri_cmd.angular.z=0
		
		#--------donus yap--------
		turn_cmd=Twist()
		turn_cmd.linear.x=0
		turn_cmd.angular.z=radians(45);
		#-------------------------
		while not rospy.is_shutdown():
			#ileri gogogo
			rospy.loginfo("ileri go")
			for x in range(0,10): #can change for accuracy
				self.cmd_vel.publish(ileri_cmd)
				r.sleep()
			#turn loop
			rospy.loginfo("Turning")
			for x in range(0,15):
				self.cmd_vel.publish(turn_cmd)
				r.sleep()            

	def shutdown(self):
		rospy.loginfo("stop")
		self.cmd_vel.publish(Twist())
		rospy.sleep(1)

if __name__ == '__main__':
	try:
		Movee()
	except:
		rospy.loginfo("terminatorrr!")

