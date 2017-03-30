#!/bin/bash

e=`grep -P '^\s*password' /etc/grub.conf`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>password is not set in grub.conf</message>'
	exit
fi

echo '<result>pass</result>'


