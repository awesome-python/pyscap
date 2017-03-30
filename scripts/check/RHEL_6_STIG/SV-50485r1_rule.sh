#!/bin/bash

r=`egrep '^\*\s+hard\s+maxlogins\s+10' /etc/security/limits.conf 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>maxlogins is not 10 in limits.conf</message>'
	exit
fi

echo '<result>pass</result>'