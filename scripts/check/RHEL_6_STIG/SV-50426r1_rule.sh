#!/bin/bash

r=`ls /lib{64,}/security/pam_ldap.so 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`grep start_tls /etc/pam_ldap.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>pam_ldap.conf is not configured with start_tls</message>'
	exit
fi
echo '<result>pass</result>'
