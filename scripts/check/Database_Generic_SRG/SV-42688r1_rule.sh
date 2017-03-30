#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS must maintain reviewer/releaser identity and credentials within the established chain of custody for all information reviewed or released</message>'
else
	echo '<result>notchecked</result>'
fi