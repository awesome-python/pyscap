#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not support the enforcement of a two-person rule for changes to organization defined application components and system-level information.</message>'
else
	echo '<result>notchecked</result>'
fi