#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "SET LINESIZE 1024;
SET PAGESIZE 0;
select name from stmt_audit_option_map
where name not in
(select audit_option from dba_stmt_audit_opts)
and name not in
('ALL STATEMENTS',
'ANALYZE ANY DICTIONARY',
'CREATE DIRECTORY',
'DEBUG CONNECT ANY',
'DEBUG CONNECT USER',
'DELETE ANY TABLE',
'DELETE TABLE',
'DROP DIRECTORY',
'EXECUTE ANY LIBRARY',
'EXECUTE ANY PROCEDURE',
'EXECUTE ANY TYPE',
'EXECUTE LIBRARY',
'EXECUTE PROCEDURE',
'EXISTS',
'GRANT LIBRARY',
'INSERT ANY TABLE',
'INSERT TABLE',
'LOCK TABLE',
'NETWORK',
'OUTLINE',
'READUP',
'READUP DBHIGH',
'SELECT ANY DICTIONARY',
'SELECT ANY SEQUENCE',
'SELECT ANY TABLE',
'SELECT MINING MODEL',
'SELECT SEQUENCE',
'SELECT TABLE',
'UPDATE ANY TABLE',
'UPDATE TABLE',
'USE EDITION',
'WRITEDOWN',
'WRITEDOWN DBLOW',
'WRITEUP',
'WRITEUP DBHIGH');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Attempts to bypass access controls are not audited:
$e"
fi

