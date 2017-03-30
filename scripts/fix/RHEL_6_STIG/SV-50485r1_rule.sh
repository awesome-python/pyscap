#!/bin/bash

f=/etc/security/limits.conf
. lib/file.sh
backup_file $f || exit 1

r=`egrep '^\*\s+hard\s+maxlogins\s+10' $f 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	cp $f $f.new
	echo '* hard maxlogins 10' >> $f.new
else
	sed 's/^\*\s\+hard\s\+maxlogins\s\+[0-9]\+.*$/* hard maxlogins 10/i' < $f > $f.new
fi
mv $f.new $f