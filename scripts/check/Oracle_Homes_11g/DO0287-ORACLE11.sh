#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME

if [[ ! -f $ORACLE_HOME/network/admin/sqlnet.ora ]]; then
	fail "The Oracle SQLNET.EXPIRE_TIME parameter is not set to a value greater than 0: no sqlnet.ora"
fi

p=$(grep -i SQLNET.EXPIRE_TIME $ORACLE_HOME/network/admin/sqlnet.ora)
if [[ "x$p" = "x" ]]; then
	fail "The Oracle SQLNET.EXPIRE_TIME parameter is not set to a value greater than 0: No SQLNET.EXPIRE_TIME"
fi

p=$(echo $p | cut -d= -f 2)
if [[ "$p" -le 0 ]]; then
	fail "The Oracle SQLNET.EXPIRE_TIME parameter is not set to a value greater than 0: SQLNET.EXPIRE_TIME <= 0"
fi

pass