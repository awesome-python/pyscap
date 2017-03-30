#!/bin/bash

r=`find / -xdev -type f -perm -002 2>/dev/null`
if [[ "x$r" != "x" ]]; then
	echo "<result>fail</result><message>World writable files found: $r</message>"
	exit
fi

echo '<result>pass</result>'
