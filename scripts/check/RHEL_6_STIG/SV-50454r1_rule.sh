#!/bin/bash

. lib/packages.sh

na_if_package_not_installed 'net-snmp'

r=`grep -v "^#" /etc/snmp/snmpd.conf | grep public`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>SNMP daemon allows public community</message>'
	exit
fi

echo '<result>pass</result>'
