#!/bin/bash
. lib/packages.sh

# from https://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Managing_Smart_Cards/enabling-smart-card-login.html

# check required packages installed
# removed graphical requirements
for i in nss-tools esc pam_pkcs11 coolkey ccid gdm authconfig authconfig-gtk krb5-libs krb5-workstation krb5-auth-dialog krb5-pkinit-openssl; do
	fail_if_package_not_installed $i 'The system must be configured to require the use of a CAC, PIV compliant hardware token, or Alternate Logon Token (ALT) for authentication'
done

# check pam_pkcs11 config
if [[ ! -f /etc/pam_pkcs11/pam_pkcs11.conf ]]; then
	fail 'The system must be configured to require the use of a CAC, PIV compliant hardware token, or Alternate Logon Token (ALT) for authentication: /etc/pam_pkcs11/pam_pkcs11.conf does not exist'
fi

cp_lines=$(grep cert_policy /etc/pam_pkcs11/pam_pkcs11.conf | wc -l)
ocsp_lines=$(grep cert_policy /etc/pam_pkcs11/pam_pkcs11.conf | grep ocsp_on | wc -l)
if [[ "$cp_lines" != "$ocsp_lines" ]]; then
	fail 'The system must be configured to require the use of a CAC, PIV compliant hardware token, or Alternate Logon Token (ALT) for authentication: /etc/pam_pkcs11/pam_pkcs11.conf is not configured with ocsp_on for all cert_policy lines'
fi

# TODO check mapping configuration

# check pam gdm settings
if [[ -f /etc/pam.d/gdm ]]; then
	if [[ "x$(egrep '^auth\s+sufficient\s+pam_pkcs11.so' /etc/pam.d/gdm)" != "x" ]]; then
		fail "The system must be configured to require the use of a CAC, PIV compliant hardware token, or Alternate Logon Token (ALT) for authentication: /etc/pam.d/gdm is not configured for CAC usage"
	fi
fi

if [[ -f /etc/pam.d/gnome-screensaver ]]; then
	if [[ "x$(egrep '^auth\s+sufficient\s+pam_pkcs11.so' /etc/pam.d/gnome-screensaver)" != "x" ]]; then
		fail "The system must be configured to require the use of a CAC, PIV compliant hardware token, or Alternate Logon Token (ALT) for authentication: /etc/pam.d/gnome-screensaver is not configured for CAC usage"
	fi
fi

if [[ "x$(egrep '^auth\s+sufficient\s+pam_pkcs11.so' /etc/pam.d/common-auth)" != "x" ]]; then
	fail "The system must be configured to require the use of a CAC, PIV compliant hardware token, or Alternate Logon Token (ALT) for authentication: /etc/pam.d/common-auth is not configured for CAC usage"
fi

notchecked