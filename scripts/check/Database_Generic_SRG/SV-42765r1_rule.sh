#!/bin/bash

# The DBMS must support the organizational requirements to specifically prohibit or restrict the use of unauthorized functions, ports, protocols, and/or services.

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	mysql_listening_remotely
	if [[ $? ]]; then
		echo '<result>pass</result>'
		exit
	fi

	# TODO
	echo '<result>notchecked</result>'
else
	echo '<result>notchecked</result>'
fi