#!/bin/bash

r=`egrep 'action_mail_acct\s*=\s*root' /etc/audit/auditd.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>action_mail_acct is not set to root for auditd</message>'
	exit
fi

echo '<result>pass</result>'