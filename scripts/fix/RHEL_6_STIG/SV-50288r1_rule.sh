#!/bin/bash

files=`egrep 'gpgcheck\s*=\s*0' /etc/yum.repos.d/*.repo | cut -d: -f 1`
for file in $files; do
	. lib/file.sh
backup_file $file || exit 1
	sed 's/^gpgcheck\s*=.*$/gpgcheck=1/' $file > $file.new
	mv -f $file.new $file
	#diff $file.new $file
	#rm -f $file.new
done
