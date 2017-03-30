#!/bin/bash

. lib/file.sh
e=`file_groupowner "/etc/shadow"`
if [[ "$e" != "root" ]]; then
	echo "<result>fail</result><message>group-owner of /etc/shadow is $e, not root</message>"
	exit
fi

echo '<result>pass</result>'

