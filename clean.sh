#!/bin/bash

find scap -name '*.pyc' | xargs /bin/rm -f
rm -f *.pem
(
    cd agent
    bash clean.sh
)
