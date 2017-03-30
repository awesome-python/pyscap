#!/bin/bash

. lib/oracle.sh

fail_if_no_ORACLE_HOME

f=/etc/oratab
if [[ ! -f $f ]]; then
	fail "DBMS service identification is not unique or does not clearly identify the service: oratab doesn't exist"
fi

sn=$(egrep -v '(^#)|(^\s*$)' /etc/oratab | cut -d: -f1)

fail "DBMS service identification is not unique or does not clearly identify the service: service names: $sn"
