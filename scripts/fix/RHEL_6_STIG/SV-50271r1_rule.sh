#!/bin/bash

f=/etc/audisp/plugins.d/syslog.conf
. lib/file.sh
backup_file "$f" || exit 1

r=`grep -i '^active' $f`
if [[ "x$r" == "x" ]]; then
	echo 'active = yes' >> $f
else
	sed 's/^active\s*=\s*.*/active = yes/i' $f > $f.new
	mv -f $f.new $f
fi

service auditd restart