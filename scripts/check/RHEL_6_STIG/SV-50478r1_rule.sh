#!/bin/bash

r=`mount | grep 'nfs on'`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`grep insecure_locks /etc/exports`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>insecure_locks allowed in nfs exports</message>'
	exit
fi

echo '<result>pass</result>'