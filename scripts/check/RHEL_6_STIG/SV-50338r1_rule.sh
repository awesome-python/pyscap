#!/bin/bash

e=`sysctl net.ipv4.icmp_ignore_bogus_error_responses | grep -P 'net.ipv4.icmp_ignore_bogus_error_responses\s*=\s*1$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv4.icmp_ignore_bogus_error_responses is not 1</message>'
	exit
fi

echo '<result>pass</result>'
