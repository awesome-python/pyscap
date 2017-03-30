#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>Attempts to bypass access controls are not audited.</message>'
else
	echo '<result>notchecked</result>'
fi