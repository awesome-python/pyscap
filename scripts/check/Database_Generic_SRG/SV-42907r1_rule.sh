#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must only generate error messages that provide information necessary for corrective actions without revealing organization defined sensitive or potentially harmful information in error logs and administrative messages that could be exploited: not supported"
else
	notchecked
fi
