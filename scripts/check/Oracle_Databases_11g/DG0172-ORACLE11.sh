#!/bin/bash

. lib/oracle.sh

fail_if_ols_not_installed

e=$(sqlplus_sysdba "select * from DBA_SA_AUDIT_OPTIONS;")
if [[ $e =~ 'no rows selected' ]]; then
	fail "Security labels are not audited"
fi

pass