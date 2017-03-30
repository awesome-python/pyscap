#!/bin/bash

. lib/oracle.sh

fail_if_oas_not_installed

notchecked "Connections by mid-tier web and application systems to the Oracle DBMS are not protected, encrypted or authenticated according to database, web, application, enclave and network requirements:
$(sqlplus_sysdba "select name, ext_username from user\$ where ext_username <> NULL;")"