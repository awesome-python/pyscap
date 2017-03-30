#!/bin/bash

. lib/general.sh

r=`which gconftool-2 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	notapplicable "gconftool-2 is not in the path"
fi

r=`which gdm 2>/dev/null`
if [[ "x$r" == "x" ]]; then
        notapplicable "gdm is not in the path"
fi

r=`gconftool-2 -g /apps/gdm/simple-greeter/banner_message_enable 2>/dev/null | grep true`
if [[ "x$r" == "x" ]]; then
	fail "gdm banner is not enabled"
fi

pass

