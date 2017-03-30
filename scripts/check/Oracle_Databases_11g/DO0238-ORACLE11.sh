#!/bin/bash

. lib/oracle.sh
. lib/file.sh

e=$(sqlplus_sysdba "select log_mode from v$database;")
if [[ $e =~ NOARCHIVELOG ]]; then
	pass
fi

e=$(sqlplus_sysdba "select value from v$parameter where name = 'log_archive_dest';")
if [[ $e =~ 'no rows selected' ]]; then
	fail "The directories assigned to the LOG_ARCHIVE_DEST* parameters are not protected from unauthorized
access"
fi

e=$(sqlplus_sysdba "select value from v$parameter where name LIKE 'log_archive_dest_%';")
if [[ $e =~ 'no rows selected' ]]; then
	fail "The directories assigned to the LOG_ARCHIVE_DEST* parameters are not protected from unauthorized
access"
fi

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'log_archive_dest';
select value from v\$parameter where name = 'log_archive_duplex_dest';
select value from v\$parameter where name LIKE 'log_archive_dest_%';")
for i in $e; do
	fail_if_world_readable $i "The directories assigned to the LOG_ARCHIVE_DEST* parameters are not protected from unauthorized
access"
done

pass