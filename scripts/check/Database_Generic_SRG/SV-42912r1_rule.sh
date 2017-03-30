#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must support organizational requirements to employ automated patch management tools to facilitate flaw remediation to organization defined information system components: not supported"
else
	echo '<result>notchecked</result>'
fi