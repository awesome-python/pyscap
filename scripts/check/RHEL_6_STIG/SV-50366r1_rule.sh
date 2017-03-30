#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'setxattr'
echo '<result>pass</result>'
