#!/bin/bash

f=/etc/vsftpd/vsftpd.conf
. lib/file.sh
backup_file $f || exit 1

r=`grep '^banner_file' $f`
if [[ "x$r" == "x" ]]; then
	echo "Appending banner_file setting..."
	echo "banner_file=/etc/issue" >> $f
else
	echo "Modifying banner_file setting..."
	cat $f | sed 's/^banner_file.*$/banner_file=\/etc\/issue/i' > $f.new
	mv -f $f.new $f
fi
