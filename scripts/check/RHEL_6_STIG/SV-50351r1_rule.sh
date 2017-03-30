#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'fchmodat'
echo '<result>pass</result>'
