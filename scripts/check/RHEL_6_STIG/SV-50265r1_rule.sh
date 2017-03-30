#!/bin/bash

for i in '/lib' '/lib64' '/usr/lib' '/usr/lib64' '/lib/modules'
do
	r=`find -L "$i" -perm /022 2>/dev/null`
	for f in $r; do
		if [[ -L $f ]]; then
			if [[ -e $f ]]; then # skip broken links
				echo "<result>fail</result><message>Invalid permissions on $f</message>"
				exit
			fi
		else
			echo "<result>fail</result><message>Invalid permissions on $f</message>"
			exit
		fi
	done
done

echo '<result>pass</result>'

