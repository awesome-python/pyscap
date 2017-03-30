#!/bin/bash

. lib/oracle.sh

fail_if_no_ORACLE_HOME
q=$(opatch_inventory | grep 'Oracle Database 11g' | head -n1 | cut -c70-80)

notchecked "The latest security patches have not been installed: manual check, current version is $q"