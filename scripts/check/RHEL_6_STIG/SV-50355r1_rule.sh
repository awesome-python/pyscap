#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'fchownat'
echo '<result>pass</result>'
