#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'fremovexattr'
echo '<result>pass</result>'
