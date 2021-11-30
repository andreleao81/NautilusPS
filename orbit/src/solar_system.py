#!/usr/bin/env python3

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
import math
import random

class RandomTransform:

    def __init__(self, planet):
        rospy.init_node('random_transform', anonymous = True)

        self.tf = TransformStamped()
        self.tf.header.frame_id = 'center_of_the_universe'
        self.tf.child_frame_id = planet[0] # planet's name
        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.rotation.w = 1
        self.r = planet[1] # planet's radius
        self.v = planet[2] # planet's velocity

        self.broadcaster = tf2_ros.TransformBroadcaster()
    
    def broadcast(self):

        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.translation.x = math.sin(self.v*kTime)*self.r
        self.tf.transform.translation.y = math.cos(self.v*kTime)*self.r
        self.tf.transform.translation.z = 0

        self.broadcaster.sendTransform(self.tf)
        

if __name__ == '__main__':
    # param 'planets' is a dictionary of lists containing planet's information
    rndtf = [ RandomTransform(planet) for planet in rospy.get_param('planets') ]
    kTime = 0 
    rate = rospy.Rate(30) 
    
    while not rospy.is_shutdown():
        kTime += 0.01   
        for rndtransform in rndtf:
            rndtransform.broadcast()
        rate.sleep()