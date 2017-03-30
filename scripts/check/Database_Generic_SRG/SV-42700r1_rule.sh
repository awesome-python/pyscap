#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not allow designated organizational personnel to select which auditable events are to be audited by the database.</message>'
else
	echo '<result>notchecked</result>'
fi