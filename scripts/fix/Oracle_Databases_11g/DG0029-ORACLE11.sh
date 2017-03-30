#!/bin/bash

. lib/oracle.sh

echo Audit Tablespaces:
sqlplus_sysdba "SELECT table_name, tablespace_name
FROM   dba_tables
WHERE  table_name = 'AUD\$'
OR table_name = 'FGA_LOG\$';"


sqlplus_sysdba 'SELECT COUNT(*) FROM FGA_LOG$ ;
SELECT COUNT(*) FROM aud$ ;'
exit 0

deinit()
{
	echo Deinitializing the DBMS_AUDIT_MGMT package...
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.deinit_cleanup(audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD);
	END;
	/
	" >/dev/null 2>/dev/null
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.deinit_cleanup(audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_FGA_STD);
	END;
	/
	" >/dev/null 2>/dev/null
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.deinit_cleanup(audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS);
	END;
	/
	" >/dev/null 2>/dev/null
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.deinit_cleanup(audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_XML);
	END;
	/
	" >/dev/null 2>/dev/null
}

drop_purge()
{
	echo Dropping old purge jobs...
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.drop_purge_job(
     audit_trail_purge_name     => 'AUDIT_PURGE_AUD');
	END;
	/
	" >/dev/null 2>/dev/null
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.drop_purge_job(
	 audit_trail_purge_name     => 'AUDIT_PURGE_FGA');
	END;
	/
	" >/dev/null 2>/dev/null
}

drop_ts()
{
	echo Dropping old timestamp update jobs...
	sqlplus_sysdba "BEGIN
	DBMS_SCHEDULER.DROP_JOB(
		job_name        => 'AUDIT_TS_AUD',
		force			=> TRUE);
	END;
	/
	" >/dev/null 2>/dev/null
	sqlplus_sysdba "BEGIN
	DBMS_SCHEDULER.DROP_JOB(
		job_name        => 'AUDIT_TS_FGA',
		force			=> TRUE);
	END;
	/
	" >/dev/null 2>/dev/null
}

