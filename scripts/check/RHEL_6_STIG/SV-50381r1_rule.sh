#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'init_module'
not_auditing_syscall_fail 'delete_module'

echo '<result>pass</result>'