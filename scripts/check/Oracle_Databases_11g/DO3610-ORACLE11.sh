#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select count(*) from all_def_audit_opts where ren = 'A/A';")
if [[ "$e" -eq 0 ]]; then
	fail "Required object auditing is not configured:
$e"
fi

t=$(sqlplus_sysdba "select object_type from dba_obj_audit_opts where object_name = 'AUD\$';")
u=$(sqlplus_sysdba "select upd from dba_obj_audit_opts where object_name = 'AUD\$';")
d=$(sqlplus_sysdba "select del from dba_obj_audit_opts where object_name = 'AUD\$';")
if [[ "$t" =~ "TABLE" ]]; then
	if [[ ! "$u" =~ "A/A" || ! "$d" =~ "A/A" ]]; then
		fail "Required object auditing is not configured:
		AUD\$ type is $t, upd is $u, del is $d"
	fi
elif [[ "$t" =~ "VIEW" ]]; then
	if [[ ! "$u" =~ "A/A" || ! "$d" =~ "A/A" ]]; then
		fail "Required object auditing is not configured:
		AUD\$ type is $t, upd is $u, del is $d"
	fi
	# TODO check underlying table
	# set long 1000
	# set wrap on
	# select text from dba_views where view_name = 'AUD$';
fi

pass