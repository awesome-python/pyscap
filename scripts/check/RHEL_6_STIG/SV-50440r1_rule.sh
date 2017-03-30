#!/bin/bash

r=`which gconftool-2 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`gconftool-2 -g /apps/gnome-screensaver/mode 2>/dev/null | grep blank-only`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>Screensaver mode is not blank-only</message>'
	exit
fi

echo '<result>pass</result>'