#!/bin/bash

e=`grep -P '^SINGLE\s*=\s*/sbin/sulogin' /etc/sysconfig/init`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>SINGLE is not set to sulogin in /etc/sysconfig/init</message>'
	exit
fi

echo '<result>pass</result>'


