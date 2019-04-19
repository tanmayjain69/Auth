from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#genrating keys
#if the user is signing up for the first time this part will run to genrate public
#and private key unique to that user
def get_private_key():
    userprivate_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    pem = userprivate_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open('private_key.pem', 'wb') as f:
        f.write(pem)





# pem = private_key.private_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PrivateFormat.PKCS8,
#     encryption_algorithm=serialization.NoEncryption()
# )
#
# with open('private_key.pem', 'wb') as f:
#     f.write(pem)
# pem = public_key.public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )
#
# with open('public_key.pem', 'wb') as f:
#     f.write(pem)
#
#
# with open("private_key.pem", "rb") as key_file:
#     private_key = serialization.load_pem_private_key(
#         key_file.read(),
#         password=None,
#         backend=default_backend()
#     )
# with open("public_key.pem", "rb") as key_file:
#     public_key = serialization.load_pem_public_key(
#         key_file.read(),
#         backend=default_backend()
#     )

#
# message = b'sad me!'
# encrypted = public_key.encrypt(
#     message,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )
# print(len(encrypted))
# print(encrypted)
# parts = [encrypted[i:i+64] for i in range(0, len(encrypted), 64)]
# print("jud gyeeee")
# print(b"".join(parts))
#
# for a in parts:
#     print(a)
# original_message = private_key.decrypt(
#     encrypted,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )



    

