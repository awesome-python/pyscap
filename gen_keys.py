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


CA_HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]
AGENT_HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]
SCANNER_HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]

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

def sign_cert(hostname, issuer, key, ca_key, ca_cert, cert_file_name):
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

    with open(cert_file_name, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
        # add ca to cert chain
        f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

    return cert

ca_key = gen_key()
write_key(ca_key, "ca_key.pem")
write_key(ca_key, "agent/ca_key.pem")

# Various details about who we are. For a self-signed certificate the
# subject and issuer are always the same.
issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, CA_HOSTNAME),
])

ca_cert = x509.CertificateBuilder().subject_name(
    x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, CA_HOSTNAME),
    ])
).issuer_name(
    issuer
).public_key(
    ca_key.public_key()
).serial_number(
    # x509.random_serial_number()
    random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.utcnow() + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(CA_HOSTNAME)]),
    critical=False,
).add_extension(
    x509.BasicConstraints(ca=True, path_length=None),
    critical=True,
# Sign our certificate with our private key
).sign(ca_key, hashes.SHA256(), default_backend())

write_cert(ca_cert, "ca_cert.pem")
write_cert(ca_cert, "agent/ca_cert.pem")

write_key(ca_key, "agent/agent_key.pem")
write_cert(ca_cert, "agent/agent_cert.pem")

write_key(ca_key, "scanner_key.pem")
write_cert(ca_cert, "scanner_cert.pem")

# # Generate our agent key
# agent_key = gen_key_to_file("agent_key.pem")
# agent_cert = sign_cert(AGENT_HOSTNAME, issuer, agent_key, ca_key, ca_cert, "agent_cert.pem")
#
# # Generate our scanner key
# scanner_key = gen_key_to_file("scanner_key.pem")
# scanner_cert = sign_cert(SCANNER_HOSTNAME, issuer, scanner_key, ca_key, ca_cert, "scanner_cert.pem")
