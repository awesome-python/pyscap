#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	# if we don't allow remote connections, this is NA
	mysql_listening_remotely
	if [[ $? ]]; then
		echo '<result>notapplicable</result>'
		exit
	fi

	# TODO
	echo '<result>notchecked</result>'
else
	echo '<result>notchecked</result>'
fi