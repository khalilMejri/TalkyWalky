#!/usr/bin/env python3
from os import path
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

'''
Scenario
* First : Create a RSA key
* Second : Create a Certificate Request
* Wait for validation
* Save it to Disk (currently , TODO: save it to ldap server)
'''


# Create private Key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=3072,
    backend=default_backend()
)  
# Save it to disk
with open("./client_key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption() 
    ))
# Create a cerificate request
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    # Provide various details about who we are.
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"TalkyWalky"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"User:username"),
])).add_extension(x509.BasicConstraints(ca=False,path_length=None),critical=True).sign(key, hashes.SHA256(), default_backend())
# Write our CSR out to disk.
with open("./client_csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))


def handle_cert(CERT_PATH):
    if(path.exists(CERT_PATH) and path.isfile(CERT_PATH)):
        cert_client = x509.load_pem_x509_certificate(open(CERT_PATH,'rb').read(),default_backend())
        print(dir(cert_client))
        print(cert_client.issuer,cert_client.version,cert_client.subject)
    else:
        print("there is no certificate issued for client")


handle_cert('client_cert.pem')