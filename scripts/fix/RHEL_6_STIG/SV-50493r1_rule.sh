#!/bin/bash

f=/etc/default/useradd
. lib/file.sh
backup_file "$f" || exit 1

r=`grep -i '^INACTIVE' $f`
if [[ "x$r" == "x" ]]; then
	echo 'INACTIVE=35' >> $f
else
	sed 's/^INACTIVE\s*=.*/INACTIVE=35/i' $f > $f.new
	mv -f $f.new $f
fi