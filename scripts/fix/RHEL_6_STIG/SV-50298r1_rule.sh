#!/bin/bash

sh fix/RHEL_6_STIG/system_auth.sh || exit 1
sh fix/RHEL_6_STIG/system_auth_ac.sh || exit 1