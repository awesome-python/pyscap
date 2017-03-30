#!/bin/bash

f=/etc/security/limits.conf
. lib/file.sh
backup_file $f || exit 1

r=`egrep '^\*\s+hard\s+core\s+10' $f 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	cp $f $f.new
	echo '* hard core 0' >> $f.new
else
	sed 's/^\*\s\+hard\s\+core\s\+.*$/* hard core 0/i' < $f > $f.new
fi
mv $f.new $f