#!/usr/bin/env python
import rospy
from websocket import create_connection
import requests
import json
import socket
import datetime
import sys
import logging, os
import time
import threading

from std_msgs.msg import String, Header, Float64
from sensor_msgs.msg import NavSatFix,TimeReference, BatteryState, Range, Temperature, FluidPressure
from mavros_msgs.msg import PositionTarget, State, ADSBVehicle, RCIn, RCOut

# Geometry message type
from geometry_msgs.msg import Twist, TwistStamped, Vector3, Pose, Point, PoseWithCovariance, Quaternion, PoseStamped
from nav_msgs.msg import Odometry

def get_now():
    return datetime.datetime.now()


def state_callback(data):
	#rospy.loginfo(rospy.get_caller_id())
	print("data.mode : "+str(data.mode))
	print("data.connected : "+str(data.connected))
def battery_callback(data):
        #print(get_now());	
        #rospy.loginfo(rospy.get_caller_id())
	#print("data.voltage : "+str(data.voltage))
	newItem={
                "r1ID": "9e64",
		"value":str({
                	"battery":data.voltage
                        }),
                "timestamp":str(get_now())
                }

       
	serverAddr=("18.222.149.253",9998)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #print(str(newItem));
	client_socket.sendto(json.dumps(newItem),serverAddr)

	#url_items="http://localhost:5055/globalP_local"
	url_items="http://18.222.149.253:5056/battery"

        print("\nSending battery state")
        print(newItem)
	response=requests.post(url_items, data=newItem)
	#print(response.text)


def adsbVehicle_callback(data):
	#rospy.loginfo(rospy.get_caller_id())
	#print("data.callsign : "+data.callsign)
	print(str(data))

def rangeF_callback(data):
	#rospy.loginfo(rospy.get_caller_id())
	
	print(str(data.min_range))

def compass_callback(data):
	#rospy.loginfo(rospy.get_caller_id())
	print("Compass_hdg data : "+str(data.data))

def global_callback(data):
	#rospy.loginfo(rospy.get_caller_id())
	print("longitude : "+str(data.longitude)+", latitude : "+str(data.latitude))

def temperature_baro_callback(data):
	#rospy.loginfo(rospy.get_caller_id())
	#print("temperature : "+str(data.temperature)+", variance : "+str(data.variance))

	newItem={
                "r1ID": "9e64",
		"value":str({
                        "temperature":data.temperature,
                        "variance":data.variance
                        }),
                "timestamp":str(get_now())
                }

       
	serverAddr=("18.222.149.253",9998)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #print(str(newItem));
	client_socket.sendto(json.dumps(newItem),serverAddr)

	#url_items="http://localhost:5055/globalP_local"
	url_items="http://18.222.149.253:5056/temperature_baro"
        print("\nSending temperature_baro")
        print(newItem)
	response=requests.post(url_items, data=newItem)
	#print(response.text)

def static_pressure_callback(data):
	print("fluid_pressure : "+str(data.fluid_pressure)+", variance : "+str(data.variance))

def rcIN_callback(data):
	print("RC_IN_channels : "+str(data.channels))

def rcOUT_callback(data):
	print("RC_OUT_channels : "+str(data.channels))



def globalP_local_callback(data):
	#print("pose.x: "+str(data.pose.pose.position.x))
	#print("pose.y: "+str(data.pose.pose.position.y))
	#print("pose.z: "+str(data.pose.pose.position.z))
	#print("orientation.x: "+str(data.pose.pose.orientation.x))
	#print("orientation.y: "+str(data.pose.pose.orientation.y))
	#print("orientation.z: "+str(data.pose.pose.orientation.z))
	#print("orientation.w: "+str(data.pose.pose.orientation.w))
	

        newItem={
                "r1ID": "9e64",
		"value":str(
                    {"posex":data.pose.pose.position.x,
                    "posey":data.pose.pose.position.y,
                    "posez":data.pose.pose.position.z,
                    "orix":data.pose.pose.orientation.x,
                    "oriy":data.pose.pose.orientation.y,
                    "oriz":data.pose.pose.orientation.z,
                    "oriw":data.pose.pose.orientation.w}
                    ),
                "timestamp":str(get_now())
                }

        #websockets.connect("http://localhost:9999")
        #websockets.send(json.dumps(newItem))
	
        #ws = create_connection("ws://localhost:8080")
        #ws.send(json.dumps(newItem))
        #serverAddr=("127.0.0.1",9998)
	serverAddr=("18.222.149.253",9998)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #print(str(newItem));
	client_socket.sendto(json.dumps(newItem),serverAddr)

	#url_items="http://localhost:5055/globalP_local"
	url_items="http://18.222.149.253:5056/globalP_local"
        print("\nSending globalPosition_local")
        print(newItem)
	response=requests.post(url_items, data=newItem)
	#print(response.text)



def listener():
	# In ROS, nodes are uniquely named. If two nodes with the same
	# name are launched, the previous one is kicked off. The
    	# anonymous=True flag means that rospy will choose a unique
    	# name for our 'listener' node so that multiple listeners can
    	# run simultaneously.
    	rospy.init_node('listener', anonymous=True)

    	#rospy.Subscriber("/mavros/state", State, state_callback)
    	rospy.Subscriber("/mavros/battery", BatteryState, battery_callback)
    	#rospy.Subscriber("/robot_pose", PoseStamped, robot_pose_callback) does not echo
    	#rospy.Subscriber("/mavros/adsb/vehicle", ADSBVehicle, adsbVehicle_callback)
    	#rospy.Subscriber("/mavros/distance_sensor/rangefinder_pub", Range, rangeF_callback)
    	#rospy.Subscriber("/mavros/global_position/compass_hdg", Float64, compass_callback)
    	#rospy.Subscriber("/mavros/global_position/global", NavSatFix, global_callback)
    	rospy.Subscriber("/mavros/imu/temperature_baro", Temperature, temperature_baro_callback)
    	#rospy.Subscriber("/mavros/imu/static_pressure", FluidPressure, static_pressure_callback)
    	#rospy.Subscriber("/mavros/rc/in",RCIn,rcIN_callback)
    	#rospy.Subscriber("/mavros/rc/out",RCOut,rcOUT_callback)
    	rospy.Subscriber("/mavros/global_position/local",Odometry,globalP_local_callback)
    	#rospy.Subscriber("/mavros/local_position/pose",PoseStamped,localP_pose_callback) does not echo
        #rospy.Subscriber("/mavros/local_position/velocity",TwistStamped,localP_velo_callback) does not echo
    	# spin() simply keeps python from exiting until this node is stopped
    	rospy.spin()

if __name__ == '__main__':
    listener()
