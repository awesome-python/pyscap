#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	r=`mysql_query "SHOW VARIABLES LIKE 'local_infile'" | grep ON`
	if [[ ! -z "$r" ]]; then
		echo '<result>fail</result><message>Local infile is enabled</message>'
	else
		echo '<result>pass</result>'
	fi
else
	echo '<result>notchecked</result>'
fi
