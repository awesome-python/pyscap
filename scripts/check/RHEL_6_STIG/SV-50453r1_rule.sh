#!/bin/bash

r=`mount | grep 'nfs on'`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`mount | grep 'nfs on' | grep nodev`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>NFS mount without nodev</message>'
	exit
fi

echo '<result>pass</result>'