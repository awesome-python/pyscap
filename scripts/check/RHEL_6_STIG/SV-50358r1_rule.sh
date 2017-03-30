#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'fsetxattr'
echo '<result>pass</result>'
