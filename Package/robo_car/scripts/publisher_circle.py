#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def robo_car():
    rospy.init_node('robo_car_move', anonymous= True)
    pub_rear= rospy.Publisher('/robo_car/Rear_wheel_motor/command', Float64, queue_size=10)
    pub_right = rospy.Publisher('/robo_car/Front_right_wheel_motor/command', Float64, queue_size=10)
    pub_left = rospy.Publisher('/robo_car/Front_left_wheel_motor/command', Float64, queue_size=10)
    rate = rospy.Rate(10) #2hz
    
    for i in range(150):
        pub_rear.publish(5)
        pub_right.publish(5)
        pub_left.publish(5)
        print('Command Published for the Rear_wheel_motor ~ 5')
        print('Command Published for the Front_left_wheel_motor ~ 5')
        print('Command Published for the Front_right_wheel_motor ~ 5')
        rate.sleep()
    for i in range(150):
        pub_rear.publish(0)
        pub_right.publish(0)
        pub_left.publish(0)
        print('Command Published for the Rear_wheel_motor ~ 0')
        print('Command Published for the Front_left_wheel_motor ~ 0')
        print('Command Published for the Front_right_wheel_motor ~ 0')
        rate.sleep()

if __name__ == '__main__':
    try:
        robo_car()
    except rospy.ROSInterruptException:
        pass
