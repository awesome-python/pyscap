#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS is not be capable of taking organization defined actions upon audit failure (e.g., overwrite oldest audit records, stop generating audit records, cease processing, notify of audit failure)</message>'
else
	echo '<result>notchecked</result>'
fi