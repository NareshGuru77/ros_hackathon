#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def call_front(msg):
	
	x1=msg.ranges
	print x1
	
	twist=Twist()
	
	msg.angle_min=0.2
	msg.angle_max=-0.2

	print msg.angle_min
	print msg.angle_max
	for i in range (0,10):
		#print x1[i]
		if x1[i]>=5.59:

			twist.linear.x=0.2
		
		else:
			flag=1
			twist.linear.x=-0.2

	
	lr_pub.publish(twist)


#def call_back(msg):
	#y=msg.ranges
	


def main():
	global lr_pub
	rospy.init_node('listener', anonymous=True)
	lr_pub=rospy.Publisher('/cmd_vel', Twist,queue_size=10)
	rospy.Subscriber('/base_scan_front', LaserScan, call_front)
	#rospy.Subscriber('/base_scan_back',LaserScan,call_back)

	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		rate.sleep()

		pass
    
if __name__ == '__main__':
		main()
	
   

