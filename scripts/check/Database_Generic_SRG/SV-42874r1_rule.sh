#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not automatically terminate emergency accounts after an organization defined time period for each type of account: not supported</message>'
else
	echo '<result>notchecked</result>'
fi