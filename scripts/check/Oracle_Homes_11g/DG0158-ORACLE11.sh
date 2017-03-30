#!/bin/bash

. lib/oracle.sh

# check if remote users can login as admin via non-secure connections
r=$(sqlplus_sysdba "SELECT VALUE FROM V\$PARAMETER WHERE NAME='audit_sys_operations';")
if [[ ! $r =~ TRUE ]]; then
	fail "DBMS remote administration is not audited: audit_sys_operations isn't set"
fi

pass