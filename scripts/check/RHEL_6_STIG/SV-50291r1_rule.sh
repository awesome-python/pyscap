#!/bin/bash

r=`grep -r usb-storage /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>usb-storage is not disabled</message>'
	exit
fi

echo '<result>pass</result>'
