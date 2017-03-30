#!/bin/bash
. lib/db.sh
die_if_no_db
if [[ "x$STIG_DATABASE" = "xmysql" ]]; then
	. lib/mysql.sh
	. lib/file.sh

	f=/etc/my.cnf
	backup_file $f
	cat $f | perl fix/insert_text.pl '# STIG modification
local_infile = 0
' after '\[mysqld\]' > $f.new
	mv -f $f.new $f
	chmod 644 $f
	
	/etc/init.d/mysqld restart
fi
