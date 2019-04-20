import io
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import ipfsapi
import os

from Encryption.Encrypt import get_private_key
# if(first_time==1):
# #     get_private_key()
def save_with_url(url,user_name,password):
    path='C:\\Users\Arnav\PycharmProjects\Auth\Encryption\private_key.pem'
    with open(path, "rb") as key_file:
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

        # print("Enter the site url")
        # url=str(input())
        url=str.encode(url)
        # print("Enter user Name")
        # user_name=input()
        user_name=str.encode(user_name)
        # print("Enter Password")
        # password=input()
        password=str.encode(password)

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

        # print(original_message.decode())
        encrypted_username = p_key.encrypt(
            user_name,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        combined_encrytped=encrypted_username+encrypted_password+pem
        combined_object=api.add_bytes(combined_encrytped)
       #url insert into databse

        print(private_key.decrypt(
            api.cat(combined_object)[:256],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )))
        print(private_key.decrypt(
            api.cat(combined_object)[256:512],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )))
        print(api.cat(combined_object)[512:963])
        if(pem==api.cat(combined_object)[512:963]):
            print("Public key is retrived successfully")


        # print(api.ls(link_obj))



    except ipfsapi.exceptions.ConnectionError as ce:
        print(str(ce))
def save(name,user_name,password):
    path='C:\\Users\Arnav\PycharmProjects\Auth\Encryption\private_key.pem'
    with open(path, "rb") as key_file:
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

        # print("Enter the site url")
        # url=str(input())
        name=str.encode(name)
        # print("Enter user Name")
        # user_name=input()
        user_name=str.encode(user_name)
        # print("Enter Password")
        # password=input()
        password=str.encode(password)

        encrypted_password = p_key.encrypt(
            password,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_url = p_key.encrypt(
            name,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # print(original_message.decode())
        encrypted_username = p_key.encrypt(
            user_name,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        combined_encrytped=encrypted_username+encrypted_password+pem
        combined_object=api.add_bytes(combined_encrytped)
       #url insert into databse

        print(private_key.decrypt(
            api.cat(combined_object)[:256],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )))
        print(private_key.decrypt(
            api.cat(combined_object)[256:512],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )))
        print(api.cat(combined_object)[512:963])
        if(pem==api.cat(combined_object)[512:963]):
            print("Public key is retrived successfully")


        # print(api.ls(link_obj))



    except ipfsapi.exceptions.ConnectionError as ce:
        print(str(ce))