#!/bin/bash

. lib/oracle.sh
. lib/file.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'spfile';
select member from v\$logfile;
select name from v\$datafile;
select name from v\$controlfile;" | egrep -v -e '^NAME$' -e '^MEMBER$' -e '^VALUE$' -e '^-+$' -e 'rows selected\.$' -e '^$')
for f in $e; do
	#ls -l $f
	p=$(file_perm $f)
	o=$(file_owner $f)
	g=$(file_groupowner $f)
	if [ "x$(file_perm_lt $p 0640)" = "xtrue" ]; then
		fail "Access to sensitive data is not restricted to authorized users identified by the Information Owner: too permissive mode on $f, $p"
	fi
	if [ "x$o" = $'x\noracle' ]; then
		fail "Access to sensitive data is not restricted to authorized users identified by the Information Owner: $o is not oracle for $f"
	fi
	if [ "x$g" = $'x\ndba' ]; then
		fail "Access to sensitive data is not restricted to authorized users identified by the Information Owner: $g is not dba for $f"
	fi
done

pass