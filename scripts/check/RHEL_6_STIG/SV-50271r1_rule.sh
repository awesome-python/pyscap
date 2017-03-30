#!/bin/bash

r=`egrep 'active\s+=\s+yes' /etc/audisp/plugins.d/syslog.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>syslog not activated in audisp</message>'
	exit
fi

echo '<result>pass</result>'