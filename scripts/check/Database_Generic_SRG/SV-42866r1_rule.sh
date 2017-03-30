#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must preserve any organization defined system state information in the event of a system failure: not supported"
else
	notchecked
fi
