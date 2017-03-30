#!/bin/bash

cat fix/Oracle_Databases_11g/oracle_logon_dod.sql | su -l oracle -c "sqlplus -L -S 'sys/MANAGER AS SYSDBA'"
