#!/bin/bash

. lib/db.sh
die_if_no_db

if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	sh fix/Database_Generic_SRG/mysql_audit_rules.sh
fi
