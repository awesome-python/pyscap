#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "Database data files containing sensitive information must be encrypted: not supported"
else
	notchecked
fi
