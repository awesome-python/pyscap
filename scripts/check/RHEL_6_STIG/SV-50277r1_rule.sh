#!/bin/bash

r=`grep -P '^\s*PASS_MIN_DAYS\s+1' /etc/login.defs`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>PASS_MIN_DAYS is not 1 in login.defs</message>'
	exit
fi

echo '<result>pass</result>'

