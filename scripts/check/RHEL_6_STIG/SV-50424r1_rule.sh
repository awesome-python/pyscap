#!/bin/bash

. lib/file.sh

log_files=`perl -e 'while(<>) { if($_ =~ /^(\*|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|security|syslog|user|uucp|local[0-7]|,)+\..*\s+[-]*(\/\S+)/) { print "$2\n";} }' /etc/rsyslog.conf /etc/rsyslog.d 2>/dev/null`

for i in $log_files; do
	e=`file_mode "$i"`
	if [ "$e" != "0600" -a "$e" != "0400" -a "$e" != "0000" ]; then
		echo "<result>fail</result><message>log file $i, mode $e isn't 0600 or 0400 or 0000</message>"
		exit
	fi
done
echo '<result>pass</result>'


