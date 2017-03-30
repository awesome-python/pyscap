#!/bin/bash

r=`grep "INACTIVE=35" /etc/default/useradd`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>INACTIVE is not 35 in /etc/default/useradd</message>'
	exit
fi

echo '<result>pass</result>'
