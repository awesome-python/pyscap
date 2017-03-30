#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	r=`mysql_query "SELECT CONCAT(TABLE_SCHEMA, '.', TABLE_NAME), engine FROM information_schema.tables WHERE TABLE_SCHEMA != 'mysql' AND TABLE_SCHEMA != 'information_schema' AND TABLE_SCHEMA != 'performance_schema' AND engine != 'InnoDB'"`
	if [[ "x$r" != "x" ]]; then
		echo "<result>fail</result><message>The following tables are not using InnoDB:
$r</message>"
		exit
	fi

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi
