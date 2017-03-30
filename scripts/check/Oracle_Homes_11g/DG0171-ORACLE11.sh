#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME

if [[ ! $STIG_DB_CONFIDENTIALITY =~ public ]]; then
	notapplicable "The DBMS has a connection defined to access or be accessed by a DBMS at a different classification level"
fi

r=$(sqlplus_sysdba "set feedback off;
SELECT COUNT(*) FROM DBA_DB_LINKS;")
if [[ "$r" -gt 0 ]]; then
	fail "The DBMS has a connection defined to access or be accessed by a DBMS at a different classification level: $(sqlplus_sysdba "SELECT DB_LINK, HOST FROM DBA_DB_LINKS;")"
fi

pass
