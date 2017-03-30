#!/bin/bash

r=`grep pam_faillock /etc/pam.d/system-auth-ac | grep "fail_interval=900"`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message> pam_faillock fail_interval is not 900</message>'
	exit
fi

echo '<result>pass</result>'
