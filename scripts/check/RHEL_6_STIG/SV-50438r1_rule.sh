#!/bin/bash

r=`rpm -V audit 2>/dev/null | grep '$1 ~ /..5/ && $2 != "c"'`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>Audit executables with erroneous hashes</message>'
	exit
fi

echo '<result>pass</result>'