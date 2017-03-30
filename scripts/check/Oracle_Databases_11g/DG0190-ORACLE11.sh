#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select * from ALL_DB_LINKS;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
fi

fail "Database links defined:
$e"