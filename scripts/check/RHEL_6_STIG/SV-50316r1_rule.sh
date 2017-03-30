#!/bin/bash

a=`grep -r sctp /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$a" == "x" ]]; then
	echo '<result>fail</result><message>sctp module is not disabled</message>'
else
	echo '<result>pass</result>'
fi
