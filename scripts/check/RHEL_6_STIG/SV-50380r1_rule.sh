#!/bin/bash

. lib/file.sh
e=`file_owner "/etc/grub.conf"`
if [[ "$e" != "root" ]]; then
	echo '<result>fail</result><message>file owner of grub.conf is not root</message>'
	exit
fi

echo '<result>pass</result>'

