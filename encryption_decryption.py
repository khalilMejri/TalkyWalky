from Crypto.PublicKey import RSA
from Crypto import Random #This one is important since it has the default function in RSA.generate() to generate random bytes!
from Crypto.Cipher import PKCS1_OAEP
import base64

#I'm leaving this function so that you understand how it works from encryption => decryption

def rsa_encrypt_decrypt():
    #Generating RSA key pair
    key = RSA.generate(2048)
    #Extracting private_key
    private_key = key.export_key('PEM')
    #Extracting public_key
    public_key = key.publickey().exportKey('PEM')
    #Get the message to send
    message = input('\nPlease enter your message for RSA encryption and decryption: ')
    #Encode the message
    message = str.encode(message)
    #Import the public key in order to use it for encryption
    rsa_public_key = RSA.importKey(public_key)
    #PKCS#1 OAEP is an asymmetric cipher based on RSA and the OAEP padding
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    #Finally encryption
    encrypted_message = rsa_public_key.encrypt(message)
    
    #Base64 encoding so that we can store it easily on DB/Server
    encrypted_message = base64.b64encode(encrypted_message)

    print('\nYour encrypted message is : ', encrypted_message)

    #DECRYPTION
    #Import private key
    rsa_private_key = RSA.importKey(private_key)
    #Apply the same magic trick again using PKCS1 OAEP
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)

    #Base64 decoding before decrypting, otherwise it would be incorrect, it's logical right? :)
    encrypted_message = base64.b64decode(encrypted_message)
    decrypted_message = rsa_private_key.decrypt(encrypted_message)

    print('\nYour message after decryption is : ', decrypted_message)

#THESE FUNCTIONS ARE THE ONES WE GONNA USE IN OUR FINAL APP
#How are we gonna get the public/private keys, I think that those are stored on the server
#So server will be able to get the proper key pair using users id maybe? or certificate?

#For the encrypt fct: sender calls it then sends the encrypted message to server along with the receiver's address
def rsa_encrypt(message, receiver_public_key):
    message = str.encode(message)
    rsa_public_key = RSA.importKey(receiver_public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_message = rsa_public_key.encrypt(message)
    encrypted_message = base64.b64encode(encrypted_message)
    return encrypted_message

#LOGICALLY, the server now has the encrypted message and will distribute it to the receiver
#For the decrypt fct: receiver calls it using his private key to get the initial message
def rsa_decrypt(encrypted_message, receiver_private_key):
    rsa_private_key = RSA.importKey(receiver_private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    encrypted_message = base64.b64decode(encrypted_message)
    decrypted_message = rsa_private_key.decrypt(encrypted_message)
    return decrypted_message

#FOR TESTING! SINCE WE DON'T HAVE RSA KEY PAIRS LOCALLY
#rsa_encrypt_decrypt()

# get rsa key from file
def get_rsa_key(filepath):
    with open(filepath, mode='rb') as private_file:
        priv_key_data = private_file.read()
        private_key = RSA.importKey(priv_key_data)
        #print(private_key.export_key())
        return private_key
