#!/bin/bash

e=`egrep 'gpgcheck\s*=\s*0' /etc/yum.repos.d/*.repo`
# check turned off
if [[ "x$e" != "x" ]]; then
	echo '<result>fail</result><message>gpgcheck turned off in yum.repos.d</message>'
else
	echo '<result>pass</result>'
fi

