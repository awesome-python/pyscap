#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS must notify appropriate individuals when accounts are terminated.</message>'
else
	echo '<result>notchecked</result>'
fi