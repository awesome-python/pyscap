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

import logging
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography import utils
from cryptography.hazmat.primitives import hashes
import socket
import os
import datetime

# logger setup
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(ch_formatter)
rootLogger.addHandler(ch)

logger = logging.getLogger(__name__)

hostname = socket.gethostname()
fqdn = socket.gethostbyaddr(socket.gethostname())[0]

# Generate our key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Write our key to disk for safe keeping
with open("ca_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

def random_serial_number():
    return utils.int_from_bytes(os.urandom(20), "big") >> 1

# Various details about who we are. For a self-signed certificate the
# subject and issuer are always the same.
subject = issuer = x509.Name([
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
    private_key.public_key()
).serial_number(
    # x509.random_serial_number()
    random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.utcnow() + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(fqdn)]),
    critical=False,
# Sign our certificate with our private key
).sign(private_key, hashes.SHA256(), default_backend())

# Write our certificate out to disk.
with open("ca_cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))
