#!/bin/bash

r=`grep max_log_file /etc/audit/auditd.conf | grep 6`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>max_log_file is not set to 6 for auditd</message>'
else
	echo '<result>pass</result>'
fi

