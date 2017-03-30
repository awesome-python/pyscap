#!/bin/bash

e=`egrep '^vc/[0-9]+' /etc/securetty`
if [[ "x$e" != "x" ]]; then
	echo '<result>fail</result><message>vc listed in /etc/securetty</message>'
	exit
fi

echo '<result>pass</result>'

