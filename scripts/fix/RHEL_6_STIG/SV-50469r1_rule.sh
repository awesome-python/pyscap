#!/bin/bash

for f in `grep -l control-alt-delete /etc/init/* 2>/dev/null`; do
	. lib/file.sh
	backup_file $f || exit 1

	sed 's|^exec /sbin/shutdown.*Control-Alt-Delete.*$|exec /usr/bin/logger -p security.info "Ctrl-Alt-Delete pressed"|i' $f > $f.new
	mv -f $f.new $f
done
