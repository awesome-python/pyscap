#!/bin/bash

cat fix/Oracle_Databases_11g/oracle_audit_dod.sql | su -l oracle -c "sqlplus -L -S '/ AS SYSDBA'"
