#!/bin/bash

r=`egrep '^\s*PASS_MAX_DAYS\s+60' /etc/login.defs`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>PASS_MAX_DAYS is not 60 in login.defs</message>'
	exit
fi

echo '<result>pass</result>'

