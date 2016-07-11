#!/usr/bin/env python

'''
if you have a map file you can use this to go to a location just get the coords from rviz you wish to go
and put them in position ...
'''

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

class gotopose():
	def __init__(self):
		self.goal_sent = False
		rospy.on_shutdown(self.shutdown)
		self.move_base=actionlib.SimpleActionClient("move_base",MoveBaseAction)
		rospy.loginfo("action server waiting..")
		self.move_base.wait_for_server(rospy.Duration(5))
	
	def goto(self,pos,quat):
		self.goal_sent=True
		goal=MoveBaseGoal()
		goal.target_pose.header.frame_id='map'
		goal.target_pose.header.stamp=rospy.Time.now()
		goal.target_pose.pose=Pose(Point(pos['x'],pos['y'],0.00),Quaternion(quat['r1'],quat['r2'],quat['r3'],quat['r4']))
		
		#gogo move
		self.move_base.send_goal(goal)
		##60 secs to complete the task
		success=self.move_base.wait_for_result(rospy.Duration(60))
		state=self.move_base.get_state()
		result=False
		
		if success and state == GoalStatus.SUCCEEDED:
			result=True
		else:
			self.move_base.cancel_goal()
			
		self.goal_sent=False
		return result
	def shutdown(self):
		if self.goal_sent:
			self.move_base.cancel_goal()
		rospy.loginfo("Stopped")
		rospy.sleep(1)
if __name__=='__main__':
	try:
		rospy.init_node('nav_test',anonymous=False)
		navigator=gotopose()
		
		position={'x':0.454 , 'y':-0.277}
		quarternion={'r1':0.000,'r2':0.000,'r3':0.000,'r4':1.000}
		rospy.loginfo("Go to (%s , %s) pose",position['x'],position['y'])
		success=navigator.goto(position,quarternion)
		
		if success:
			rospy.loginfo("reached the pose")
		else:
			rospy.loginfo("failed to go")
			
		rospy.sleep(1)
		
	except rospy.ROSInterruptException:
		rospy.loginfo("shut down")
