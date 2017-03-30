#!/bin/bash

for i in '/bin' '/usr/bin' '/usr/local/bin' '/sbin' '/usr/sbin' '/usr/local/sbin'
do
	r=`find -L "$i" -perm /022 2>/dev/null`
	if [[ "x$r" != "x" ]]; then
		echo "<result>fail</result><message>incorrect permissions on $r</message>"
		exit
	fi
done

echo '<result>pass</result>'

