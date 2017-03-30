#!/bin/bash

. lib/oracle.sh

r=$(grep -i dba /etc/group | \cut -d: -f4)
fail "OS DBA group membership has not been restricted to authorized accounts:
$r"
