#!/bin/bash

# DBMS default account names must be changed.

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# the default username is root, so we check for that and anonymous user

	. lib/mysql.sh
	mysql_not_running_notchecked

	for p in `mysql_query "SELECT 1 FROM mysql.user WHERE User='root'"`; do
		#echo "Checking $p"
		if [[ "x$p" == "x1" ]]; then
			echo "<result>fail</result><message>default account root user found</message>"
			exit
		fi
	done

        for p in `mysql_query "SELECT 1 FROM mysql.user WHERE User=''"`; do
                #echo "Checking $p"
                if [[ "x$p" == "x1" ]]; then
                        echo "<result>fail</result><message>default account '' (anonymous) user found</message>"
                        exit
                fi
        done

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi
