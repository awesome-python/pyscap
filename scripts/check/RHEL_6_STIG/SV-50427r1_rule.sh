#!/bin/bash

r=`ls /lib{64,}/security/pam_ldap.so 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`grep cert /etc/pam_ldap.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_ldap.conf is not configured with a certificate</message>'
	exit
fi
echo '<result>pass</result>'
