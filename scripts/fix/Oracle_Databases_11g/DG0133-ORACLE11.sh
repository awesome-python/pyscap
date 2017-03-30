#!/bin/bash

e=$(echo "SET LINESIZE 1024;
SET PAGESIZE 0;
alter profile default limit password_lock_time unlimited;
EXIT" | su -l oracle -c "sqlplus -L -S '/ AS SYSDBA'")

# TODO alter profile [profile name] limit password_lock_time default;