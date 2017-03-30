#!/bin/bash

s=ntpdate

e=`chkconfig "$s" --list 2>/dev/null`
# service not installed
if [[ "x$e" == "x" ]]; then
	echo '<result>pass</result>'
	exit
fi

r=`chkconfig "$s" --list 2>/dev/null | grep on`
if [[ "x$r" != "x" ]]; then
	echo "<result>fail</result><message>service $s is enabled</message>"
	exit
fi

# ntpdate doesn't return a status for stopped
r=`service $s status`
if [[ "x$r" == "x" ]]; then
	echo '<result>pass</result>'
	exit
fi

r=`service $s status 2>/dev/null | grep stopped`
if [[ "x$r" == "x" ]]; then
	echo "<result>fail</result><message>service $s is not stopped</message>"
	exit
fi

echo '<result>pass</result>'