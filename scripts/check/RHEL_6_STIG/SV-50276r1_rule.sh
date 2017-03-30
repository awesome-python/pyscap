#!/bin/bash

if [[ "x$(rpm -q --queryformat "%{SUMMARY}\n" gpg-pubkey | grep 'not installed')" != "x" ]]; then
	echo '<result>fail</result><message>Test package gpg-pubkey is not installed</message>'
	exit 1
fi 

r=`rpm -q --queryformat "%{SUMMARY}\n" gpg-pubkey | grep 'Red Hat' 2>/dev/null`
c=`rpm -q --queryformat "%{SUMMARY}\n" gpg-pubkey | grep 'CentOS' 2>/dev/null`

if [[ "x$r" == "x" &&  "x$c" == "x" ]]; then
	echo '<result>fail</result><message>OS is not Red Hat or CentOS</message>'
else
	echo '<result>pass</result>'
fi
