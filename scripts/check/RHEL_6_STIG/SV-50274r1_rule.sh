#!/bin/bash

r=`which gconftool-2 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory --get /apps/gnome_settings_daemon/keybindings/screensaver 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>screensaver keybindings not present</message>'
	exit
fi

echo '<result>pass</result>'