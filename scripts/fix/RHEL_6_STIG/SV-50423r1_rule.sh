#!bin/bash

f=/etc/postfix/main.cf
. lib/file.sh
backup_file $f || exit 1

r=`grep '^inet_interfaces' $f`
if [[ "x$r" == "x" ]]; then
	echo 'inet_interfaces = localhost' >> $f
else
	sed 's/^inet_interfaces\s*=\s*.*$/inet_interfaces = localhost/i' $f > $f.new
	mv -f $f.new $f
fi

