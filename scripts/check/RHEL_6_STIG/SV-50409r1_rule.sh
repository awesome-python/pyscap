#!/bin/bash

r=`egrep -i '^ClientAliveInterval\s+900' /etc/ssh/sshd_config`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>ClientAliveInterval is not set to 900 in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
