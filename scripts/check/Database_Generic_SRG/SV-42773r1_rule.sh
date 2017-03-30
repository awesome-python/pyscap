#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "DBMS must conduct backups of system-level information per organization defined frequency that is consistent with recovery time and recovery point objectives"
else
	notchecked
fi

