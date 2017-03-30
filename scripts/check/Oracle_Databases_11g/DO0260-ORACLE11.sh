#!/bin/bash

. lib/oracle.sh
. lib/file.sh

e=$(sqlplus_sysdba "select count(*) from v\$controlfile;")
if [[ "$e" -lt 2 ]]; then
	fail "A minimum of two Oracle control files are not defined and configured to be stored on separate, archived physical disks or archived directories on a RAID device: $e control files found"
fi

e=$(sqlplus_sysdba "select name from v\$controlfile;")
for i in $e; do
	#echo $i
	m=$(file_mountpoint $i)
	#echo $i mountpoint $m
	if [[ -z "$last_m" ]]; then
		last_m=$m
	elif [[ "x$m" != "x$last_m" ]]; then
		pass
	#else
	#	echo $m matches $last_m
	fi
done

fail "A minimum of two Oracle control files are not defined and configured to be stored on separate, archived physical disks or archived directories on a RAID device:
$e"