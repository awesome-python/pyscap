#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'removexattr'
echo '<result>pass</result>'
