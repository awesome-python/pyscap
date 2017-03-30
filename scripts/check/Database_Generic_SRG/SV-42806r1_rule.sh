#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	mysql_na_if_not_listening_remotely

	fail "The DBMS must support organizational requirements to enforce password encryption for transmission"
else
	notchecked
fi
