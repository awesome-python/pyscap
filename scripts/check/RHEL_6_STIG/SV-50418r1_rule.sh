#!/bin/bash

r=`egrep -i '^Ciphers\s+(aes128-ctr|aes192-ctr|aes256-ctr|aes128-cbc|3des-cbc|aes192-cbc|aes256-cbc|,)+$' /etc/ssh/sshd_config`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>non-FIPS-approved ciphers are in use</message>'
else
	echo '<result>pass</result>'
fi
