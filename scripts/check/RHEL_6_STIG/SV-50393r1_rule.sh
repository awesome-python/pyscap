#!/bin/bash

r=`grep pam_faillock /etc/pam.d/system-auth-ac | grep "unlock_time=604800"`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_faillock is not set in system-auth-ac</message>'
	exit
fi

echo '<result>pass</result>'
