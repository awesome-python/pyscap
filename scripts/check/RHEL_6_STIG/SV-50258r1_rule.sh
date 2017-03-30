#!/bin/bash

. lib/file.sh
e=`file_owner "/etc/group"`
if [[ "$e" != "root" ]]; then
	echo '<result>fail</result><message>owner is not root for /etc/group</message>'
	exit
fi

echo '<result>pass</result>'

