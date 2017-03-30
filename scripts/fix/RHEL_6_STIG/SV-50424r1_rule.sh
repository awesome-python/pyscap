#!/bin/bash

log_files=`perl -e 'while(<>) { if($_ =~ /^(\*|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|security|syslog|user|uucp|local[0-7]|,)+\..*\s+[-]*(\/\S+)/) { print "$2\n";} }' /etc/rsyslog.conf /etc/rsyslog.d 2>/dev/null`

for i in $log_files; do
	chmod 0600 "$i"
done
