#!/bin/bash

r=`grep aide /etc/crontab`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>aide is not listed in crontab</message>'
	exit
fi

echo '<result>pass</result>'