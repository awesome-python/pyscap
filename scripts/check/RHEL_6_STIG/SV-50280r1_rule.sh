#!/bin/bash

r=`grep -P '^\s*PASS_WARN_AGE\s+7' /etc/login.defs`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>PASS_WARN_AGE is not 7 in login.defs</message>'
	exit
fi

echo '<result>pass</result>'

