#!/bin/bash

. lib/oracle.sh
. lib/file.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name='audit_trail';")
if [[ ! $e =~ TRUE||OS||XML ]]; then
	pass
fi

e=$(sqlplus_sysdba "select value from v\$parameter where name='audit_file_dest';")
#echo $e
if [[ ! -d $e ]]; then
	error "audit_file_dest directory is not found: $e"
fi

fail_if_world_readable $e

pass