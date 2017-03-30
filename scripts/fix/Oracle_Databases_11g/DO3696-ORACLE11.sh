#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "alter system set resource_limit = TRUE scope = both;"