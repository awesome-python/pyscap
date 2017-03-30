#!/bin/bash

r=`grep "umask 077" /etc/profile 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>umask not set to 077 in /etc/profile</message>'
	exit
fi

echo '<result>pass</result>'
