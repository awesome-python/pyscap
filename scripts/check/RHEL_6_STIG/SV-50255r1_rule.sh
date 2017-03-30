#!/bin/bash

r=`mount 2>/dev/null | grep "on /tmp "`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>/tmp is not a different partition</message>'
else
	echo '<result>pass</result>'
fi
