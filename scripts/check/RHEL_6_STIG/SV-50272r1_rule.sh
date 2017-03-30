#!/bin/bash

for i in '/bin' '/usr/bin' '/usr/local/bin' '/sbin' '/usr/sbin' '/usr/local/sbin'
do
	r=`find -L "$i" \! -user root 2>/dev/null`
	if [[ "x$r" != "x" ]]; then
		echo '<result>fail</result><message>system command files found that are not owned by root</message>'
		exit
	fi
done

echo '<result>pass</result>'

