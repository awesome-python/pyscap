#!/bin/bash

. lib/file.sh
e=`file_groupowner "/etc/gshadow"`
if [[ "$e" != "root" ]]; then
	echo '<result>fail</result><message>group-owner of /etc/gshadow is not root</message>'
	exit
fi

echo '<result>pass</result>'

