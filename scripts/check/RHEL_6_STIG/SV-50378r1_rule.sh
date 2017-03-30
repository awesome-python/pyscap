#!/bin/bash

r=`grep -P '^\s*crypt_style\s*=\s*sha512' /etc/libuser.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>crypt_style is not set to sha512 in libuser.conf</message>'
	exit
fi

echo '<result>pass</result>'


