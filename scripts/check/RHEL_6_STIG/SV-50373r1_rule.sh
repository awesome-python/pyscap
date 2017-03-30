#!/bin/bash

r=`grep -P 'pam_cracklib.*difok=4' /etc/pam.d/system-auth 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_cracklib difok is not set to 4</message>'
	exit
fi

echo '<result>pass</result>'


