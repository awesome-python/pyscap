#!/bin/bash

r=`mount 2>/dev/null | grep "on /var "`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>/var is not on different partition</message>'
else
	echo '<result>pass</result>'
fi
