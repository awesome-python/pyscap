#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'stime'
echo '<result>pass</result>'

