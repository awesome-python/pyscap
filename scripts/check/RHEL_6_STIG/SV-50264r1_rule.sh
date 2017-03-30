#!/bin/bash

r=`egrep 'disk_error_action\s+=\s+(syslog|exec|single|halt)' /etc/audit/auditd.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>disk_error_action is not syslog/exec/single/halt in auditd.conf</message>'
	exit
fi

echo '<result>pass</result>'