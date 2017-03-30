#!/bin/bash

. lib/file.sh
e=`file_mode /etc/shadow`
if [[ "$e" != "0000" ]]; then
	echo "<result>fail</result><message>mode of /etc/shadow is $e, not 0000</message>"
	exit
fi

echo '<result>pass</result>'

