from tkinter import *
import tkinter as tk
from tkinter import messagebox
root=Tk()
root.title('Login Window')
root.geometry('1000x1000')

user=tk.StringVar()
passw=tk.StringVar()
l1=Label(root,text="Login Page",font=("arial",16,"bold")).pack(fill=BOTH)
l2=Label(root,text="Username : ").place(x=20,y=50)
l3=Label(root,text="Password : ").place(x=20,y=100)
t1=Entry(root,textvariable=user,width=20).place(x=100,y=50)
t2=Entry(root,textvariable=passw,width=20,show="*").place(x=100,y=100)

def clicked():
    #messagebox.showinfo("Say Hello", "Hello World")
    name=user.get()
    psw=passw.get()
    if name=='root' and psw=="pass":
        messagebox.showinfo("Login", " Login Successfully ")
    else:
        messagebox.showerror("Login","Incorrect username and password !!!")


btn=Button(root,text="Login",command=clicked).place(x=80,y=150)
root.mainloop()