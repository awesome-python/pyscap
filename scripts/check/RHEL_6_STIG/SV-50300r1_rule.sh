#!/bin/bash

e=`awk -F: '($2 != "x") {print}' /etc/passwd`
if [[ "x$e" != "x" ]]; then
	echo '<result>fail</result><message>non-shadowed password in /etc/passwd</message>'
	exit
fi

echo '<result>pass</result>'

