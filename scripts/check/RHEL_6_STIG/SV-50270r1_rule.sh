#!/bin/bash

r=`egrep -i 'space_left_action\s*=\s*email' /etc/audit/auditd.conf`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>space_left_action for auditd is not email</message>'
else
	echo '<result>pass</result>'
fi
