#!/bin/bash

. lib/oracle.sh
. lib/file.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name='diagnostic_dest';")
if [[ ! -d $e ]]; then
	error "The directory assigned to the DIAGNOSTIC_DEST parameter should be protected from unauthorized access: diagnostic_dest directory is not found: $e"
fi

fail_if_world_readable $e "The directory assigned to the DIAGNOSTIC_DEST parameter should be protected from unauthorized access"

pass