#!/bin/bash

e=`grep -r -P 'ipv6\s+disable\s*=\s*1' /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$e" == "x" ]]; then
	# ipv6 is enabled
	a=`service ip6tables status 2>/dev/null | grep 'not running'`
	if [[ "x$a" == "x" ]]; then
		echo '<result>pass</result>'
	else
		echo '<result>fail</result><message>ipv6 not disabled and ip6tables service not running</message>'
	fi
else
	echo '<result>notapplicable</result>'
fi
