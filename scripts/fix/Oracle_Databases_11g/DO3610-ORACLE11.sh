#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "audit rename on default by access;"
sqlplus_sysdba "audit update, delete on AUD\$ by access;"