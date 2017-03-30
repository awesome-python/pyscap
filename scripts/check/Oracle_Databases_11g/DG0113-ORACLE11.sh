#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select file_name from dba_data_files t1, dba_tablespaces t2
where t1.tablespace_name = t2.tablespace_name;" | egrep -v -e '^FILE_NAME$' -e '^-+$' -e 'rows selected\.$' -e '^$')

fail "DBMS data files are not dedicated to support individual applications: $e"
