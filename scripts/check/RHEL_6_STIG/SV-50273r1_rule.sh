#!/bin/bash

r=`mount 2>/dev/null | grep "on /home "`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>/home is not a separate partition</message>'
else
	echo '<result>pass</result>'
fi
