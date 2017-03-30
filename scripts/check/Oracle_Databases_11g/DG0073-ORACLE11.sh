#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select profile||': '||limit from dba_profiles,
(select limit as def_login_attempts from dba_profiles
where profile = 'DEFAULT'
and resource_name = 'FAILED_LOGIN_ATTEMPTS')
where resource_name = 'FAILED_LOGIN_ATTEMPTS'
and replace(limit, 'DEFAULT', def_login_attempts) IN
('UNLIMITED', NULL)
or resource_name = 'FAILED_LOGIN_ATTEMPTS'
and to_number(decode(limit, 'UNLIMITED', 10, 'DEFAULT', 10, limit)) > 3;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Database accounts should not specify account lock times less than the site-approved minimum:
$e"
fi
