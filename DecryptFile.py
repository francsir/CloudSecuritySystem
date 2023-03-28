from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend


def Decrypt(filename, private_key_filename):
    with open(private_key_filename, 'rb') as f:
        private_key = serialization.load_pem_private_key(f.read(), password = None, backend = default_backend())

    with open(filename, 'rb') as f:
        cipher = f.read()

    plaintext = private_key.decrypt(cipher, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    with open(filename + '.decrypted', 'wb') as f:
        f.write(plaintext)
