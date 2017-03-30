#!/bin/bash

. lib/oracle.sh

p=$(dba_privs)

if [ "x$(table_exists DBA_SNAPSHOTS)" = "xfalse" ]; then
	if [ "x$(table_exists DBA_REGISTERED_SNAPSHOT)" = "xfalse" ]; then
		pass
	else
		e=$(sqlplus_sysdba "select
				grantee grantee,
				granted_role priv
			from    dba_role_privs
			where   grantee in (select OWNER FROM DBA_REGISTERED_SNAPSHOTS)
				and granted_role in ($p)
			union
			select
				grantee grantee,
				privilege priv
			from    dba_sys_privs
			where   grantee in (select OWNER FROM DBA_REGISTERED_SNAPSHOTS)
				and privilege in ($p)
			union
			select
				grantee grantee,
				privilege priv
			from    dba_tab_privs
			where   grantee in (select OWNER FROM DBA_REGISTERED_SNAPSHOTS)
				and privilege in ($p)
			union
			select
				grantee grantee,
				privilege priv
			from    dba_col_privs
			where   grantee in (select OWNER FROM DBA_REGISTERED_SNAPSHOTS)
				and privilege in ($p);")
		if [[ $e =~ 'no rows selected' ]]; then
			# not replicating
			pass
		else
			fail "Registered owners users with DBA privs:
$e"
		fi
	fi
else
	e=$(sqlplus_sysdba "select
            grantee grantee,
            granted_role priv
        from    dba_role_privs
        where   grantee in (select OWNER FROM DBA_SNAPSHOTS)
			and granted_role in ($p)
        union
        select
            grantee grantee,
            privilege priv
        from    dba_sys_privs
        where   grantee in (select OWNER FROM DBA_SNAPSHOTS)
			and privilege in ($p)
        union
        select
            grantee grantee,
            privilege priv
        from    dba_tab_privs
        where   grantee in (select OWNER FROM DBA_SNAPSHOTS)
			and privilege in ($p)
        union
        select
            grantee grantee,
            privilege priv
        from    dba_col_privs
        where   grantee in (select OWNER FROM DBA_SNAPSHOTS)
			and privilege in ($p);")
	if [[ $e =~ 'no rows selected' ]]; then
		# not replicators with dba privs
		pass
	else
		fail "Snapshot owners with DBA privs:
$e"
	fi
fi