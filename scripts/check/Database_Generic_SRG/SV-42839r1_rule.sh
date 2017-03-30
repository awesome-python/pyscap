#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must employ NIST validated FIPS compliant cryptography to protect unclassified information when such information must be separated from individuals who have the necessary clearances yet lack the necessary access approvals: not supported"
else
	notchecked
fi
