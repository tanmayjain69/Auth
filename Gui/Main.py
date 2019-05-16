from tkinter import *

import subprocess
import pyrebase
import multiprocessing
from threading import Thread
from firebase import firebase

curr_logged_in=""
config = {
  "apiKey": "AIzaSyCzWwwT2EVNV-PR4QFk3UVMXHT_P94C3FY",
  "authDomain": "login-ce190.firebaseapp.com",
  "databaseURL": "https://login-ce190.firebaseio.com/",
     "storageBucket": "login-ce190.appspot.com"
}

db = pyrebase.initialize_app(config)
fbbd = db.database()
auth=db.auth()
from Encryption.filehandle import save_with_url,fetch
# global fb
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

fb = firebase.FirebaseApplication('https://login-ce190.firebaseio.com', None)
# fb.put("/current/", current_machine_id, "none")


def register():
    global register_screen

    register_screen = Toplevel(main_screen)  #diffrent screens mean diffrent windows
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="light blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Email * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#ed9857", command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def delete_user():
    
    '''with open("current.txt","r") as f:
        dele=f.read().splitlines()
    #     username=dele[0]
    #
    #     list_of_files = os.listdir()
    #     f.close()
    #     if username in list_of_files:
    #         os.remove(username)
    #         os.remove("current.txt")'''
    #
    # fb.delete('/users/', curr_logged_in)

    main_account_screen()




