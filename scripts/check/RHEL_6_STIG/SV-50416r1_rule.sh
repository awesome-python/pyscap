#!/bin/bash

r=`egrep -i '^Banner\s+/etc/issue' /etc/ssh/sshd_config`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>Banner is not set to /etc/issue in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
