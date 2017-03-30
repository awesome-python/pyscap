#!/bin/bash

r=`grep -P 'pam_cracklib.*ucredit=-1' /etc/pam.d/system-auth 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_cracklib ucredit is not set to -1</message>'
	exit
fi

echo '<result>pass</result>'



