#!/bin/bash

. lib/file.sh
e=`file_mode /etc/gshadow`
if [[ "$e" != "0000" ]]; then
	echo '<result>fail</result><message>Mode of /etc/gshadow is not 0000</message>'
	exit
fi

echo '<result>pass</result>'

