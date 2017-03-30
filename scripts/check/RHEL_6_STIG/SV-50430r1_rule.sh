#!/bin/bash

r=`which gconftool-2 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`gconftool-2 -g /apps/gnome-screensaver/idle_delay 2>/dev/null | grep 15`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>screensaver idle delay is not set to 15</message>'
	exit
fi

echo '<result>pass</result>'
