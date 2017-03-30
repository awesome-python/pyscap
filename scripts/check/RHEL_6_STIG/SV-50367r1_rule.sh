#!/bin/bash

r=`grep EACCES /etc/audit/audit.rules`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>EACCES errors are not audited</message>'
	exit
fi

r=`grep EPERM /etc/audit/audit.rules`

if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>EPERM errors are not audited</message>'
	exit
fi

echo '<result>pass</result>'