error_if_no_ORACLE_HOME
e=$(sqlplus_sysdba "SELECT DISTINCT Owner, Object_Type, Object_Name FROM DBA_Objects_AE
     WHERE Owner IN (
       'SYS', 'OUTLN', 'SYSTEM', 'CTXSYS', 'DBSNMP',
       'LOGSTDBY_ADMINISTRATOR', 'ORDSYS',
       'ORDPLUGINS', 'OEM_MONITOR', 'MDSYS', 'LBACSYS', 
       'DMSYS', 'WMSYS', 'OLAPDBA', 'OLAPSVR', 'OLAP_USER',
       'OLAPSYS', 'EXFSYS', 'SYSMAN', 'MDDATA',
       'SI_INFORMTN_SCHEMA', 'XDB', 'ODM')
     AND Object_Type = 'PACKAGE'
	 AND Object_Name = 'DBMS_AUDIT_MGMT'
     ORDER BY Owner, Object_Type, Object_Name;")
if [[ "$e" =~ 'no rows selected' ]]; then
	echo "DBMS_AUDIT_MGMT package is not installed."
	exit 1
fi

if [[ -z "$STIG_DB_CONFIDENTIALITY" ]]; then
	echo 'STIG_DB_CONFIDENTIALITY not set'
	exit 1
elif [[ "x$STIG_DB_CONFIDENTIALITY" = "xpublic" || "x$STIG_DB_CONFIDENTIALITY" = "xsensitive" ]]; then
	deinit
	
	echo Initializing the DBMS_AUDIT_MGMT package...
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.init_cleanup(
		audit_trail_type         => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD,
		default_cleanup_interval => 12 /* hours */);
	END;
	/
	"
	
	drop_purge
	
	echo Setting up purge job...
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP(
		AUDIT_TRAIL_TYPE     =>  DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD,
		LAST_ARCHIVE_TIME    =>  SYSTIMESTAMP-30 /* days */);
	DBMS_AUDIT_MGMT.create_purge_job(
		audit_trail_type           => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD,
		audit_trail_purge_interval => 24 /* hours */,  
		audit_trail_purge_name     => 'AUDIT_PURGE_AUD',
		use_last_arch_timestamp    => TRUE);
	END;
	/
	"
	
	drop_ts
	
	echo Creating timestamp update job...
	sqlplus_sysdba "BEGIN
	DBMS_SCHEDULER.create_job (
		job_name        => 'AUDIT_TS_AUD',
		job_type        => 'PLSQL_BLOCK',
		job_action      => 'BEGIN 
							  DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP(DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD, TRUNC(SYSTIMESTAMP)-30);
							END;',
		start_date      => SYSTIMESTAMP,
		repeat_interval => 'freq=daily; byhour=0; byminute=0; bysecond=0;',
		end_date        => NULL,
		enabled         => TRUE,
		comments        => 'Automatically set audit last archive time.');
	END;
	/
	"
	
	echo Setting audit_trail to DB
	sqlplus_sysdba "alter system set audit_trail = DB scope = spfile;"
elif [[ "x$STIG_DB_CONFIDENTIALITY" = "xclassified" ]]; then
	deinit
	
	echo Initializing the DBMS_AUDIT_MGMT package...
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.init_cleanup(
		audit_trail_type         => DBMS_AUDIT_MGMT.AUDIT_TRAIL_FGA_STD,
		default_cleanup_interval => 12 /* hours */);
	END;
	/
	"
	
	drop_purge
	
	echo Creating purge job...
	sqlplus_sysdba "BEGIN
	DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP(
		AUDIT_TRAIL_TYPE     =>  DBMS_AUDIT_MGMT.AUDIT_TRAIL_FGA_STD,
		LAST_ARCHIVE_TIME    =>  SYSTIMESTAMP-30 /* days */);
	DBMS_AUDIT_MGMT.create_purge_job(
		audit_trail_type           => DBMS_AUDIT_MGMT.AUDIT_TRAIL_FGA_STD,
		audit_trail_purge_interval => 24 /* hours */,  
		audit_trail_purge_name     => 'AUDIT_PURGE_FGA',
		use_last_arch_timestamp    => TRUE);
	END;
	/
	"
	
	drop_ts
	
	echo Creating timestamp update job...
	sqlplus_sysdba "BEGIN
	DBMS_SCHEDULER.create_job (
		job_name        => 'AUDIT_TS_FGA',
		job_type        => 'PLSQL_BLOCK',
		job_action      => 'BEGIN 
							  DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP(DBMS_AUDIT_MGMT.AUDIT_TRAIL_FGA_STD, TRUNC(SYSTIMESTAMP)-30);
							END;',
		start_date      => SYSTIMESTAMP,
		repeat_interval => 'freq=daily; byhour=0; byminute=0; bysecond=0;',
		end_date        => NULL,
		enabled         => TRUE,
		comments        => 'Automatically set audit last archive time.');
	END;
	/
	"
	
	echo Setting audit_trail to DB,EXTENDED
	sqlplus_sysdba "alter system set audit_trail = DB,EXTENDED scope = spfile;"
else
	echo "Unknown confidentiality setting $STIG_DB_CONFIDENTIALITY"
	exit 1
fi

echo DBA_AUDIT_MGMT_CLEAN_EVENTS:
sqlplus_sysdba "SELECT * FROM DBA_AUDIT_MGMT_CLEAN_EVENTS;"
echo DBA_AUDIT_MGMT_CLEANUP_JOBS:
sqlplus_sysdba "SELECT * FROM DBA_AUDIT_MGMT_CLEANUP_JOBS;"
echo DBA_AUDIT_MGMT_CONFIG_PARAMS:
sqlplus_sysdba "SELECT * FROM DBA_AUDIT_MGMT_CONFIG_PARAMS;"

echo Audit jobs:
sqlplus_sysdba "SELECT job_action
FROM   dba_scheduler_jobs
WHERE  job_name LIKE 'AUDIT%';"

echo Audit Tablespaces:
sqlplus_sysdba "SELECT table_name, tablespace_name
FROM   dba_tables
WHERE  table_name = 'AUD\$'
OR table_name = 'FGA_LOG\$';"

echo Turning on auditing
sqlplus_sysdba "alter system set audit_sys_operations = TRUE scope = spfile;"

restart_oracle

echo Recompile views and synonyms...
sqlplus_sysdba "alter view SYS.DBA_FGA_AUDIT_TRAIL compile;"
sqlplus_sysdba "alter view SYS.DBA_COMMON_AUDIT_TRAIL compile;"
sqlplus_sysdba "alter PUBLIC synonym DBA_FGA_AUDIT_TRAIL compile;"
sqlplus_sysdba "alter PUBLIC synonym DBA_COMMON_AUDIT_TRAIL compile;"
