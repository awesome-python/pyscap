#!/bin/bash

e=`egrep '^ttyS[0-9]' /etc/securetty`
if [[ "x$e" != "x" ]]; then
	echo '<result>fail</result><message>ttyS is listed in /etc/securetty</message>'
	exit
fi

echo '<result>pass</result>'

