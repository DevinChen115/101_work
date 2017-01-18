#!/bin/sh

#read para
if [ -z $1 ];then
	#echo "Usage: sh selectLogcat.sh %AppName%"
	echo "we support CM, CMS, KBD"
	#echo "please input your choose:"
	read -p 'please input your choose: ' AppName
	#exit 1
else
	AppName=$1
fi

if [ $AppName == "CM" ];then
	adb shell pm clear c
elif [ $AppName == "CMS" ];then
	adb shell pm clear com.cleaurity
elif [ $AppName == "KBD" ];then
	adb shell pm clear com.ijintor_en
else
	echo -e "\nSorry!! we do not support "$AppName
fi

# adb shell am force-stop com.cleanmaster.security