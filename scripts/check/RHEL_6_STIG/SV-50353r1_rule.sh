#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'fchown'
echo '<result>pass</result>'
