#!/bin/bash

r=`pwck -rq 2>/dev/null`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>Inconsistency in GIDs between /etc/passwd and /etc/group</message>'
	exit
fi

echo '<result>pass</result>'