#!/bin/bash

e=`updatedb 2>/dev/null; locate \.rhosts 2>/dev/null`
if [[ "x$e" != "x" ]]; then
	echo '<result>fail</result><message>.rhosts file found</message>'
	exit
fi

if [[ -f /etc/hosts.equiv ]]; then
	echo '<result>fail</result><message>/etc/hosts.equiv exists</message>'
else
	echo '<result>pass</result>'
fi

