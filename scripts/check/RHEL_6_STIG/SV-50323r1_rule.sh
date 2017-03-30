#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'settimeofday'

echo '<result>pass</result>'

