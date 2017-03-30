#!/bin/bash

rm -f /etc/hushlogins

for i in `cut -d: -f1 /etc/passwd`; do
	# have to eval to expand tilde
	file=`eval echo "~$i/.hushlogin"`
	rm -f $file
done