#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


def left_right():
        
        msg=Twist()
        rospy.init_node('leftright')
        lr_pub = rospy.Publisher('/cmd_vel', Twist,queue_size=10)
        
       # msg=rospy.Subscriber('odom', Odometry)  
        #x_pos= msg.pose.pose.position.x
        #y_pos= msg.pose.pose.position.y
        #z_pos= msg.pose.pose.position.z
        
        con="y"
        while(con=="y"):
		con=raw_input("Do you want to continue y/n ")
		dire=raw_input("Enter the string l=left r=right s=stop")
		if dire=="l":
                 moving(-0.2,msg,lr_pub)
                 
		elif dire=="r":
                 moving(0.2,msg,lr_pub)

        	elif dire=="s":
                	msg.linear.y=0
		else:
			print "Wrong choice"
        	lr_pub.publish(msg)
    
def moving(vel,msg,lr_pub):
    nt=0
    distance = input("Enter distance ")
    time=distance/0.2
    ct=rospy.get_time()                
    while (nt-ct<=time):
        msg.linear.y=vel
        lr_pub.publish(msg)
        nt=rospy.get_time()
    msg.linear.y=0
    

if __name__ == '__main__':
   left_right()
