#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'os_roles';")
if [[ $e =~ FALSE ]]; then
	pass
fi

fail "The Oracle OS_ROLES parameter is not set to FALSE"