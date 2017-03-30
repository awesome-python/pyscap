#!/bin/bash

. lib/file.sh

log_files=`perl -e 'while(<>) { if($_ =~ /^(\*|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|security|syslog|user|uucp|local[0-7]|,)+\..*\s+[-]*(\/\S+)/) { print "$2\n";} }' /etc/rsyslog.conf /etc/rsyslog.d 2>/dev/null`

for i in $log_files; do
	e=`file_owner "$i"`
	if [[ "$e" != "root" ]]; then
		echo "<result>fail</result><message>owner of $i is not root</message>"
		exit
	fi
done
echo '<result>pass</result>'
