import socket
import time
import subprocess
from Encryption.filehandle import fetch
from WebScraping.web import *

# import threading
from firebase import firebase
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()


fb = firebase.FirebaseApplication('https://login-ce190.firebaseio.com', None)
def recv():
    curr_logged_in=""
    while(True):

        curr_logged_in=fb.get("/current/",current_machine_id)
        if(curr_logged_in==None): continue
        else:
            host, port = "10.12.4.199", 1234
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                client.bind((host, port))
            finally:
                pass
            client.listen(5)  # how many connections can it receive at one time
            print("Start Listening...")
            curr_logged_in = fb.get("/current/", current_machine_id)
            while True:
                curr_logged_in = fb.get("/current/", current_machine_id)
                res = fb.get('/hash', curr_logged_in)
                conn, addr = client.accept()
                print("client with address: ", addr, " is connected.")

                data = conn.recv(1024)
                print(data.decode("utf-8")[2:])
                if(data[2:].decode()=="LMS"):
                    det = fetch(res["lms=bennett=edu=in"])
                    print(det['usname'].decode(),det['pwd'].decode())
                    lmsLogin(det['usname'].decode(),det['pwd'].decode())
                    client.close()
                    recv()


                elif (data[2:].decode() == "FB"):
                    det = fetch(res["www=facebook=com"])
                    fbLogin(det['usname'].decode(),det['pwd'].decode())
                    client.close()
                    recv()


                elif (data[2:].decode() == "HK"):
                    det = fetch(res["www=hackerrank=com=auth=login"])
                    hrLogin(det['usname'].decode(),det['pwd'].decode())
                    client.close()
                    recv()

recv()

