#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def callback(msg):
    print('Received Speed', msg.data)

def straight_line():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Straight_line')
    rospy.Subscriber('/robo_car/Rear_wheel_motor/command', Float64, callback, queue_size = 10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        straight_line()
    except rospy.ROSInterruptException:
        pass
