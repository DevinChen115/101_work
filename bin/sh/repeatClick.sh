#!/bin/sh

for i in {1..101}

do
	echo $i
   adb shell input keyevent 26
   sleep 1
   adb shell input swipe 620 228 620 1440
   sleep 5
   adb shell input swipe 168 1157 920 1157
   sleep 1
   adb shell input keyevent 26
   sleep 1
   #adb shell input tap 90 1250
   #sleep 1
   #adb shell input tap 260 1250
   #sleep 1
   #adb shell input tap 420 1250
   #sleep 1
   #adb shell input tap 630 1250
   #sleep 1
done
