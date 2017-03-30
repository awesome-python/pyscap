#!/bin/bash

e=`awk -F: '($3 == "0") {print}' /etc/passwd | grep -v ^root`
if [[ "x$e" != "x" ]]; then
	echo "<result>fail</result><message>non-root account with user id 0</message>"
	exit
fi

echo '<result>pass</result>'

