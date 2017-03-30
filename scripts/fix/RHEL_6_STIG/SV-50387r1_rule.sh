#!/bin/bash

f=/etc/sysconfig/init
. lib/file.sh
backup_file "$f" || exit 1

r=`grep -i '^SINGLE' $f`
if [[ "x$r" == "x" ]]; then
	echo 'SINGLE=/sbin/sulogin' >> $f
else
	sed 's|^SINGLE\s*=\s*.*|SINGLE=/sbin/sulogin|i' $f > $f.new
	mv -f $f.new $f
fi