from tkinter import *
import os
import time
from firebase import firebase
from Encryption.filehandle import save,save_with_url


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
    username_lable = Label(register_screen, text="Username * ")
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
    with open("current.txt","r") as f:
        dele=f.read().splitlines()
        username=dele[0]

        list_of_files = os.listdir()
        f.close()
        if username in list_of_files:
            os.remove(username)
            os.remove("current.txt")

    main_account_screen()




def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r+")
        verify = file1.read().splitlines()
        if password1 in verify:
            with open("current.txt","w") as f:
                f.seek(0)  # <- This is the missing piece
                f.truncate()
                f.write(username1+"\n")
                f.write(password1)
                f.close()
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()



def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()



def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login():
    login_screen.destroy()

def delete_login_success():
    login_success_screen.destroy()
    delete_login()
    main_screen_delete()
    in_main_screen()
def main_screen_delete():
    main_screen.destroy()

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
def in_main_screen():
    global in_main_screen
    in_main_screen=Tk()
    in_main_screen.geometry("300x250")
    in_main_screen.title("Block-It v1.0")
    Label(in_main_screen,text="Main Menu", bg="light blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(in_main_screen,text="").pack()
    Button(in_main_screen,text="Enter  new credentials with url",bg="#ffa8a8",command=cred_url_screen).pack()
    Label(in_main_screen,text="").pack()
    Button(in_main_screen,text="Enter  new credentials without url",bg="#ff9b9b").pack()
    Label(in_main_screen,text="").pack()

    Button(in_main_screen,text="Delete User",command=delete_user).pack()
    in_main_screen.mainloop()
def in_main_screen_destroy():
    del in_main_screen



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
    ui = user.get()

    pi = pwd.get()
    url_info=url.get()
    save_with_url(url_info,ui,pi) #storin it in ipfs

    file = open(ui, "w")
    file.write(url_info+"\t"+ui + "\t"+pi)
    file.close()

    user_entry.delete(0, END)
    pwd_entry.delete(0, END)
    url_entry.delete(0, END)

    suc=Label(cred_url_screen, text="Site Added", fg="green", font=("calibri", 11))
    suc.pack()

    suc.place_forget()

main_account_screen()