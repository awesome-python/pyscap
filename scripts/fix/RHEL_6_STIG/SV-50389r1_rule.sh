#!/bin/bash

f=/etc/sysconfig/init
. lib/file.sh
backup_file "$f" || exit 1

r=`grep -i '^PROMPT' $f`
if [[ "x$r" == "x" ]]; then
	echo 'PROMPT=no' >> $f
else
	sed 's/^PROMPT\s*=\s*.*/PROMPT=no/i' $f > $f.new
	mv -f $f.new $f
fi