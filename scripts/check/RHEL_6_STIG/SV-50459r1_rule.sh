#!/bin/bash

r=`grep remember /etc/pam.d/system-auth | grep 'remember=24'`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>System does not remember 24 passwords</message>'
	exit
fi

echo '<result>pass</result>'