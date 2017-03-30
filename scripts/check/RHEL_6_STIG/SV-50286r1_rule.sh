#!/bin/bash

if [ -e /etc/hushlogins ]; then
	echo '<result>fail</result><message>/etc/hustlogins exists</message>'
	exit
fi

for i in `cut -d: -f1 /etc/passwd`; do
	# have to eval to expand tilde
	file=`eval echo "~$i/.hushlogin"`
	if [ -e "$file" ]; then
		echo "<result>fail</result><message>~/.hushlogin exists for user $i</message>"
		exit
	fi
done

echo '<result>pass</result>'