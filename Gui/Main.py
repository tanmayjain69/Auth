from tkinter import *
import os

creds = 'tempfile.txt'

# def register_user():
#     username_info=username.get()
#     password_info=password.get()
#
#     file=open(username_info+".txt","w")
#     file.write(username_info+"\n")
#     file.write(password_info+"\n")
#     file.close()
#
#     username_entry.delete(0,END)
#     password_entry.delete(0,END)
#
#     Label(screen_reg,text="Sign up Success",fg="green",font=("calibri",11)).pack()
# def register():  #regestration screen
#     global screen_reg
#     screen_reg=Toplevel(screen)
#     screen_reg.title("Sign Up")
#     screen_reg.geometry("300x250")
#
#     global username,username_entry  #global variable to use outside function
#     global password, password_entry
#     username=StringVar()
#     password=StringVar()
#
#
#     Label(screen_reg, text="Enter You Desired Details * ").pack()
#     Label(screen_reg, text="").pack()
#     Label(screen_reg,text="Username * ").pack()
#     username_entry= Entry(screen_reg,textvariable=username)
#     username_entry.pack()
#     Label(screen_reg,text="Password * ").pack()
#     password_entry = Entry(screen_reg,textvariable=password)
#     password_entry.pack()
#     Label(screen_reg, text="").pack()
#     Button(screen_reg,text="Sign Up", height="1", width="10",command=register_user()).pack()
#
#
# def login():
#     print("LOgged in")
#
# def main_screen():
#     global screen  #to acces from another function
#     screen=Tk()  #main object for tkinter
#     screen.geometry("300x250")
#     screen.title("SmartSafe")
#     Label(text="Safe 1.0",bg="light blue",width="300",height="2",font=("Calibri",13)).pack()
#     Label(text="").pack()
#     Button(text="Login",height="2",width="30",command=login).pack()
#     Label(text="").pack()
#     Button(text="Sign Up",height="2",width="30",command=register).pack()
#     screen.mainloop()
# main_screen()
def Signup():
    global pwordE
    global nameE
    global roots

    roots = Tk()
    roots.title('Signup')
    instruction = Label(roots, text='Please Enter new Credentials')
    instruction.grid(row=0, column=0, sticky=E)

    nameL = Label(roots, text='New Username: ')
    pwordL = Label(roots, text='New Password: ')
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)

    signupButton = Button(roots, text='Signup', command=FSSignup)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()

def main_screen():
    global screen  #to acces from another function
    screen=Tk()  #main object for tkinter
    screen.geometry("300x250")
    screen.title("SmartSafe")
    Label(text="Safe 1.0",bg="light blue",width="300",height="2",font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",height="2",width="30",command=Login).pack()
    Label(text="").pack()
    Button(text="Sign Up",height="2",width="30",command=Signup).pack()
    screen.mainloop()
def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()


def Login():
    global nameEL
    global pwordEL
    global rootA

    rootA = Tk()

    rootA.title('Login')

    instruction = Label(rootA, text='Please Login\n')
    instruction.grid(columnspan=5)

    nameL = Label(rootA, text='Username:')
    pwordL = Label(rootA, text='Password:')
    nameL.grid(row=1,columnspan=5, column=3)
    pwordL.grid(row=3, columnspan=5, column=3)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=2, columnspan=5, column=3)
    pwordEL.grid(row=4, columnspan=5, column=3)

    loginB = Button(rootA, text='Login', command=CheckLogin)
    loginB.grid(columnspan=25, column=5)

    rmuser = Button(rootA, text='Sign Up', fg='red', command=Signup)
    rmuser.grid(columnspan=25, column=5)
    rootA.mainloop()


def CheckLogin():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.title(':D')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[+] Logged In')
        rlbl.pack()
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[! Invalid Login')
        rlbl.pack()
        r.mainloop()


def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()

main_screen()
