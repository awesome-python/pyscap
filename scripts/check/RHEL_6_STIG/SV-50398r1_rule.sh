#!/bin/bash

e=`sysctl kernel.exec-shield | grep -P 'kernel\.exec-shield\s*=\s*1$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>kernel.exec-shield is not 1</message>'
	exit
fi

echo '<result>pass</result>'

