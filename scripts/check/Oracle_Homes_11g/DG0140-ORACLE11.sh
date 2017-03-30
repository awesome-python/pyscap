#!/bin/bash

. lib/oracle.sh

fail_if_no_ORACLE_HOME

r=$(auditctl -l | grep "$ORACLE_HOME")
if [[ "x$r" == "x" ]]; then
	fail "Access to DBMS security data is not audited"
fi

pass