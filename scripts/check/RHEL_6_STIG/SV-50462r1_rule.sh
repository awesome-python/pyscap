#!/bin/bash
. lib/general.sh

if [[ ! -s /etc/crypttab ]]; then
	fail "The operating system must protect the confidentiality and integrity of data at rest: /etc/crypttab doesn't exist or has no entries"
fi

# mainline cryptoloop is not secure, so we don't test for it

if ! which dmsetup > /dev/null; then
	fail "The operating system must protect the confidentiality and integrity of data at rest: dmsetup is not in PATH"
fi
if ! which cryptsetup > /dev/null; then
	fail "The operating system must protect the confidentiality and integrity of data at rest: cryptsetup is not in PATH"
fi

if [[ "x$(dmsetup targets | grep crypt)" = "x" ]]; then
	fail "The operating system must protect the confidentiality and integrity of data at rest: crypt device-mapper target doesn't exist"
fi

if [[ "$(dmsetup ls --target crypt | wc -l)" -le 0 ]]; then
	fail "The operating system must protect the confidentiality and integrity of data at rest: no crypt devices found"
done

pass
