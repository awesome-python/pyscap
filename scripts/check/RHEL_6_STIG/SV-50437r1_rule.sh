#!/bin/bash

r=`grep num_logs /etc/audit/auditd.conf | grep 5`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>auditd.conf num_logs is not 5</message>'
else
	echo '<result>pass</result>'
fi
