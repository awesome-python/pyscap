#!/bin/bash

. lib/oracle.sh

q=$(sqlplus_sysdba "select value from v\$parameter where name = 'job_queue_processes';")
if [[ "$q" -gt 10 ]]; then
	fail "Database job/batch queues are not reviewed regularly to detect unauthorized database job submissions: job_queue_processes > 10"
fi

q=$(sqlplus_sysdba "select value from all_scheduler_global_attribute
where ATTRIBUTE_NAME = 'MAX_JOB_SLAVE_PROCESSES';")
if [[ "x$q" = "x" || "$q" -gt 10 ]]; then
	fail "Database job/batch queues are not reviewed regularly to detect unauthorized database job submissions: MAX_JOB_SLAVE_PROCESSES > 10"
fi

q=$(sqlplus_sysdba "select exe from dba_obj_audit_opts where object_name = 'DBMS_SCHEDULER';")
if [[ "x$q" != "xA/A" ]]; then
	fail "Database job/batch queues are not reviewed regularly to detect unauthorized database job submissions: DBMS_SCHEDULER is not audited"
fi

q=$(sqlplus_sysdba "select exe from dba_obj_audit_opts where object_name = 'DBMS_JOB';")
if [[ "x$q" != "xA/A" ]]; then
	fail "Database job/batch queues are not reviewed regularly to detect unauthorized database job submissions: DBMS_JOB is not audited"
fi

pass
