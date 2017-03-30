#!/bin/bash

f=/etc/csh.cshrc
. lib/file.sh
backup_file $f || exit 1

r=`grep umask $f`
if [[ "x$r" == "x" ]]; then
	echo 'umask 077' >> $f
else
	sed 's/umask\s\+[0-9]\+/umask 077/' $f > $f.new
	mv -f $f.new $f
fi