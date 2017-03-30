#!/bin/bash

e=`grep -P '^PROMPT\s*=\s*no' /etc/sysconfig/init`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>PROMPT is not turned off in /etc/sysconfig/init</message>'
	exit
fi

echo '<result>pass</result>'



