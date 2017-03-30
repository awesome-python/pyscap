#!/bin/bash

r=`egrep -i '^PermitEmptyPasswords\s+yes' /etc/ssh/sshd_config`

if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>PermitEmptyPasswords is not set to yes in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
