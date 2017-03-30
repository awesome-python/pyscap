#!/bin/bash

# The DBMS must restrict access to system tables and other configuration information or metadata to DBAs or other authorized users.

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	for p in `mysql_query "SELECT 1 FROM mysql.tables_priv WHERE User NOT LIKE '$STIG_DATABASE_USERNAME%' AND Table_name LIKE 'mysql.%'"`; do
		if [[ "x$p" == "x1" ]]; then
			echo '<result>fail</result><message>Non-DBA user with table privileges</message>'
			exit
		fi
	done

	for p in `mysql_query "SELECT 1 FROM mysql.columns_priv WHERE User NOT LIKE '$STIG_DATABASE_USERNAME%' AND Table_name LIKE 'mysql.%'"`; do
		if [[ "x$p" == "x1" ]]; then
			echo '<result>fail</result><message>Non-DBA user with column privileges</message>'
			exit
		fi
	done

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi
