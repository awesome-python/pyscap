#!/bin/bash

r=`rpm -Va 2>/dev/null | grep '$1 ~ /..5/ && $2 != "c"'`
if [[ "x$r" != "x" ]]; then
	echo "<result>fail</result><message>File hash is different from rpm: $r</message>"
	exit
fi

echo '<result>pass</result>'
