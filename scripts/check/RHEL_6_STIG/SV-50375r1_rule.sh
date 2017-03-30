#!/bin/bash

r=`grep -P 'pam_unix.*sha512' /etc/pam.d/system-auth 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_unix module is not using sha512 in system-auth</message>'
	exit
fi

echo '<result>pass</result>'


