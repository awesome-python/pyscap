#!/bin/bash

r=`rpm -V audit 2>/dev/null| grep '^.....U'`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>User-ownership of audit binaries and configuration files is incorrect</message>'
	exit
fi

echo '<result>pass</result>'