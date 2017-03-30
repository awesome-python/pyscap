#!/bin/bash

. lib/oracle.sh

fail_if_oas_not_installed

error_if_no_ORACLE_HOME

if [ ! -f $ORACLE_HOME/network/admin/sqlnet.ora ]; then
	# ssl on by default
	return
fi

if [[ "x$(egrep -i '^\s*SQLNET.SSLFIPS_140\s*=\s*true' $ORACLE_HOME/network/admin/sqlnet.ora 2>/dev/null)" == "x" ]]; then
	fail "DBMS does not use NIST FIPS 140-2 validated cryptography"
fi


if [[ "x$(grep -Pizo '^\s*SSL_CIPHER_SUITES\s*=\s*\((SSL_RSA_WITH_AES_256_CBC_SHA|SSL_RSA_WITH_AES_128_CBC_SHA|SSL_RSA_WITH_3DES_EDE_CBC_SHA|SSL_RSA_WITH_RC4_128_SHA|SSL_RSA_WITH_RC4_128_MD5|SSL_RSA_WITH_DES_CBC_SHA|SSL_DH_anon_WITH_3DES_EDE_CBC_SHA|SSL_DH_anon_WITH_RC4_128_MD5|SSL_DH_anon_WITH_DES_CBC_SHA|\s*|,)+\)' $ORACLE_HOME/network/admin/sqlnet.ora 2>/dev/null)" == "x" ]]; then
	fail "DBMS does not use NIST FIPS 140-2 validated cryptography"
fi

pass