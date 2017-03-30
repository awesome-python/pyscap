#!/bin/bash

r=`grep pam_cracklib /etc/pam.d/system-auth | grep maxrepeat=3`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_cracklib maxrepeat is not set to 3 in system-auth</message>'
	exit
fi

echo '<result>pass</result>'