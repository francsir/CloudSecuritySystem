from cryptography import x509
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
import datetime
import uuid


class cert:
    def __init__(self, subject):
        ca_priv, ca_pub = generate_rsa_key_pair()
        self.ca_subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, subject)])
        ca_certificate = generate_self_signed_certificate(ca_priv, ca_pub, self.ca_subject, self.ca_subject)
        with open("./CA_CERT/CA.pem", "wb") as f:
            f.write(ca_certificate.public_bytes(Encoding.PEM))
        pem_data = ca_priv.private_bytes(encoding=Encoding.PEM, format=PrivateFormat.PKCS8, encryption_algorithm=NoEncryption())
        
        with open("./CA_CERT/CA", 'wb') as f:
            f.write(pem_data)

def authenticate_user():
        with open("./CA_CERT/CA.pem", "rb") as f:
            ca_cert_pem = f.read()
        with open("./UsersPubKeys/PutCertHere.pem", "rb") as f:
            client_cert_pem = f.read()

        try:
            client_cert = x509.load_pem_x509_certificate(client_cert_pem)
            ca_cert = x509.load_pem_x509_certificate(ca_cert_pem)
            # Verify the user's certificate signature

            ca_public_key = ca_cert.public_key()
            ca_public_key.verify(
                client_cert.signature,
                client_cert.tbs_certificate_bytes,
                padding.PKCS1v15(),
                client_cert.signature_hash_algorithm,
            )

            return True
        except Exception as e:
            print(f"Authentication failed: {e}")
            return False

def save_to_file(data, filename, encoding=Encoding.PEM):
        with open("./UsersPubKeys/"+filename, "wb") as f:
            f.write(data.public_bytes(encoding))


def generate_user_certificate(username):
        user_priv, user_pub = generate_rsa_key_pair()
        user_subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, username)])
        
        with open("./CA_CERT/CA.pem", "rb") as f:
              pem_data = f.read()
        
        ca_cert = x509.load_pem_x509_certificate(pem_data)
        ca_subject = ca_cert.subject

        with open("./CA_CERT/CA", "rb") as f:
              pem_data = f.read()
        ca_private_key = load_pem_private_key(pem_data, password=None)

        user_certificate = generate_self_signed_certificate(ca_private_key, user_pub, user_subject, ca_subject)
        save_to_file(user_certificate, f"{username}.pem")
        return user_priv, user_pub

def generate_self_signed_certificate(private_key, public_key, subject, issuer, valid_days=365):
        builder = x509.CertificateBuilder()
        builder = builder.subject_name(subject)
        builder = builder.issuer_name(issuer)
        builder = builder.not_valid_before(datetime.datetime.utcnow())
        builder = builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=valid_days))
        builder = builder.serial_number(uuid.uuid4().int)
        builder = builder.public_key(public_key)
        builder = builder.add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True,
        )

        certificate = builder.sign(
            private_key=private_key, algorithm=hashes.SHA256(),
        )

        return certificate
    

def generate_rsa_key_pair(key_size=2048):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
        )
        public_key = private_key.public_key()
        return private_key, public_key