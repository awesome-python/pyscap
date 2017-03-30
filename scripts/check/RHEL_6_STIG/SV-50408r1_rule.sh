#!/bin/bash

r=`egrep -i '^Protocol\s+2' /etc/ssh/sshd_config`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>Protocol is not set to 2 in sshd_config</message>'
else
	echo '<result>pass</result>'
fi
