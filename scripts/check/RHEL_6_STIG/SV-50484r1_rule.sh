#!/bin/bash

r=`pwck -rq 2>/dev/null`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>Duplicate account names found</message>'
	exit
fi

echo '<result>pass</result>'