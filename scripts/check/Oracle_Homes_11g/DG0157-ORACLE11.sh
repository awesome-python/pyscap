#!/bin/bash

. lib/oracle.sh

# check if remote users can login as admin via non-secure connections
r=$(sqlplus_sysdba "SELECT VALUE FROM V\$PARAMETER WHERE NAME='remote_login_passwordfile';")
if [[ $r =~ (EXCLUSIVE|SHARED) ]]; then
	fail "Remote DBMS administration is not documented, not authorized or is not disabled: remote_login_passwordfile is set to EXCLUSIVE or SHARED"
fi

r=$(grep 'dba' /etc/group 2>/dev/null)
if [[ "x$r" = "x" ]]; then
	fail "Remote DBMS administration is not documented, not authorized or is not disabled: OSDBA (dba) group contains $(grep 'dba' /etc/group | cut -d: -f4)"
fi

r=$(grep 'oper' /etc/group 2>/dev/null)
if [[ "x$r" = "x" ]]; then
	fail "Remote DBMS administration is not documented, not authorized or is not disabled: OSOPER (oper) group contains $(grep 'oper' /etc/group | cut -d: -f4)"
fi

pass