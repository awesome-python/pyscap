#!/bin/bash

echo $(cat fix/Oracle_Databases_11g/oracle_verify_password_dod.sql | su -l oracle -c "sqlplus -L -S 'sys/MANAGER AS SYSDBA'")

echo Looking for verify_password_dod function in dba_procedures
echo $(echo "set heading off;
select OBJECT_NAME, procedure_name
from sys.DBA_PROCEDURES
where object_name = 'VERIFY_PASSWORD_DOD'
order by procedure_name;
EXIT" | su -l oracle -c "sqlplus -L -S '/ AS SYSDBA'")
