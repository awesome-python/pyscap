#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	mysql_listening_remotely
	if [[ ! $? ]]; then
		echo '<result>notapplicable</result>'
		exit
	fi

	# mysql returns the thread id for connection_id(), nothing random

	echo '<result>fail</result><message>mysql returns the thread id for connection_id(), nothing random</message>'
else
	echo '<result>notchecked</result>'
fi