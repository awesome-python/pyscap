#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'adjtimex'
echo '<result>pass</result>'
