#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "ALTER SYSTEM SET JOB_QUEUE_PROCESSES = 10;"
sqlplus_sysdba "exec dbms_scheduler.set_scheduler_attribute('max_job_slave_processes', 10);"
sqlplus_sysdba "audit execute on dbms_scheduler by access;"
sqlplus_sysdba "audit execute on DBMS_JOB by access;"