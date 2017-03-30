#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	mysql_na_if_not_listening_remotely

	fail "The DBMS must enforce requirements for remote connections to the information system"
else
	notchecked
fi
