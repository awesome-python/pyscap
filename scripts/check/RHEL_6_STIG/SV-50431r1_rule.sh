#!/bin/bash

r=`which gconftool-2 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`gconftool-2 -g /apps/gnome-screensaver/idle_activation_enabled 2>/dev/null | grep true`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>screensaver idle activation is not enabled</message>'
	exit
fi

echo '<result>pass</result>'