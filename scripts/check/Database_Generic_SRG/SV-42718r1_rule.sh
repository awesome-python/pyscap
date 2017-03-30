#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not shutdown immediately in the event of an audit failure, unless an alternative audit capability exists.</message>'
else
	echo '<result>notchecked</result>'
fi