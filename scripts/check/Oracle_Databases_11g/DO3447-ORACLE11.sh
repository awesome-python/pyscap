#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'os_authent_prefix';")
if [[ $e =~ ^[oO][pP][sS]\$$ ]]; then
	fail "The Oracle OS_AUTHENT_PREFIX parameter is set to the default value of OPS\$:
$e"
fi

pass
