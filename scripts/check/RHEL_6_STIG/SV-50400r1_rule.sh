#!/bin/bash

. lib/packages.sh

na_if_package_not_installed 'vsftpd'

if [ "$(ls -A /etc/xinetd.d)" ]; then
	#echo xinetd being used
	xconf=`grep vsftpd /etc/xinetd.d/* 2>/dev/null`
	if [[ "x$xconf" == "x" ]]; then
		#echo started through xinetd
		conf=`grep server_args $xconf 2>/dev/null | awk '{print $3}'`
	else
		conf=/etc/vsftpd/vsftpd.conf
	fi
else
	conf=/etc/vsftpd/vsftpd.conf
fi
#echo test

r=`egrep -i 'banner_file\s*=\s*/etc/issue' $conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>vsftpd.conf does not use /etc/issue as a banner</message>'
	exit
fi

pass
