#!/bin/bash

r=`find /home -xdev -name .netrc 2>/dev/null`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>.netrc files on the system</message>'
	exit
fi

echo '<result>pass</result>'
