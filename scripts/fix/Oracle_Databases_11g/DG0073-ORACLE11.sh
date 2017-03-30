#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "alter profile default limit
failed_login_attempts 3;"