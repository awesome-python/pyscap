#!/usr/bin/env python

# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import socket
import os
import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509, utils
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID


SCANNER_HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]
AGENT_HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]

def random_serial_number():
    return utils.int_from_bytes(os.urandom(20), "big") >> 1

def gen_key():
    # Generate our key
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return key

def write_key(key, file_name):
    # Write our key to disk for safe keeping
    with open(file_name, "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))

def write_cert(cert, file_name):
    # Write our certificate out to disk.
    with open(file_name, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

def sign_cert(hostname, issuer, key, ca_key, ca_cert):
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, hostname),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        key.public_key()
    ).serial_number(
        # x509.random_serial_number()
        random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 days
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(hostname)]),
        critical=False,
    # Sign our certificate with our private key
    ).sign(ca_key, hashes.SHA256(), default_backend())

    return cert

def selfsign_ca_cert(hostname, issuer, key):
    cert = x509.CertificateBuilder().subject_name(
        x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
            x509.NameAttribute(NameOID.COMMON_NAME, hostname),
        ])
    ).issuer_name(
        issuer
    ).public_key(
        key.public_key()
    ).serial_number(
        # x509.random_serial_number()
        random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 days
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(hostname)]),
        critical=False,
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=None),
        critical=True,
    # Sign our certificate with our private key
    ).sign(key, hashes.SHA256(), default_backend())
    return cert

def write_cert_chain(cert_file_name, cert, ca_cert):
    with open(cert_file_name, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
        # add ca to cert chain
        f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

scanner_key = gen_key()
write_key(scanner_key, "scanner_key.pem")

# Various details about who we are. For a self-signed certificate the
# subject and issuer are always the same.
issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, SCANNER_HOSTNAME),
])

scanner_cert = selfsign_ca_cert(SCANNER_HOSTNAME, issuer, scanner_key)

write_cert(scanner_cert, "scanner_cert.pem")
write_cert(scanner_cert, "agent/scanner_cert.pem")

# normal generation; separate scanner/agent
# agent_key = gen_key_to_file("agent/agent_key.pem")
# agent_cert = sign_cert(AGENT_HOSTNAME, issuer, agent_key, scanner_key, scanner_cert)
# write_cert_chain("agent/agent_cert.pem", agent_cert, scanner_cert)

# all on localhost; can't generate different keys for same host
write_key(scanner_key, "agent/agent_key.pem")
write_cert(scanner_cert, "agent/agent_cert.pem")
