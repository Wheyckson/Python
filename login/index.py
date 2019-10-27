#import libs
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

#============== Janela ========
jan = Tk()
jan.title("W Tech - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.9)
jan.iconbitmap(default="icons/logo1.ico")

#========== carregar img ==========
logo = PhotoImage(file="icons/logo.png")

#============== widgets =========
LeftFrame= Frame(jan, width=200 , height=300, bg="Navy",relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame= Frame(jan, width=395 , height=300, bg="grey11",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel= Label(LeftFrame, image=logo ,bg="Navy")
LogoLabel.place(x=-140,y=-5)
#
Titulo = Label(RightFrame, text=" Sign In ",font=("Century Gothic",30),bg="grey11",fg="white")
Titulo.place(x=110,y=10)

UserLabel = Label(RightFrame, text=" Username:",font=("Century Gothic",20),bg="grey11",fg="white")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=160,y=113)
#
UserLabel = Label(RightFrame, text=" Password :",font=("Century Gothic",20),bg="grey11",fg="white")
UserLabel.place(x=5,y=145)

PassEntry = ttk.Entry(RightFrame, width=30,show="♥")
PassEntry.place(x=160,y=157)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get() 

    database.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ? )
    """,(User,Pass))
    print("Selected") 
    VerifyLogin = database.cursor.fetchone()
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acess Confirmed, WELCOME !!")
    except:
            messagebox.showinfo(title="Login Info", message="Acess denied, Check the fields !") 

#Buttons
LoginButton = ttk.Button(RightFrame, text="Login",width=20, command=Login)
LoginButton.place(x=120 ,y=210)
#

def Register():
    #remove
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    Titulo.place(x=5000)
    #inserir
    NomeLabel = Label(RightFrame, text=" Name: ", font=("Century Gothic",20),bg="grey11", fg="white")
    NomeLabel.place(x=5,y=5)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=160,y=15)

    EmailLabel = Label(RightFrame, text=" E-mail: ", font=("Century Gothic",20),bg="grey11", fg="white")
    EmailLabel.place(x=5,y=55)

    EmailEntry = ttk.Entry(RightFrame,width=30)
    EmailEntry.place(x=160,y=66)
    
    def RegisterBD():
        #inserção BD
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if(Name == "" and Email == "" and User =="" and Pass == ""):
            messagebox.showerror(title="Registes Error", message="You didn't fill in all the fields ")
        else:            
            database.cursor.execute(""" 
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """,(Name, Email, User, Pass))
            #salva conteudo BD
            database.conn.commit()
            messagebox.showinfo(title="Register Info",message="Register Sucessful")

    Register = ttk.Button(RightFrame, text="Register",width=20, command=RegisterBD)
    Register.place(x=120 ,y=210)

    def Voltar():
        #remove
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        
        #Inserindo 
        LoginButton.place(x=120 )
        RegisterButton.place(x=120 )

    Back = ttk.Button(RightFrame, text="Back",width=20, command=Voltar)
    Back.place(x=120 ,y=250) 

RegisterButton = ttk.Button(RightFrame, text="Register",width=20, command=Register)
RegisterButton.place(x=120 ,y=250)

jan.mainloop()