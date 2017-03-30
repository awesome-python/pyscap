#!/bin/bash

. lib/oracle.sh
. lib/file.sh

ORACLE_BASE=`su -l oracle -c 'echo $ORACLE_BASE'`
error_if_no_ORACLE_BASE

q=`su -l oracle -c 'find $ORACLE_BASE -name extproc'`
p=`file_perm $q`
if [[ $(file_perm_gt $p 0700) == 'true' ]]; then
	fail "Access to external DBMS executables is not disabled or restricted: $q has > 0700 perms: $p"
fi

error_if_no_ORACLE_HOME

q=`egrep -i '^\s*run_user\s*=\s*nobody' $ORACLE_HOME/rdbms/admin/externaljob.ora`
if [[ "x$q" = "x" ]]; then
	fail "Access to external DBMS executables is not disabled or restricted: run_user is not set to nobody in externaljob.ora"
fi

q=`egrep -i '^\s*run_group\s*=\s*nobody' $ORACLE_HOME/rdbms/admin/externaljob.ora`
if [[ "x$q" = "x" ]]; then
	fail "Access to external DBMS executables is not disabled or restricted: run_group is not set to nobody in externaljob.ora"
fi

if [[ ! -f $ORACLE_HOME/hs/admin/extproc.ora ]]; then
	fail "Access to external DBMS executables is not disabled or restricted: extproc.ora does not exist"
fi

#EXTPROC_DLLS=ONLY:[dll full file name1]:[dll full file name2]:..
q=`egrep -i '^\s*EXTPROC_DLLS\s*=\s*(ONLY|:|/.*)+' $ORACLE_HOME/hs/admin/extproc.ora`
if [[ "x$q" = "x" ]]; then
	fail "Access to external DBMS executables is not disabled or restricted: EXTPROC_DLLS is not set correctly in extproc.ora: $q"
fi

q=`grep -i 'EXTPROC' $ORACLE_HOME/network/admin/listener.ora`
if [[ "x$q" = "x" ]]; then
	fail "Access to external DBMS executables is not disabled or restricted: EXTPROC is accessible from the listener"
fi

pass