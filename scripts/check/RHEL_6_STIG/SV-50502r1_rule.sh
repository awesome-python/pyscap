#!/bin/bash

. lib/packages.sh

na_if_package_not_installed 'tftp-server'

r=`egrep "server_args\s*=\s*.*-s /var/lib/tftpboot" /etc/xinetd.d/tftp`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>tftp server config is missing -s flag</message>'
	exit
fi

echo '<result>pass</result>'
