#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'unlink'
not_auditing_syscall_fail 'unlinkat'
not_auditing_syscall_fail 'rename'
not_auditing_syscall_fail 'renameat'

echo '<result>pass</result>'