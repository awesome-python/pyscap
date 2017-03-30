#!/bin/bash

e=`ls -l /etc/passwd | grep -- '-rw-r--r--'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>Incorrect permissions on /etc/passwd</message>'
	exit
fi

echo '<result>pass</result>'

