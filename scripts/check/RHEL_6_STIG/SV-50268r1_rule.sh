#!/bin/bash

r=`egrep -i 'disk_full_action\s*=\s*(syslog|exec|single|halt)' /etc/audit/auditd.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>disk_full_action is not syslog/exec/single/halt in auditd.conf</message>'
	exit
fi

echo '<result>pass</result>'