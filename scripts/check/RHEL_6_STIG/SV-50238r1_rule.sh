#!/bin/bash

r=`egrep "^\s*kernel .* audit=1" /etc/grub.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>auditing is not enabled at boot</message>'
	exit
fi

echo '<result>pass</result>'