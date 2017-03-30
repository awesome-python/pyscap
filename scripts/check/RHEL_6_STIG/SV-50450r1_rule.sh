#!/bin/bash

r=`grep -i "umask 077" /etc/csh.cshrc 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>umask not set to 077 in csh.cshrc</message>'
	exit
fi

echo '<result>pass</result>'
