#!/bin/bash

r=`grep -P 'pam_cracklib.*dcredit=-1' /etc/pam.d/system-auth 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_cracklib dcredit is not -1</message>'
	exit
fi

echo '<result>pass</result>'


