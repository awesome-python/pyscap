#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	mysql_pam_enabled
	if [[ "x$?" != "x1" ]]; then
		# if not enabled, no role mapping implemented
		echo '<result>fail</result><message>pam plugin is not enabled, no role mapping implemented</message>'
		exit
	fi

	### TODO need to check if role-mapping is implemented
	echo '<result>notchecked</result>'
else
	echo '<result>notchecked</result>'
fi