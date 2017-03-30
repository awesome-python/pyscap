#!/bin/bash

r=`rpm -q aide | grep 'not installed'`
if [[ "x$r" != "x" ]]; then
	echo 'y' | yum install aide
fi

chkconfig aide on
service aide start
sleep 5s