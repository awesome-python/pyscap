#!/bin/bash

. lib/oracle.sh

fail "The DBMS does not have configured all applicable settings to use trusted files, functions, features, or other components during startup, shutdown, aborts, or other unplanned interruptions: datafiles are checked against the control files on start up, but configuration files are not protected"