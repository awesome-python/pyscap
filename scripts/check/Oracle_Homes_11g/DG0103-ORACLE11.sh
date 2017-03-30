#!/bin/bash

. lib/oracle.sh

fail_if_no_ORACLE_HOME

f=$ORACLE_HOME/network/admin/sqlnet.ora
if [[ -f $f ]]; then
	r=`egrep -i '^\s*tcp.validnode_checking\s*=\s*YES' $f`
	if [[ "x$r" != "x" ]]; then
		pass
	fi
	
	r=`egrep -i '^\s*tcp.invited_nodes\s*=\s*\([0-9., ]+\)' $f`
	if [[ "x$r" != "x" ]]; then
		pass
	fi

fi

sn=$(sqlplus_sysdba "select value from v\$parameter where name = 'service_names';")

f=$ORACLE_HOME/network/admin/cman.ora
if [[ -f $f ]]; then
	r=`grep -Pizo '\(rule\s*=.*\(src\s*=\s*/32\).*\)' $f`
	if [[ "x$r" != "x" ]]; then
		fail "The DBMS listener does not restrict database access by network address: cman.ora rule is not restricting source addresses (/32)"
	fi
	
	r=`grep -Pizo '\(rule\s*=.*\(src\s*=\s*[0-9.]+/[1-3][0-9]\).*\)' $f`
	if [[ "x$r" != "x" ]]; then
		if [[ $r =~ \(srv\s*=\s*\*\) || $r =~ \(srv\s*=\s*$sn\) ]]; then
			pass
		fi
	fi
	
fi

# TODO add pass check for iptables rule restriction

fail "The DBMS listener does not restrict database access by network address"