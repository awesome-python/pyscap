#!/bin/bash

r=`egrep -i "umask 02[2|7]" /etc/init.d/functions 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>umask in /etc/init.d/functions is not restrictive</message>'
	exit
fi

echo '<result>pass</result>'
