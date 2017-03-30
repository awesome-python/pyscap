#!/bin/bash

r=`grep -P '^\s*PASS_MIN_LEN\s+14' /etc/login.defs`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>PASS_MIN_LEN is not 14 in login.defs</message>'
	exit
fi

echo '<result>pass</result>'

