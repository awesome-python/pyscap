#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must restrict error messages, so only authorized personnel may view them: not supported"
else
	notchecked
fi
