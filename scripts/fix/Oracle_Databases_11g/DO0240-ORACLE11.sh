#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "alter system set os_roles = FALSE scope = spfile;"

restart_oracle