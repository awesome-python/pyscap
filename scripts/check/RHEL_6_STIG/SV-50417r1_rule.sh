#!/bin/bash

r=`egrep -i '^PermitUserEnvironment\s+no' /etc/ssh/sshd_config`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>PermitUserEnvironment is not set to no in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
