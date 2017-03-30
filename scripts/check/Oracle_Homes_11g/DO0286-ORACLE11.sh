#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME

if [[ ! -f $ORACLE_HOME/network/admin/sqlnet.ora ]]; then
	fail "The Oracle INBOUND_CONNECT_TIMEOUT and SQLNET.INBOUND_CONNECT_TIMEOUT parameters are not set to a value greater than 0: no sqlnet.ora"
fi

for i in $(oracle_listeners); do
	p=$(grep -i INBOUND_CONNECT_TIMEOUT_$i $ORACLE_HOME/network/admin/sqlnet.ora)
	if [[ "x$p" = "x" ]]; then
		fail "The Oracle INBOUND_CONNECT_TIMEOUT and SQLNET.INBOUND_CONNECT_TIMEOUT parameters are not set to a value greater than 0: No INBOUND_CONNECT_TIMEOUT for listener $i"
	fi
	
	p=$(echo $p | cut -d= -f 2)
	if [[ "$p" -le 0 ]]; then
		fail "The Oracle INBOUND_CONNECT_TIMEOUT and SQLNET.INBOUND_CONNECT_TIMEOUT parameters are not set to a value greater than 0: INBOUND_CONNECT_TIMEOUT for listener $i <= 0"
	fi
done

p=$(grep -i SQLNET.INBOUND_CONNECT_TIMEOUT $ORACLE_HOME/network/admin/sqlnet.ora)
if [[ "x$p" = "x" ]]; then
	fail "The Oracle INBOUND_CONNECT_TIMEOUT and SQLNET.INBOUND_CONNECT_TIMEOUT parameters are not set to a value greater than 0: No INBOUND_CONNECT_TIMEOUT"
fi

p=$(echo $p | cut -d= -f 2)
if [[ "$p" -le 0 ]]; then
	fail "The Oracle INBOUND_CONNECT_TIMEOUT and SQLNET.INBOUND_CONNECT_TIMEOUT parameters are not set to a value greater than 0: INBOUND_CONNECT_TIMEOUT <= 0"
fi

pass