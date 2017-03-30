#!/bin/bash

e=`grep -r -P 'ipv6\s+disable\s*=\s*1' /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$e" == "x" ]]; then
	# ipv6 is enabled
	echo '<result>fail</result><message>ipv6 is not disabled</message>'
	exit
fi

echo '<result>pass</result>'


