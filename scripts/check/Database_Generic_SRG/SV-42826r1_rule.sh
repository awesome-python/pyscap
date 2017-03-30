#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "Databases employed to write data to portable digital media must use cryptographic mechanisms to protect and restrict access to information on portable digital media: not supported"
else
	notchecked
fi
