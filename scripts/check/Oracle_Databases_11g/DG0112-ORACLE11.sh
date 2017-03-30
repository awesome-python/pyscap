#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select file_name from dba_data_files
where tablespace_name='SYSTEM';" | tail -n +4)
if [[ $e =~ 'no rows selected' ]]; then
	# no system files
	pass
else
	for i in $e; do
		f=$(find `dirname $i` -mindepth 1 -not -iname '*.dbf' -and -not -iname 'redo*.log' -and -not -iname '*.ctl')
		if [[ "x$f" != "x" ]]; then
			fail "DBMS system data files are not stored in dedicated disk directories: $f"
		fi
	done
	pass
fi
