#!/bin/bash

r=`grep -P 'pam_faillock.*deny=3' /etc/pam.d/system-auth-ac 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_faillock deny is not set to 3</message>'
	exit
fi

echo '<result>pass</result>'



