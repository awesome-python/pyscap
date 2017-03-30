#!/bin/bash

r=`mount | grep 'nfs on'`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`mount | grep 'nfs on' | grep nosuid`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>NFS mount without nosuid</message>'
	exit
fi

echo '<result>pass</result>'