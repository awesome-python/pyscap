#!/bin/bash

. lib/packages.sh

na_if_package_not_installed 'vsftpd'

if [ "$(ls -A /etc/xinetd.d)" ]; then
	xconf=`grep vsftpd /etc/xinetd.d/* 2>/dev/null`
	if [[ "x$xconf" == "x" ]]; then
		# started through xinetd
		conf=`grep server_args $xconf 2>/dev/null | awk '{print $3}'`
	else
		conf=/etc/vsftpd/vsftpd.conf
	fi
else
	conf=/etc/vsftpd/vsftpd.conf
fi

r=`grep -i 'xferlog_enable\s*=\s*yes' $conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>xferlog is not enabled in vsftpd</message>'
	exit
fi

echo '<result>pass</result>'
