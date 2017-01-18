#!/bin/sh

#read apk
if [ -z $1 ];then
	echo "Usage: sh installMoreDevice.sh APKFILE"
	exit 1
fi

Device=`adb devices | grep -v " device" | awk '$2=="device" { printf $1" " }'`;
#Device=`adb devices | grep -v " device" | grep device`;
echo $Device

IFS=' ' read -r -a ADDR <<< $Device
for i in "${ADDR[@]}"; do
	adb -s $i install -r -d $1
done
