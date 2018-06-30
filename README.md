# pepper_cerebrum
This is a ROS executive node. This node will combine the speech-to-text node, the text-to-speech node and the ros_yolo node.
This node is made so that we can ask Pepper if there are any snickers. Pepper will respond with an answer.

## How to use
### downloading everything
If you want to use this node you will also need to install the following projects.
- Speech-to-text: https://github.com/PXLRoboticsLab/STT4ROS
- Text-to-speech: https://github.com/PXLRoboticsLab/TTS4ROS
- ROS_yolo: https://github.com/PXLRoboticsLab/darknet 

And for these to work with pepper you will also need to install naoqi. A guide for this can be found [here](https://github.com/PXLRoboticsLab/ROS_Pepper/blob/master/ROS-Pepper.md)

### Start the node
You can start the node individually by using the following command: \
`$ rosrun pepper_cerebrum executive.py` \
If you want to start the executive node and ros_yolo you can use following command: \
`$ roslaunch pepper_cerebrum test.launch` \
If you want to start all the nodes at once, you can use the following command: \
`$ roslaunch pepper_cerebrum demo.launch` 

## What is what
### bin folder
In this folder there are two launch files for ROS. The launch file demo will start all the necesarry nodes if you have them on your computer.
The launch file test only start the pepper cerebrum executive and the ros_yolo node.

### src folder
In here you can find the python file executive.py which is the brain that let's everything work together.
