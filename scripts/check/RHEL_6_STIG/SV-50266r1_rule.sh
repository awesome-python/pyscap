#!/bin/bash

for i in '/lib' '/lib64' '/usr/lib' '/usr/lib64' '/lib/modules'
do
	r=`find -L "$i" \! -user root 2>/dev/null`
	if [[ "x$r" != "x" ]]; then
		echo "<result>fail</result><message>owner is not root for $r</message>"
		exit
	fi
done

echo '<result>pass</result>'

