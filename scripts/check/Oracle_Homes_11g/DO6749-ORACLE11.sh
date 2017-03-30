#!/bin/bash

. lib/oracle.sh

q=$(sqlplus_sysdba "select value from v\$parameter where name = 'sec_max_failed_login_attempts';")
if [[ "$q" = 0 || "$q" -gt 3 ]]; then
	fail "The Oracle SEC_MAX_FAILED_LOGIN_ATTEMPTS parameter is not set to an IAO-approved value between
1 and 3: $q"
fi

pass
