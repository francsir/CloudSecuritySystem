from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def encrypt(filename, public_key_filename):
    with open(public_key_filename, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=,)
