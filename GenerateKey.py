from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generateKeys(key_number):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    priv_FileName = 'private_key.pem'+str(key_number)	
    with open("./privateKeys/"+priv_FileName, 'wb') as f:
       f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption(),))

    public_key = private_key.public_key()
    pubK_FileName = 'public_key.pem'+str(key_number)
    with open("./publicKeys/"+pubK_FileName, 'wb') as f:
        f.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo,))

    return (priv_FileName, pubK_FileName)


