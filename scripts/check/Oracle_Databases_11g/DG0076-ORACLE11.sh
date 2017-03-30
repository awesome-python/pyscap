#!/bin/bash

. lib/oracle.sh

fail "Sensitive information from production database exports remains unmodified after import to a development
database"
