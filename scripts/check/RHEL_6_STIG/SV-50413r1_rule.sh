#!/bin/bash

r=`egrep -i '^HostbasedAuthentication\s+yes' /etc/ssh/sshd_config`

if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result>HostbasedAuthentication is not set to yes in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
