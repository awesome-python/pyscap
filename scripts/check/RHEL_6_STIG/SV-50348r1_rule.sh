#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'fchmod'
echo '<result>pass</result>'
