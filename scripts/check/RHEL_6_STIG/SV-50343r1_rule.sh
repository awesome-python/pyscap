#!/bin/bash

e=`sysctl net.ipv4.conf.all.rp_filter | grep -P 'net.ipv4.conf.all.rp_filter\s*=\s*1$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv4.conf.all.rp_filter is not 1</message>'
	exit
fi

echo '<result>pass</result>'

