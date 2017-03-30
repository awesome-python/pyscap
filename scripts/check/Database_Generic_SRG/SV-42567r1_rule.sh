#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	mysql_pam_enabled
	if [[ "x$?" != "x1" ]]; then
		echo '<result>fail</result><message>pam plugin is not enabled</message>'
		exit
	fi

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi