#!/bin/bash

# The DBMS must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	for p in `mysql_query "SELECT 1 FROM mysql.user WHERE User=''"`; do
		#echo "Checking $p"
		if [[ "x$p" == "x1" ]]; then
			#echo anonymous username
			echo '<result>fail</result><message>Anonymous username found for database</message>'
			exit
		fi
	done

	for p in `mysql_query "SELECT 1 FROM mysql.tables_priv WHERE User=''"`; do
		#echo "Checking $p"
		if [[ "x$p" == "x1" ]]; then
			#echo anonymous username
			echo '<result>fail</result><message>Anonymous username found for table</message>'
			exit
		fi
	done

	for p in `mysql_query "SELECT 1 FROM mysql.columns_priv WHERE User=''"`; do
		#echo "Checking $p"
		if [[ "x$p" == "x1" ]]; then
			#echo anonymous username
			echo '<result>fail</result><message>Anonymous username found for column</message>'
			exit
		fi
	done

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi
