#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

pub = rospy.Publisher('/key', String, queue_size=10)
rospy.init_node('auto_controller', anonymous=True)

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
    rate = rospy.Rate(1000)
    l=[]
    for i in range(540):
        l.append(msg.ranges[i])
    d=(l[0]+l[539])/2
    rospy.loginfo("%s %s %s "%(l[0],l[539],d))
    if l[0]>d:
        pub.publish("d")
        rospy.loginfo("d")
        pub.publish("w")
        rospy.loginfo("w")
    elif l[0]<d:
        pub.publish("a")
        rospy.loginfo("a")
        pub.publish("w")
        rospy.loginfo("w")
    else:
        pub.publish("w")
        rospy.loginfo("w")
    rate.sleep()


if __name__ == '__main__':
    try:
        sub = rospy.Subscriber('/scan', LaserScan, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
