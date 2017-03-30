#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not provide the ability to write specified audit record content to a centralized audit log repository.</message>'
else
	echo '<result>notchecked</result>'
fi