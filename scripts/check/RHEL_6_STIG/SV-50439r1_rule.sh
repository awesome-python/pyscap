#!/bin/bash

r=`which gconftool-2 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`gconftool-2 -g /apps/gnome-screensaver/lock_enabled 2>/dev/null | grep true`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>Screensaver lock_enabled is not true</message>'
	exit
fi

echo '<result>pass</result>'