#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name='utl_file_dir';" | grep '\*')
if [[ "x$e" == "x" ]]; then
	pass
else
	fail "Access to external objects has not been disabled and is not required or authorized:
$e"
fi
