#!/bin/sh

#read para
if [ -z $1 ];then
	echo "Usage: sh pg.sh 1"
	echo "1: 清除貼紙"
	exit 1
fi

if [ $1 == 1 ];then
	echo "開貼紙"
	adb shell rm -rf /sdcard/Photo Grid/ /sdcard/roidapp/
	echo "清除成功"
fi

