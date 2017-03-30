#!/bin/bash

for i in '/bin' '/usr/bin' '/usr/local/bin' '/sbin' '/usr/sbin' '/usr/local/sbin'
do
	r=`find -L "$i" \! -user root 2>/dev/null`
	for file in $r; do
		echo "Changing owner of $file to root..."
		chown root $file
	done
done
