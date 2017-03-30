#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'lsetxattr'
echo '<result>pass</result>'
