#!/bin/bash
# Unused database components which are integrated in the DBMS and cannot be uninstalled must be disabled.

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi