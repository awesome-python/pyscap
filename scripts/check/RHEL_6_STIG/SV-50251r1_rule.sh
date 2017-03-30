#!/bin/bash

. lib/file.sh
e=`file_groupowner "/etc/passwd"`
if [[ "$e" != "root" ]]; then
	echo '<result>fail</result><message>Group-owner of /etc/passwd is not root</message>'
	exit
fi

echo '<result>pass</result>'

