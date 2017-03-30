#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'lchown'
echo '<result>pass</result>'
