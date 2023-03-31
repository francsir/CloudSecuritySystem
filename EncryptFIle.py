from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

def encrypt(filename, public_key_filename):
    with open("./publicKeys/"+public_key_filename, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend(),)

    with open(filename, 'rb') as f:
        plaintext = f.read()
    cipher = public_key.encrypt(plaintext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label = None,))

    with open(filename + '.encrypted', 'wb') as f:
        f.write(cipher)


