#!/bin/bash
e=`sysctl 'net.ipv6.conf.default.accept_redirects' |& grep 'unknown key'`
#echo $e
if [[ "x$e" != "x" ]]; then
	# pass because the ipv6 module must be unloaded
	echo '<result>pass</result>'
	exit
fi

r=`sysctl net.ipv6.conf.default.accept_redirects 2>/dev/null | grep -P 'net.ipv6.conf.default.accept_redirects\s*=\s*0'`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>net.ipv6.conf.default.accept_redirects is not 0</message>'
	exit
fi

echo '<result>pass</result>'
