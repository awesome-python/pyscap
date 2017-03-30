#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "DELETE FROM AUD\$;"

notchecked "The DBMS audit logs are not included in backup operations"