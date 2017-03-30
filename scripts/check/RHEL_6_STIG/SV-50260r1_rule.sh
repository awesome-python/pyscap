#!/bin/bash

r=`grep all_squash /etc/exports 2>/dev/null`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>all_squash found in /etc/exports</message>'
	exit
fi

echo '<result>pass</result>'