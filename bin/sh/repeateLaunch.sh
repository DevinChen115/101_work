#!/bin/sh

#echo "請輸入執行次數"
#read times

for i in {1..5}}
#for (( i=1; i<=$times; i++ ))
do
	echo $i
   adb shell am start -n conPage
   sleep 15
   adb shell am force-stop cod
   sleep 1
done

echo "關閉屏保, 裝新版本, 往後調 48 小時"