#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'lremovexattr'
echo '<result>pass</result>'
