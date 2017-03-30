#!/bin/bash

r=`rpm -V audit 2>/dev/null| grep '^......G'`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>Group-ownership of audit binaries and configuration files is incorrect</message>'
	exit
fi

echo '<result>pass</result>'