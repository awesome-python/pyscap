#!/bin/bash

. lib/packages.sh

na_if_package_not_installed 'xorg-x11-server-common'

r=`grep -i '^id:3:initdefault:' /etc/inittab`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>system does not start up at init level 3</message>'
	exit
fi

echo '<result>pass</result>'