#!/bin/bash

. lib/oracle.sh

echo -n "This script removes roles from PUBLIC and . This may cause problems if programs are relying on this behavior. Continue? (yes/no):"

read r
if [[ ! $r =~ ^[yY] ]]; then
	exit
fi

#sqlplus_sysdba "revoke UTL_SMTP_ROLE from PUBLIC;"
#sqlplus_sysdba "select * from dba_errors order by sequence;"

q=$(sqlplus_sysdba "select COUNT(*) from all_objects where status <> 'VALID';")
if [[ "$q" -gt "0" ]]; then
	echo "Please fix $q invalid objects before running fix script:"
	sqlplus_sysdba "set feed off;
	select distinct '    ' || object_type || ',' || owner || '.' || object_name from all_objects where status <> 'VALID';"
	exit
fi

# From STIG
privs="UTL_HTTP 
UTL_FILE
UTL_SMTP
UTL_TCP
DBMS_BACKUP_RESTORE
DBMS_JOB
DBMS_LOB
DBMS_OBFUSCATION_TOOLKIT
DBMS_RANDOM
DBMS_SQL
DBMS_SYS_SQL"

# From http://www.red-database-security.com/wp/sentrigo_webinar.pdf
# privs="$privs
# UTL_INADDR
# UTL_DBWS
# DBMS_CRYPTO_TOOLKIT
# DBMS_ADVISOR
# DBMS_LDAP
# DBMS_LDAP_UTL
# DBMS_SCHEDULER
# DBMS_DDL
# DBMS_EPG
# DBMS_XMLGEN
# DBMS_AW_XML
# CTXSYS.DRITHSX
# ORDSYS.ORD_DICOM"

for i in $privs; do
	q=$(sqlplus_sysdba "select COUNT(*) from dba_tab_privs
	where grantee='PUBLIC' and privilege ='EXECUTE'
	and table_name = '$i';")
	if [[ "$q" -le "0" ]]; then
		echo "Skipping $i, already revoked"
		continue
	fi
	
	r="$(echo -n $i)_ROLE"
	
	echo "$i referred to by:"
	sqlplus_sysdba "set feed off;
	select distinct '    ' || owner || '.' || name || ' depends on ' || referenced_owner || '.' || referenced_name
	from all_dependencies where referenced_name = '$i';"
	
	deps=$(sqlplus_sysdba "set feed off;
	select distinct owner
	from all_dependencies where referenced_name = '$i'
	and owner <> 'PUBLIC';")
	
	# create role for assigning package privileges
	sqlplus_sysdba "drop role $r;" &>/dev/null
	sqlplus_sysdba "create role $r;"
	sqlplus_sysdba "grant execute on $i to $r;"

	# assign privilege to dependents
	for d in $deps; do
		q=$(sqlplus_sysdba "select count(*) from DBA_ROLE_PRIVS where grantee='$d' and granted_role = '$r';")
		if [[ "$q" -gt "0" ]]; then
			echo $d already has role $r. Skipping...
		else
			echo Granting $r to $d...
			sqlplus_sysdba "grant $r to $d;"
		fi
	done

	echo
	echo "Revoking PUBLIC's execute privilege to $i..."
	sqlplus_sysdba "revoke execute on $i from PUBLIC;"

	echo
	echo "Fixing invalid objects:"
	sqlplus_sysdba "EXEC UTL_RECOMP.recomp_serial();"
	
	echo "Still have invalid objects:"
	sqlplus_sysdba "set feed off;
	select distinct '    ' || object_type || ',' || owner || '.' || object_name from all_objects where status <> 'VALID';"
	
	echo
	q=$(sqlplus_sysdba "select COUNT(*) from all_objects where status <> 'VALID';")
	if [[ "$q" -gt "0" ]]; then
		q=$(sqlplus_sysdba "set feed off;
			select distinct owner from all_objects where status <> 'VALID';")
		for o in $q; do
			if [[ "x$o" = "xPUBLIC" ]]; then
				echo 
			fi
			echo "Trying to grant directly to $o..."
			sqlplus_sysdba "grant execute on $i to $o;"
		done
		sqlplus_sysdba "EXEC UTL_RECOMP.recomp_serial();"
	fi
	
	q=$(sqlplus_sysdba "select COUNT(*) from all_objects where status <> 'VALID';")
	if [[ "$q" -gt "0" ]]; then
		echo
		echo Failed re-compiling:
		sqlplus_sysdba "set feed off;
		select distinct '    ' || object_type || ',' || owner || '.' || object_name from all_objects where status <> 'VALID';"

		echo Reverting back to public grant.
		sqlplus_sysdba "GRANT execute on $i TO PUBLIC;"
		sqlplus_sysdba "EXEC UTL_RECOMP.recomp_serial();"
	fi
done