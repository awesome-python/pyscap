#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must enforce dual authorization, based on organizational policies and procedures for organization defined privileged commands"
else
	notchecked
fi

