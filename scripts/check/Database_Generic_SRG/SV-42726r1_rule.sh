#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not provide the capability to automatically process audit records for events of interest based upon selectable event criteria.</message>'
else
	echo '<result>notchecked</result>'
fi