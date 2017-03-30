#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = '_trace_files_public';")
if [[ $e =~ TRUE ]]; then
	fail "The Oracle _TRACE_FILES_PUBLIC parameter is present and not set to FALSE"
fi

pass
