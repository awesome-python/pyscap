#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must employ NSA-approved cryptography to protect classified information: not supported"
else
	notchecked
fi
