#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped 

# pub = rospy.Publisher('/key', String, queue_size=10)
# rospy.init_node('auto_controller', anonymous=True)

# def talker():
#     pub = rospy.Publisher('key', String, queue_size=10)
#     rospy.init_node('auto_controller', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()
#         rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         rate.sleep()

def callback(msg):
    ack_msg = AckermannDriveStamped()
    ack_msg.header.stamp = rospy.Time.now()
    ack_msg.header.frame_id = 'your_frame_here'
    pub.publish(ack_msg)
    l=[]
    for i in range(540):
        l.append(msg.ranges[i])
    d=(l[0]+l[539])/2
    rospy.loginfo("%s %s %s "%(l[0],l[539],d))
    if l[0]>d:
        ack_msg.drive.steering_angle = -0.3
        ack_msg.drive.speed = 2
        pub.publish(ack_msg)
        rospy.loginfo(ack_msg)
        # pub.publish("d")
        # rospy.loginfo("d")
        # pub.publish("w")
        # rospy.loginfo("w")
    elif l[0]<d:
        ack_msg.drive.steering_angle = 0.3
        ack_msg.drive.speed = 2
        pub.publish(ack_msg)
        rospy.loginfo(ack_msg)
    else:
        ack_msg.drive.speed = 2
        pub.publish(ack_msg)
        rospy.loginfo(ack_msg)



if __name__ == '__main__':
    try:
        pub = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=1)
        rospy.init_node('auto_controller', anonymous=True)
        # rospy.init_node('scan_values', anonymous=True)
        sub = rospy.Subscriber('/scan', LaserScan, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
