#!/bin/bash

r=`egrep -i '^PermitRootLogin\s+no' /etc/ssh/sshd_config`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>PermitRootLogin is not set to no in sshd_config</message>'
	exit
fi

r=`egrep -i '^PermitRootLogin\s+yes' /etc/ssh/sshd_config`
if [[ "x$r" != "x" ]]; then
        echo '<result>fail</result><message>PermitRootLogin is set to yes in sshd_config</message>'
	exit
fi

echo '<result>pass</result>'
