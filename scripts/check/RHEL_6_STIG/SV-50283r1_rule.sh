#!/bin/bash

e=`egrep 'gpgcheck\s*=\s*1' /etc/yum.conf`
# check turned on
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>gpgcheck is not turned on in yum.conf</message>'
	exit
fi

echo '<result>pass</result>'