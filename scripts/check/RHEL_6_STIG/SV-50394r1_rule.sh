#!/bin/bash

e=`diff lib/DoD_banner.txt /etc/issue 2>/dev/null`
if [[ "x$e" != "x" ]]; then
	echo '<result>fail</result><message>/etc/issue does not match DoD banner</message>'
	exit
fi

echo '<result>pass</result>'
