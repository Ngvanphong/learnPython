from tkinter import *
from tkinter import messagebox
def btnLogin_click():
    user= tbUsername.get()
    passw= tbPassword.get()
    if(user=="admin" and passw=="1"):
        messagebox.showinfo("Infor","Success")
    else:
        messagebox.showinfo("error","Have a error")

frmLogin=Tk()
frmLogin.title("Form Login")
lable1= Label(frmLogin,text="UserName",font= ("Arial",16))
lable1.pack()
tbUsername= Entry(frmLogin,width=30,font=("Arial",16))
tbUsername.pack()
lable2= Label(frmLogin,text="Password",font=("Arial",16))
lable2.pack()
tbPassword= Entry(frmLogin,width=30,font=("Arial",16))
tbPassword.pack()
btnLogin= Button(frmLogin,text="Login",font=("Arial",16),command=btnLogin_click)

btnLogin.pack()

frmLogin.mainloop()

