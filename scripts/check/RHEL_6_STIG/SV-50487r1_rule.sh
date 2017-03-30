#!/bin/bash

r=`egrep "^:FORWARD\s+DROP" /etc/sysconfig/iptables 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>iptables does not have DROP as a policy default for the FORWARD chain</message>'
	exit
fi

echo '<result>pass</result>'