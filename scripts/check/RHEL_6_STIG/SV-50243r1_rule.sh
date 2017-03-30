#!/bin/bash

. lib/file.sh
e=`file_owner "/etc/gshadow"`
if [[ "$e" != "root" ]]; then
	echo '<result>fail</result><message>file owner of /etc/gshadow is not root</message>'
	exit
fi

echo '<result>pass</result>'

