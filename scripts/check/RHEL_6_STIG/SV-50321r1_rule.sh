#!/bin/bash

e=`perl -e 'while(<>) { if($_ =~ /^\*\.\*\s+(@|@@|\:omrelp\:)+\S+/) { print "$_\n";} }' /etc/rsyslog.conf /etc/rsyslog.d 2>/dev/null`

if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>syslog messages are not being sent to remote host</message>'
	exit
fi
echo '<result>pass</result>'


