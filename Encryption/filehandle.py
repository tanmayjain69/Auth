import io
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import ipfsapi
import os

from Encryption.Encrypt import get_private_key
if(first_time==1):
    get_private_key()
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
p_key = private_key.public_key()
pem = p_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
try:
    api=ipfsapi.connect('127.0.0.1',5001)
    print("Connection to the server established")


    print("Enter the site url")
    url=str(input())
    url=str.encode(url)
    print("Enter user Name")
    user_name=input()
    user_name=str.encode(user_name)
    print("Enter Password")
    password=input()

    encrypted_password = p_key.encrypt(
        password,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    encrypted_url = p_key.encrypt(
        url,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(encrypted_url)


    # print(original_message.decode())
    encrypted_username = p_key.encrypt(
        user_name,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    site=api.add_str(encrypted_url) #hash of the site url
    pkey_object=api.object_patch_append_data(site,io.BytesIO(pem))
    pass_object=api.object_patch_append_data(site,io.BytesIO(encrypted_password))
    user_name_object = api.object_patch_append_data(site, io.BytesIO(encrypted_username))


    # print(api.object_get('QmWfVY9y3xjsixTgbd9AorQxH7VtMpzfx2HaWtsoUYecaX'))




except ipfsapi.exceptions.ConnectionError as ce:
    print(str(ce))