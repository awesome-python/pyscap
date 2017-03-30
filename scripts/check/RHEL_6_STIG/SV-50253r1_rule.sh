#!/bin/bash

r=`rpm -Va 2>/dev/null | grep '^......G'`
if [[ "x$r" != "x" ]]; then
	echo "<result>fail</result><message>Group-owner of file does not match package: $r</message>"
	exit
fi

echo '<result>pass</result>'
