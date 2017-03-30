#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "Procedures for establishing temporary passwords that meet DoD password requirements for new accounts must be defined, documented, and implemented"
else
	notchecked
fi