def register_user():
    username_info = username.get()
    password_info = password.get()
    try:
        auth.create_user_with_email_and_password(username_info, password_info)
        user = auth.sign_in_with_email_and_password(username_info, password_info)
        curr_logged_in=username_info.translate ({ord(c): "=" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        f = open("curr.txt", "w+")
        f.write(curr_logged_in)
        f.close()
        print("reg",curr_logged_in)
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        register_screen.destroy()
        main_screen_delete()

        in_main_screen_func()
    except Exception as e:
        Label(register_screen, text="User Exists", fg="red", font=("calibri", 11)).pack()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()


    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    try:
        user = auth.sign_in_with_email_and_password(username1, password1)
        curr_logged_in = username1.translate ({ord(c): "=" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        f = open("curr.txt", "w+")
        f.write(curr_logged_in)
        f.close()
        print(curr_logged_in)
        fb.put("/current/", current_machine_id, curr_logged_in)
        login_sucess()
    except:
        password_not_recognised()


            

#LOGOUT
def logout():

    fb.delete('/current/', current_machine_id)
    # try:
    #     print(main_screen)
    # except:
    #     print("exce")
    #     in_main_screen.withdraw()
    #     main_account_screen()
    #
    # else:
    #     in_main_screen.withdraw()
    #     main_screen.deiconify()
    in_main_screen.withdraw()
    main_screen.deiconify()








# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def login_failed(e):
    global login_failed_screen
    login_failed_screen = Toplevel(login_screen)
    login_failed_screen.title("Success")
    login_failed_screen.geometry("150x100")
    Label(login_failed_screen, text=e).pack()
    Button(login_failed_screen, text="OK", command=delete_login_failed).pack()



def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def already_logged_in():
    global already_logged_in_screen
    already_logged_in_screen = Toplevel(login_screen)
    already_logged_in_screen.title("FAILED")
    already_logged_in_screen.geometry("150x100")
    Label(already_logged_in_screen, text="ALREADY LOGGED IN").pack()
    Button(already_logged_in_screen, text="OK", command=delete_already_logged_in).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login():
    login_screen.destroy()

def delete_login_failed():
    login_failed_screen.destroy()


def delete_already_logged_in():
    already_logged_in_screen.destroy()
def delete_parms():
    parms_screen.withdraw()

def main_screen_delete():
    main_screen.withdraw()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Block-It v1.0", bg="light blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


def in_main_screen_destroy():
    del in_main_screen
def in_main_screen_func():
    global in_main_screen


    in_main_screen=Tk()
    in_main_screen.geometry("400x350")
    in_main_screen.title("Block-It v1.0")
    Label(in_main_screen,text="Main Menu", bg="light blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(in_main_screen,text="").pack()
    Button(in_main_screen,text="Enter  new credentials with url",bg="#ffa8a8",command=cred_url_screen).pack()
    Label(in_main_screen,text="").pack()
    Button(in_main_screen,text="Enter  new credentials without url",bg="#ff9b9b").pack()
    Label(in_main_screen,text="").pack()
    Button(in_main_screen, text="View Creds", bg="#ff9b9b",command=view_info).pack()
    Label(in_main_screen, text="").pack()
    # Button(in_main_screen,text="Delete User",command=delete_user).pack()
    # Label(in_main_screen, text="").pack()
    Button(in_main_screen, text="sign-Out", command=logout).pack()


    in_main_screen.mainloop()



def  cred_url_screen():
    global cred_url_screen
    global url
    global pwd
    global user
    global pwd_entry
    global user_entry
    global url_entry
    url=StringVar()
    user = StringVar()
    pwd = StringVar()
    cred_url_screen=Toplevel(in_main_screen)
    cred_url_screen.geometry("300x250")
    cred_url_screen.title("Block-It v1.0")
    Label(cred_url_screen, text="Fill Every Box Below", bg="light blue", width="300", height="2", font=("Calibri", 13)).pack()
    user_lable = Label(cred_url_screen, text="Username * ")
    user_lable.pack()
    user_entry = Entry(cred_url_screen, textvariable=user)
    user_entry.pack()
    pwd_lable = Label(cred_url_screen, text="Password * ")
    pwd_lable.pack()
    pwd_entry = Entry(cred_url_screen, textvariable=pwd, show='*')
    pwd_entry.pack()
    url_label = Label(cred_url_screen, text="Url * ")
    url_label.pack()
    url_entry = Entry(cred_url_screen, textvariable=url)
    url_entry.pack()
    Label(cred_url_screen, text="").pack()
    Button(cred_url_screen, text="Verify and Add", width=10, height=1, bg="#ed9857", command=register_site).pack()

def register_site():
    f = open("curr.txt", "r")
    curr_logged_in = f.read()
    f.close()
    ui = user_entry.get()
    pi = pwd_entry.get()
    url_info=url_entry.get()
    print(curr_logged_in)
    url_info=url_info.translate ({ord(c): "=" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    print(url_info)
    save_with_url(url_info,ui,pi,curr_logged_in) #storin it in ipfs
    user_entry.delete(0, END)
    pwd_entry.delete(0, END)
    url_entry.delete(0, END)

    suc=Label(cred_url_screen, text="Site Added", fg="green", font=("calibri", 11))
    suc.pack()

    suc.place_forget()

#view
def parms():
    f = open("curr.txt", "r")
    curr_logged_in = f.read()
    f.close()
    global parms
    global parms_screen
    fb = firebase.FirebaseApplication('https://login-ce190.firebaseio.com', None)
    parms_screen = Toplevel(view_info)
    parms_frame=Frame(parms_screen)
    parms_frame.grid()

    parms_screen.attributes("-topmost", True)
    parms_screen.title("Credentials")
    parms_screen.geometry("250x200")

    res = fb.get('/hash', curr_logged_in)
    det=fetch(res[value])
    print(det)
    Label(parms_frame, text="USERNAME",bg="light blue").grid(row=1, column=5)
    Label(parms_frame, text=det['usname']).grid(row=3, column=5)
    Label(parms_frame, text="").grid(row=5, column=0)
    Label(parms_frame, text="Password", bg="light blue").grid(row=10, column=5)
    un=Entry(parms_frame,width=10)
    un.insert(0,det['pwd'])
    un.grid(row=15, column=5)
    # Text(parms, text=det['pwd']).pack()
    Button(parms_frame, text="OK", command=delete_parms).grid(row=5, column=5)
def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    global value
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    try:
        parms()
    except:
        parms_screen.deiconify()
        parms_screen.lift()
def delete_login_success():
    login_success_screen.destroy()
    delete_login()
    main_screen_delete()
    try:

        in_main_screen_func()
    except:
        in_main_screen.deiconify()

def view_info():
    f = open("curr.txt", "r")
    curr_logged_in=f.read()
    f.close()
    global view_info
    view_info = Tk()
    view_info.geometry("300x250")
    view_info.title("Block-It v1.0")
    lb = Listbox(view_info)
    print(curr_logged_in)
    try:
        res = fb.get('/hash', curr_logged_in)
        for key in res:
            lb.insert(END, key)
        lb.bind("<<ListboxSelect>>", onselect)
        lb.pack(pady=15)
    except:
        suc = Label(cred_url_screen, text="NO sites", fg="green", font=("calibri", 11))
        suc.pack()


def current_name():
    return curr_logged_in
if(fb.get("/current/",current_machine_id)==None):
    main_account_screen()
else:

    curr_logged_in=fb.get("/current/",current_machine_id)
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Block-It v1.0", bg="light blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.withdraw()

    in_main_screen_func()
# main_account_screen()
