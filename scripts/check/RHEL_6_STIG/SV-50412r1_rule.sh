#!/bin/bash

r=`egrep -i '^IgnoreRhosts\s+no' /etc/ssh/sshd_config`

if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>IgnoreRhosts is not set to no in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
