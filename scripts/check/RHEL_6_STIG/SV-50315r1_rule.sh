#!/bin/bash

a=`grep -r dccp /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$a" == "x" ]]; then
	echo '<result>fail</result><message>dccp module is not disabled</message>'
else
	echo '<result>pass</result>'
fi
