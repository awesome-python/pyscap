#!/bin/bash

. lib/file.sh
e=`file_groupowner "/etc/group"`
if [[ "$e" != "root" ]]; then
	echo '<result>fail</result><message>group-owner of /etc/group is not root</message>'
	exit
fi

echo '<result>pass</result>'

