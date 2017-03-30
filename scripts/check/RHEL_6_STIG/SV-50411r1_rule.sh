#!/bin/bash

r=`egrep -i '^ClientAliveCountMax\s+0' /etc/ssh/sshd_config`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>ClientAliveCountMax is not set to 0 in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
