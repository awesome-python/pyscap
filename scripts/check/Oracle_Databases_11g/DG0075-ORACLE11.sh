#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select db_link,host from dba_db_links;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Unauthorized database links should not be defined and active:
$e"
fi
