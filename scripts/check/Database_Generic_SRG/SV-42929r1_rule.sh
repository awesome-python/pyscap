#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must support taking organization defined list of least disruptive actions to terminate suspicious events: not supported"
else
	notchecked
fi
