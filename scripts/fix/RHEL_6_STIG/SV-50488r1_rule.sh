#!/bin/bash

r=`rpm -q openswan | grep 'not installed'`
if [[ "x$r" != "x" ]]; then
	echo 'y' | yum install openswan
	if [[ "$?" != "0" ]]; then
		rpm --install fix/RHEL_6_STIG/openswan-2.6.32-27.el6.x86_64.rpm
	fi
fi

#chkconfig openswan on
#service openswan start
#sleep 5s