#!/bin/bash

e=`sysctl net.ipv4.conf.default.accept_source_route | grep -P 'net.ipv4.conf.default.accept_source_route\s*=\s*0$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv4.conf.default.accept_source_route is not 0</message>'
	exit
fi

echo '<result>pass</result>'
