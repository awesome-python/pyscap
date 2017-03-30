#!/bin/bash

r=`mount 2>/dev/null | grep "on /var/log/audit "`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>/var/log/audit is not a separate partition</message>'
else
	echo '<result>pass</result>'
fi
