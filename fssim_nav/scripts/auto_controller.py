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
    l=[]
    # rate = rospy.Rate(1000)
    for i in range(540):
        l.append(msg.ranges[i])
    if 'inf' in l:
        pass
    elif min(l)<0.1:
        pub.publish("s")
        rospy.loginfo("s")
        # rate.sleep()
    else :
        d=[]
        idx=[]
        for y in range(540) :
            if l[y]>1.5:
                d.append(l[y])
                idx.append(y)
            # if l[y]>1:
            #     d.append(l[y])
            #     idx.append(y)
            else:
                if len(d)<35:
                    d=[]
                    idx=[]
                else:
                    if abs(l[idx[0]]-l[idx[0]-1])>0.3:
                        for z in range(20):
                            d[z]=0
                    if abs(l[idx[-1]]-l[idx[-1]+1])>0.3:
                        for z in range(-20,0,-1):
                            d[z]=0
                    m=max(d)
                    index=l.index(m)
                    rospy.loginfo("%s %s"%(m,index))

                    # if index<180:
                    #     pub.publish("d")
                    #     rospy.loginfo("d")
                    #     pub.publish("w")
                    #     rospy.loginfo("w")
                    # elif index>360:
                    #     pub.publish("a")
                    #     rospy.loginfo("a")
                    #     pub.publish("w")
                    #     rospy.loginfo("w")
                    # elif index>180 or index<360:
                    #     pub.publish("w")
                    #     rospy.loginfo("w")
                    if index<270:
                        pub.publish("d")
                        rospy.loginfo("d")
                        pub.publish("w")
                        rospy.loginfo("w")
                        # rate.sleep()
                    elif index>270:
                        pub.publish("a")
                        rospy.loginfo("a")
                        pub.publish("w")
                        rospy.loginfo("w")
                        # rate.sleep()
                    # return 0

if __name__ == '__main__':
    try:
        sub = rospy.Subscriber('/scan', LaserScan, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
