#!/bin/bash

f=/etc/samba/smb.conf
. lib/file.sh
backup_file "$f" || exit 1

r=`egrep -i '^\s*client signing' $f`
if [[ "x$r" == "x" ]]; then
	cat $f | perl fix/insert_text.pl "\tclient signing = mandatory\n" after '^\[global\]' > $f.new
else
	sed 's/^\s*client signing\s\+=\s\+.*$/\tclient signing = mandatory/i' $f > $f.new
fi
#diff $f $f.new
mv -f $f.new $f
