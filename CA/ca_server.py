#!/usr/bin/env python3
import pika
from os import path
import datetime
from OpenSSL.crypto import verify # verifying function doesn't exist in cryptography module
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
'''
Scenario
* Generate key / load it
* Receive the certificate request / load it (network)
* Check and sign it
* Send it back / save it to disk
'''
CA_CERT_PATH = 'certificate_ca.pem'
CA_KEY_PATH = 'key_ca.pem'
cert = None
key = None
def generate_or_load():
    global cert
    global key
    if(path.isfile(CA_CERT_PATH) and path.exists(CA_CERT_PATH) and path.isfile(CA_KEY_PATH) and path.exists(CA_KEY_PATH)):
        # load files
        print('Loading !')
        cert = x509.load_pem_x509_certificate(open(CA_CERT_PATH,'rb').read(), default_backend())
        print(cert)
        key = serialization.load_pem_private_key(open(CA_KEY_PATH,'rb').read(),password=None,backend=default_backend())
    else:
        print('Generating !')
        # generate key and self signed cert
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=3072,
            backend=default_backend()
        )   # Save it to disk
        with open(CA_KEY_PATH, "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption() # for programming reasons (no prompting)
            ))
            # Making a self signed certificate 
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"TN"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Tunis"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"Insat"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"TalkyWalky"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"TalkyWalky"),
        ])
        cert = x509.CertificateBuilder().subject_name(
            subject
            ).issuer_name(
            issuer
            ).public_key(
            key.public_key()
            ).serial_number(
            x509.random_serial_number()
            ).not_valid_before(
            datetime.datetime.utcnow()
            ).not_valid_after(
            # Our CA certificate will be valid for 9125 days ~ 25 years
            datetime.datetime.utcnow() + datetime.timedelta(days=9125)
        ).sign(key, hashes.SHA256(), default_backend())
        # Write our certificate out to disk.
        with open(CA_CERT_PATH, "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
    return (key,cert)

def handle_cert_req(CSR_PATH):
    if(path.exists(CSR_PATH) and path.isfile(CSR_PATH)):
        # loading certification request
        print('Handling request')
        csr = x509.load_pem_x509_csr(open(CSR_PATH,'rb').read(),default_backend())
        cert_client = x509.CertificateBuilder().subject_name(
            csr.subject
            ).issuer_name(
            cert.subject
            ).public_key(
            csr.public_key()
            ).serial_number(
            x509.random_serial_number()
            ).not_valid_before(
            datetime.datetime.utcnow()
            ).not_valid_after(
            # Our CA certificate will be valid for 7 day
            datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )
        for ext in csr.extensions:
            cert_client.add_extension(ext.value,ext.critical)
        
        cert_client = cert_client.sign(key, hashes.SHA256(), default_backend())  
        with open('client_cert.pem','wb') as f:
            f.write(cert_client.public_bytes(serialization.Encoding.PEM))      
    else:
        print('No Request to handle')

def handle_req(reqData,cert):
    csr = x509.load_pem_x509_csr(reqData,default_backend())
    cert_client = x509.CertificateBuilder().subject_name(
            csr.subject
            ).issuer_name(
            cert.subject
            ).public_key(
            csr.public_key()
            ).serial_number(
            x509.random_serial_number()
            ).not_valid_before(
            datetime.datetime.utcnow()
            ).not_valid_after(
            # Our CA certificate will be valid for 7 day
            datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )
    for ext in csr.extensions:
        cert_client.add_extension(ext.value,ext.critical)
        
    cert_client = cert_client.sign(key, hashes.SHA256(), default_backend())  
    return    cert_client.public_bytes(serialization.Encoding.PEM).decode()
def handle_cert():
    if(path.exists('client_cert.pem') and path.isfile('client_cert.pem')):
        pass
    else:
        print('No certification exists for client')
    pass

# First step is created a ROOT certificate (self signed certificate for the authority)
#generate_or_load()

# Second is handling any certificate request and sign it using the ROOT certificate
#andle_cert_req('client_csr.pem')



class CaServer:
    
    def generate_authority_key(self):
        self.ca_key,self.ca_cert = generate_or_load()
        
    def connect(self):
        self.generate_authority_key()
        self.connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.receive()
    def send(self,client_queue,reqData):

        self.channel.exchange_declare(exchange='cert_exchange', exchange_type='direct')
        self.channel.queue_declare(queue=client_queue, durable=True)

        message = handle_req(reqData,self.ca_cert)
        self.channel.basic_publish(
            exchange='cert_exchange',
            routing_key=client_queue,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print('Server sended cert to '+str(client_queue))

    def receive(self):
        self.channel.queue_declare(queue='cert_req_queue', durable=True)

        def callback(ch, method, properties, body):
            print(body)
            client_queue, cert_req = body.decode().split(':')
            cert_req = cert_req.encode()
            print('Server Dealing with '+str(client_queue))
            self.send(client_queue,cert_req)
            ch.basic_ack(delivery_tag=method.delivery_tag)
            

        
        self.channel.basic_consume(queue='cert_req_queue', on_message_callback=callback)
        print('Server Started !! Listening')
        self.channel.start_consuming()


server = CaServer()
server.connect()