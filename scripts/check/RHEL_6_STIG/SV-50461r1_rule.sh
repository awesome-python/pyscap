#!/bin/bash

. lib/packages.sh
na_if_package_not_installed 'net-snmp'

r=`egrep 'v1\|v2c\|com2sec' /etc/snmp/snmpd.conf 2>/dev/null | grep -v '^#'`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>net-snmp daemon allows insecure protocol versions</message>'
	exit
fi

echo '<result>pass</result>'
