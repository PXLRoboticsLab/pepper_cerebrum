#!/usr/bin/env python
import rospy
import cv2
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from ros_yolov3.msg import Detection, Object
from std_msgs.msg import String
from collections import Counter

class Subscriber_node:
    def __init__(self):
        self.question = False
        self.list = []
        self.counter = 0
        self.x = 1
        self.start_time = time.time()
        
        rospy.Subscriber("yolo_annotation", Detection, self.callback, queue_size=1, buff_size=2 ** 24)
        rospy.Subscriber("stt", String, self.questionCallback, queue_size=1, buff_size=2 ** 24)
        self.answer_publisher = rospy.Publisher('tts', String, queue_size=1)
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    def questionCallback(self, data):
        if 'Snickers' in data.data or 'candy' in data.data or 'sneakers' in data.data or 'snakes' in data.data:
            self.question = True

    def callback(self, data):
        for obj in data.object_list:
            self.list.append(obj.object_name)

        self.counter += 1
        if (time.time() - self.start_time) > self.x:
            self.counter = 0
            self.start_time = time.time()
            if self.question:
                #word = Counter(self.list).most_common(1)[0][0]
                if 'Snicker' in self.list:
                    self.answer_publisher.publish("I see Snickers")
                else:
                    self.answer_publisher.publish('I cannot find any Snickers')
                self.question = False
            
            self.list = []
        

def main():
    rospy.init_node('yolo_annotation', anonymous=True)
    Subscriber_node()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS object detection with YOLOv3"
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()