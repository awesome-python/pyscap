#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	if [[ -e /etc/my.cnf ]]; then
		echo '<result>fail</result><message>/etc/my.cnf exists</message>'
		exit
	fi

	# /etc/mysql/my.cnf is ok

	if [[ -e ~mysql/.my.cnf ]]; then
		echo '<result>fail</result><message>~mysql/.my.cnf exists</message>'
		exit
	fi

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi