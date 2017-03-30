#!/bin/bash

. lib/oracle.sh

# Remote administration is not disabled for the Oracle connection manager

f=$ORACLE_HOME/network/admin/sqlnet.ora
if [[ ! -f $f ]]; then
	fail "The SQLNet SQLNET.ALLOWED_LOGON_VERSION parameter is not set to a value of 10 or higher: sqlnet.ora doesn't exist"
fi

r=$(grep 'SQLNET\.ALLOWED_LOGON_VERSION\s*=\s*' $f)
if [[ "x$r" = "x" ]]; then
	fail "The SQLNet SQLNET.ALLOWED_LOGON_VERSION parameter is not set to a value of 10 or higher: SQLNET.ALLOWED_LOGON_VERSION doesn't exist"
fi

r=$(echo $r | sed 's/SQLNET\.ALLOWED_LOGON_VERSION\s*=\s*\(.*\)$/\1/')
if [[ "$r" -lt 10 ]]; then
	fail "The SQLNet SQLNET.ALLOWED_LOGON_VERSION parameter is not set to a value of 10 or higher: SQLNET.ALLOWED_LOGON_VERSION is less than 10"
fi

pass
