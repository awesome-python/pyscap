#!/bin/bash

r=`mount 2>/dev/null | grep "on /var/log "`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>/var/log is not on a separate partition</message>'
else
	echo '<result>pass</result>'
fi
