#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not identify potentially security-relevant error conditions: not supported</message>'
else
	echo '<result>notchecked</result>'
fi