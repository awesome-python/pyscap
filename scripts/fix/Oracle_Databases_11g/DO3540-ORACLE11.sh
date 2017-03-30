#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "alter system set sql92_security = TRUE scope = spfile;"

restart_oracle