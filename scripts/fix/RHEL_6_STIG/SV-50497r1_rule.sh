#!/bin/bash

. lib/file.sh
backup_file /etc/crontab || exit 1

r=`rpm -q aide | grep 'not installed'`
if [[ "x$r" != "x" ]]; then
	echo 'y' | yum install aide
	if [[ "$?" != "0" ]]; then
		rpm --install fix/RHEL_6_STIG/ntp-4.2.6p5-1.el6.centos.x86_64.rpm
	fi
fi

echo '05 4 * * * root /usr/sbin/aide --check' >> /etc/crontab
