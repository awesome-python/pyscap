#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not separate user functionality (including user interface services) from database management functionality.</message>'
else
	echo '<result>notchecked</result>'
fi