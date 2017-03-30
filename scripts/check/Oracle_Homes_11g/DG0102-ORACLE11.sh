#!/bin/bash

. lib/oracle.sh

# all database processes
q=`ps ef | grep -i pmon | grep -v grep`
if [[ "x$q" != "x" && ! $q =~ ^oracle ]]; then
	fail "DBMS processes or services are not run under custom, dedicated OS accounts: $q"
fi
# all listener processes
q=`ps ef | grep -i tns | grep -v grep`
if [[ "x$q" != "x" && ! $q =~ ^oracle ]]; then
	fail "DBMS processes or services are not run under custom, dedicated OS accounts: $q"
fi
# Oracle Intelligent Agents
q=`ps ef | grep -i dbsnmp | grep -v grep`
if [[ "x$q" != "x" && ! $q =~ ^oracle ]]; then
	fail "DBMS processes or services are not run under custom, dedicated OS accounts: $q"
fi

pass