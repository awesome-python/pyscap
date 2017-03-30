#!/bin/bash

r=`grep -P '^\s*ENCRYPT_METHOD\s+SHA512' /etc/login.defs`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>ENCRYPT_METHOD is not set to SHA512 in login.defs</message>'
	exit
fi

echo '<result>pass</result>'

