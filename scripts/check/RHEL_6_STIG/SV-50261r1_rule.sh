#!/bin/bash

e=`ls -l /etc/group | grep -- '-rw-r--r--'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>Permissions incorrect on /etc/group</message>'
	exit
fi

echo '<result>pass</result>'

