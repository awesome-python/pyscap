#!/bin/bash

e=`ls -lL /etc/grub.conf | grep -- '-rw-------'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>Incorrect permissions on grub.conf</message>'
	exit
fi

echo '<result>pass</result>'

