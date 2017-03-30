#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	# max connections is not defined in config files
	get_mysql_option mysqld max_user_connections
	if [ -z "$result" ]; then
		fail 'max_user_connections is not defined in config files'
	fi

	pass
fi
