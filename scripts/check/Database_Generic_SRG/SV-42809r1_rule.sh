#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# DBMS default accounts must be assigned custom passwords.

	# the default root password is blank, so we check for that

	. lib/mysql.sh
	mysql_not_running_notchecked

	for p in `mysql_query "SELECT CONCAT('x', Password) FROM mysql.user WHERE User='root'"`; do
		#echo "Checking $p"
		if [[ "$p" == "x" ]]; then
			echo '<result>fail</result><message>Found blank passwordfor root account</message>'
			exit
		fi
	done

        for p in `mysql_query "SELECT CONCAT('x', Password) FROM mysql.user WHERE User=''"`; do
                #echo "Checking $p"
                if [[ "$p" == "x" ]]; then
                        echo '<result>fail</result><message>Found blank passwordfor anonymous account</message>'
                        exit
                fi
        done

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi
