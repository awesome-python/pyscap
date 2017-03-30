#!/bin/bash

e=`sysctl net.ipv4.icmp_echo_ignore_broadcasts | grep -P 'net.ipv4.icmp_echo_ignore_broadcasts\s*=\s*1$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv4.icmp_echo_ignore_broadcasts is not 1</message>'
	exit
fi

echo '<result>pass</result>'



