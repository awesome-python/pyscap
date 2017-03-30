#!/bin/bash

e=`grep -r -P 'ipv6\s+disable\s*=\s*1' /etc/modprobe.conf /etc/modprobe.d 2>/dev/null`
if [[ "x$e" != "x" ]]; then
        # ipv6 is disabled
        echo '<result>notapplicable</result>'
        exit
fi

if [[ ! -f /etc/sysconfig/ip6tables ]]; then
	echo '<result>fail</result><message>/etc/sysconfig/ip6tables does not exist</message>'
	exit
fi

r=`egrep ":INPUT\s+DROP" /etc/sysconfig/ip6tables`
if [[ "x$r" == "x" ]]; then
	echo "<result>fail</result><message>Default policy for INPUT chain is not DROP</message>"
	exit
fi

echo '<result>pass</result>'
