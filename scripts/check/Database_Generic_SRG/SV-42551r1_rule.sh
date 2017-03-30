#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	r=`ps aux | grep mysqld | egrep -v 'grep|mysqld_safe' | cut -d' ' -f1`
	if [[ "x$r" == "xroot" ]]; then
		echo '<result>fail</result><message>mysqld running as root</message>'
		exit
	fi

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi