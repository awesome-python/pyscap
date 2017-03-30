#!/bin/bash

r=`grep max_log_file_action /etc/audit/auditd.conf | grep rotate`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>max_log_file_action for auditd is not set to rotate</message>'
else
	echo '<result>pass</result>'
fi


