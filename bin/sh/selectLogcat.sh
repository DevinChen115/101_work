#!/bin/sh

#read para
if [ -z $1 ];then
	echo "Usage: sh selectLogcat.sh 1"
	
	exit 1
fi

if [ $1 == 1 ];then
	echo -e "\nPromot引導引導\n"
	adb logcat -v time | grep --color -E "PromotionSplaialog"
fi

if