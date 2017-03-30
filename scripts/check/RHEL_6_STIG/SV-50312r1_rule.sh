#!/bin/bash

e=`sysctl net.ipv4.ip_forward | grep -P 'net.ipv4.ip_forward\s*=\s*0$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv4.ip_forward is not 0</message>'
	exit
fi

echo '<result>pass</result>'
