#!/bin/bash

r=`rpm -q ntpd | grep 'not installed'`
if [[ "x$r" != "x" ]]; then
	echo 'y' | yum install ntpd
	if [[ "$?" != "0" ]]; then
		rpm --install fix/RHEL_6_STIG/ntp-4.2.6p5-1.el6.centos.x86_64.rpm
	fi
fi

chkconfig ntpd on
service ntpd start
