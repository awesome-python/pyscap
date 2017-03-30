#!/bin/bash

e=`grep nullok /etc/pam.d/system-auth /etc/pam.d/system-auth-ac`
if [[ "x$e" != "x" ]]; then
	echo '<result>fail</result><message>nullok is listed in system-auth or system-auth-ac</message>'
	exit
fi

echo '<result>pass</result>'

