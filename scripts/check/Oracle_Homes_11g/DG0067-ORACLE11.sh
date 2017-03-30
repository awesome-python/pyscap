#!/bin/bash

. lib/oracle.sh
. lib/db.sh

notchecked "Database account passwords are not stored in encoded or encrypted format whether stored in database
objects, external host files, environment variables or any other storage locations"