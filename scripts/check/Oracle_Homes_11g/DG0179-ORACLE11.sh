#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME

if [[ ! -f $ORACLE_HOME/network/admin/sqlnet.ora ]]; then
	fail "The DBMS warning banner does not meet DoD policy requirements: no sqlnet.ora file"
fi

q=$(grep SEC_USER_AUDIT_ACTION_BANNER $ORACLE_HOME/network/admin/sqlnet.ora 2>/dev/null)
if [[ "x$q" = "x" ]]; then
	fail "The DBMS warning banner does not meet DoD policy requirements: SEC_USER_AUDIT_ACTION_BANNER not defined"
fi

q=$(grep SEC_USER_UNAUTHORIZED_ACCESS_BANNER $ORACLE_HOME/network/admin/sqlnet.ora 2>/dev/null)
if [[ "x$q" = "x" ]]; then
	fail "The DBMS warning banner does not meet DoD policy requirements: SEC_USER_UNAUTHORIZED_ACCESS_BANNER not defined"
fi

pass