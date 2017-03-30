#!/bin/bash
# Unused database components, DBMS software, and database objects must be removed.

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	r=`mysql_query 'SHOW DATABASES;' | grep test`
	if [[ -z "$r" ]]; then
		echo '<result>pass</result>'
		exit
	fi

	echo '<result>fail</result><message>test database found</message>'
else
	echo '<result>notchecked</result>'
fi
