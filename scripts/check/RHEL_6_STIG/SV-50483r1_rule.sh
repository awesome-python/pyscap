#!/bin/bash

r=`egrep -r -i '^install\s+bluetooth\s+/bin/true' /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>Bluetooth kernel module not disabled</message>'
	exit
fi

r=`egrep -r -i '^install\s+net-pf-31\s+/bin/true' /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>Bluetooth kernel module not disabled</message>'
	exit
fi

echo '<result>pass</result>'