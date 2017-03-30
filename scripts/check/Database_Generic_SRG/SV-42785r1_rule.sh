#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_not_running_notchecked

	mysql_na_if_not_listening_remotely

	mysql_fail_if_no_pam_plugin
	
	notchecked "The DBMS, if using multifactor authentication when accessing privileged accounts via the network, must provide one of the factors by a device that is separate from the information system gaining access"
else
	notchecked
fi