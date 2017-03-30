#!/bin/bash

. lib/oracle.sh
. lib/db.sh

notchecked "DBMS tools or applications that echo or require a password entry in clear text are not protected from password
display"