# encoding: utf-8

import sys
import os

device = ""
if(sys.platform == "win32"):
    device = os.popen("adb devices | findstr -v List | findstr -v :")
elif(sys.platform == "win64"):
    device = os.popen("adb devices | findstr -v List | findstr -v :")
else:
    device = os.popen("adb devices | grep -v List | grep -v :")
    #device = subprocess.getoutput("adb devices | grep -v List | grep -v :")
deviceName = str(device.read()).strip()
#deviceName = #str(device).strip():q!
deviceName = deviceName.split("\tdevice")
devIp = os.popen("adb shell getprop dhcp.wlan0.ipaddress")
#print(deviceName[0])

print("現在的 device 有")
os.system("adb devices")
port = input("port : ")
os.system("adb tcpip " + port)
print("請把 usb 線拔除")
os.system("pause")
os.system("adb -s " + str(deviceName[0]) + " connect " + devIp.read() + ":" + port)




"""
List of devices attached
10.33.136.155:5555      device
G1AZFG005198XLB device
"""