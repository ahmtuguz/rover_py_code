#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
import time
import serial


def joy_cb(data):
	#$0.2,-0.8;
	msg = "$" + f'{data.axes[1]:.2f}' + "," + f'{data.axes[0]:.2f}' + ";"
	print(msg)
	ser.write(msg.encode())

rospy.init_node('joy_cmdVel_stm', anonymous=True)
#ser = serial.Serial("/dev/ttyACM0", 9600, timeout=None)
ser = serial.Serial("/dev/ttyUSB0", 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
rospy.Subscriber("/joy", Joy, joy_cb)
rospy.spin()