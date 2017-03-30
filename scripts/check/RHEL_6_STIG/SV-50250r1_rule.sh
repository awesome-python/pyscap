#!/bin/bash

. lib/file.sh
e=`file_owner "/etc/passwd"`
if [[ "$e" != "root" ]]; then
	echo '<result>fail</result><message>owner of /etc/passwd is not root</message>'
	exit
fi

echo '<result>pass</result>'

