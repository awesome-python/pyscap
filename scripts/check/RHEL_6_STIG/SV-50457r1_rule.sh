#!/bin/bash

r=`which smbclient 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`egrep -i '^\s*client signing\s+=\s+mandatory' /etc/samba/smb.conf`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>samba config does not require client signing</message>'
	exit
fi

echo '<result>pass</result>'