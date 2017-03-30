#!/bin/bash

r=`grep -P 'pam_cracklib.*lcredit=-1' /etc/pam.d/system-auth 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_cracklib lcredit is not set to -1</message>'
	exit
fi

echo '<result>pass</result>'

