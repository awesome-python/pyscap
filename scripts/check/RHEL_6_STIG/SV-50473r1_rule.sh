#!/bin/bash

e=`chkconfig "netconsole" --list 2>/dev/null`
# service not installed
if [[ "x$e" == "x" ]]; then
	echo '<result>pass</result>'
	exit
fi

r=`chkconfig "netconsole" --list 2>/dev/null | grep ':on'`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>netconsole service is enabled</message>'
	exit
fi

r=`service netconsole status 2>/dev/null | grep 'module not loaded'`
if [[ "x$r" != "x" ]]; then
	echo '<result>pass</result>'
	exit
fi

r=`service netconsole status 2>/dev/null | grep stopped`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>netconsole service is not stopped</message>'
	exit
fi

echo '<result>pass</result>'