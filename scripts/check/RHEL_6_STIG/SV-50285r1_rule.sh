#!/bin/bash

r=`egrep -i 'PrintLastLog\s+yes' /etc/ssh/sshd_config`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>PrintLastLog is not set to yes in sshd_config</message>'
	exit
fi

echo '<result>pass</result>'
