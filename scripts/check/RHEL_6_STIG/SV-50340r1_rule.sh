#!/bin/bash

e=`sysctl net.ipv4.tcp_syncookies | grep -P 'net.ipv4.tcp_syncookies\s*=\s*1$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv4.tcp_syncookies is not 1</message>'
	exit
fi

echo '<result>pass</result>'
