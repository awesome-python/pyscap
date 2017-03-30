#!/bin/bash

r=`which gconftool-2 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`gconftool-2 -g /apps/gdm/simple-greeter/banner_message_text 2>/dev/null | diff - lib/DoD_banner.txt`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>gdm banner different than DoD banner</message>'
	exit
fi

echo '<result>pass</result>'