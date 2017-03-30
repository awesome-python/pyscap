#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select owner,db_link from dba_db_links;")
if [[ "x$e" = $'x\nno rows selected' ]]; then
	# no db links
	pass
fi

f=$(sqlplus_sysdba "select count(*) from sys.dba_repcatlog;")
if [[ $f =~ ^\s*0\s*$ ]]; then
	# no db links used for replication
	pass
fi

fail "Fixed user and public database links are not authorized for use:
$e
$f"