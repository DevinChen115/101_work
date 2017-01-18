#!/bin/sh

if [ -z $1 ];then
	echo "usage: changeHost test OR changeHost origin"
	exit 1
fi

if [ $1 == "test" ];then
	echo "become test host"
	a=`sudo cp /private/etc/hosts~test /private/etc/hosts`
fi

if [ $1 == "origin" ];then
	echo "become origin host"
	a=`sudo cp /private/etc/hosts~orig /private/etc/hosts`
fi