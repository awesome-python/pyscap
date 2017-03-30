#!/bin/bash

r=`egrep '^\*\s+hard\s+core\s+0' /etc/security/limits.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>hard core is not set to 0 in limits.conf</message>'
	exit
fi

echo '<result>pass</result>'