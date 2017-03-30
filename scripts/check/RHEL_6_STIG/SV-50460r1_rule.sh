#!/bin/bash
. lib/general.sh

if [[ ! -s /etc/crypttab ]]; then
	fail "The operating system must employ cryptographic mechanisms to protect information in storage: /etc/crypttab doesn't exist or has no entries"
fi

# mainline cryptoloop is not secure, so we don't test for it

if ! which dmsetup > /dev/null; then
	fail "The operating system must employ cryptographic mechanisms to protect information in storage: dmsetup is not in PATH"
fi
if ! which cryptsetup > /dev/null; then
	fail "The operating system must employ cryptographic mechanisms to protect information in storage: cryptsetup is not in PATH"
fi

if [[ "x$(dmsetup targets | grep crypt)" = "x" ]]; then
	fail "The operating system must employ cryptographic mechanisms to protect information in storage: crypt device-mapper target doesn't exist"
fi

if [[ "$(dmsetup ls --target crypt | wc -l)" -le 0 ]]; then
	fail "The operating system must employ cryptographic mechanisms to protect information in storage: no crypt devices found"
done

pass
